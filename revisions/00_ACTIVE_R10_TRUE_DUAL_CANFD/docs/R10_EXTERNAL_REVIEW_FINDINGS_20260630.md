# R10 external review findings — NOT FOR FAB — 2026-06-30

Status: **R10 is not fabrication-ready. Do not order R10 boards.**

The external review confirms that R10 fixed the major architectural error: it now uses two MCP2518FD CAN FD controllers between the Teensy 4.1 SPI bus and two MCP2562FD CAN FD transceivers. That is the correct high-level architecture for true dual CAN FD.

However, R10 must remain an inspection/review package only. A KiCad DRC-clean PCB is not enough here because the design is PCB-first, lacks an authoritative schematic, and still has power, protection, default-state, layout, and documentation blockers.

## Hard blockers before any JLCPCB order

1. Create a real `.kicad_sch` and run ERC from a schematic-driven KiCad project.
2. Fix TLIN1029 VSUP decoupling: C7 must decouple `+12V_PROTECTED` / U4 VSUP to GND, not `+5V_REGULATED`.
3. Add selectable/DNP LIN commander pull-up: `+12V_PROTECTED -> diode -> 1 kΩ -> LIN_BUS`, with a jumper/DNP that cannot bypass the 1 kΩ resistor.
4. Add `LIN_EN -> 100 kΩ -> GND` so the LIN transceiver defaults disabled during reset/boot.
5. Add safe-default CAN standby pull-ups: `CAN_A_STBY/XSTBY -> 10 kΩ -> +3.3 V` and `CAN_B_STBY/XSTBY -> 10 kΩ -> +3.3 V`.
6. Add SPI chip-select pull-ups: `CANFD_A_NCS -> 10 kΩ -> +3.3 V` and `CANFD_B_NCS -> 10 kΩ -> +3.3 V`.
7. Connect the LM2596 TO-263 thermal tab pad explicitly to GND.
8. Redo the buck/power routing with appropriate copper width and short input/switch/output current loops.
9. Add GND pours on both layers, with stitching vias and controlled return paths.
10. Move decoupling capacitors directly next to their IC power pins, preferably on the same side as each IC.
11. Move MCP2518FD crystal/load-cap networks next to U6/U7, ideally on the same side, and finalize crystal load capacitance instead of leaving `VERIFY_CL` values.
12. Resolve USB/VIN power isolation: at minimum document Teensy VUSB/VIN trace cut; preferably add a VIN selector or proper power-path/ideal-diode arrangement.
13. Add CAN A, CAN B, LIN, and K-line ESD/TVS protection near the connector/pigtail entry.
14. Reduce DIP-switch user-error risk: add hard silkscreen warnings/truth table and consider 1-of-N selection, jumper shunts, series resistors, or analog muxes for LIN/K and CAN routing.
15. Regenerate BOM from the schematic/PCB after these changes, then re-run ERC, DRC, Gerbers, drill, and package checks.

## Correct order guidance

Do **not** send `R10_TRUE_DUAL_CANFD_JLCPCB_GERBERS.zip` to JLCPCB.

Do **not** order R10 as-is.

Next manufacturable target should be **R10A/R11**, after the blockers above are fixed and verified.

## Current interpretation

R10 is a useful proof that the true dual-CAN-FD architecture is now correct. It is not a fabrication candidate.
