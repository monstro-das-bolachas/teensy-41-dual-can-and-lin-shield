# Teensy 4.1 CAN/LIN Interface for automotive diagnostics

This project contains a Teensy 4.1 based dual-CAN + LIN/K automotive interface for Mercedes S203/W203 learning and broader EU-market diagnostic/reverse-engineering use.

## Current active revision

Use R6.

R6 supersedes R5. R5 was a DRC-clean pigtail/DIP-switch layout, but the procurement audit found that it did not include the required external components for the LM2596 buck regulator. R6 adds the missing power-supply and decoupling components and updates the transceiver choices for Teensy 4.1 3.3 V logic.

Start here:

- `CURRENT_STATUS.md` — current truth/status
- `R6_PROCUREMENT_BOM_EU.md` — R6 procurement and ordering notes
- `BOM_R6_PROCUREMENT_EU.csv` — EU-capable procurement BOM with exact manufacturer part numbers
- `R5_PIGTAIL_DIPSWITCH_MANUFACTURING.md` — historical R5 pigtail/DIP-switch notes, superseded by R6

Authoritative R6 PCB:

- `teensy-41-can-lin-r6-complete-power-routed.kicad_pcb`

Preferred fabrication package:

- `r6_complete_power_fabrication_minimal_gerbers.zip`

DRC report:

- `reports/teensy-41-can-lin-r6-complete-power-routed-drc.rpt`

Preview SVGs:

- `previews/r6_complete_power_svg/`

Gerber/drill directory:

- `gerbers/r6_complete_power_fabrication_minimal/`

## Verification summary

R6 was generated with KiCad/pcbnew automation, routed with local FreeRouting, and verified with KiCad CLI.

Result:

- KiCad CLI: 10.0.3
- DRC violations: 0
- Unconnected pads: 0
- Footprint errors: 0
- Gerber/drill export: passed

## R6 key electrical decisions

- U2/U3 CAN transceivers: Microchip MCP2562FD-E/SN, using VIO on pin 5 tied to Teensy +3.3 V.
- U4 LIN transceiver: TI TLIN1029DRQ1, with open-drain RXD pulled up to +3.3 V by R1.
- U5 5 V regulator: LM2596S-5.0 with required external inductor, Schottky diode, bulk capacitors, and ceramic decoupling.
- J1 uses OBD2 pigtail/cable solder pads instead of a risky board-mounted OBD connector footprint.

## Configuration summary

SW1 selects CAN routing:

- 1+2: CAN A normal, OBD6/14
- 3+4: CAN A crossed, OBD6/14
- 5+6: CAN B normal, OBD3/11
- 7+8: CAN B crossed, OBD3/11

SW2 selects LIN/K source:

- 1: OBD7
- 2: OBD15
- 3: OBD1
- 4: OBD8
- 5: OBD9
- 6: OBD12
- 7: OBD13
- 8: AUX_LIN_K_IO

Rule: enable exactly one LIN/K source at a time.

## Safety

Before connecting to a vehicle:

1. Verify OBD cable pinout with a multimeter.
2. Assemble and bench-test the power section first.
3. Verify +5 V rail before installing the Teensy.
4. Confirm DIP switch settings.
5. Start with passive/read-only firmware.
6. Do not enable termination or transmit frames unless intentionally testing.

## Prototype warning

R6 is the current manufacturing/procurement candidate, but it is still first-run hardware. Order a small PCB batch first, bench-test carefully, and do not connect to a car until all power and wiring checks pass.
