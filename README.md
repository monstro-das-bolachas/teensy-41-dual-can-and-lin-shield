# Teensy 4.1 CAN/LIN Interface for automotive diagnostics

This project contains a Teensy 4.1 based dual-CAN + LIN/K automotive interface for diagnostic/reverse-engineering use.  
The aim is to be used with Savvy.  
Firmware yet ot be written.  

## Current active revision

Use R7.

R7 supersedes R6. R6 added the missing LM2596 buck-regulator support parts and 3.3 V-compatible CAN/LIN transceiver selections, but visual review found that its generated Teensy 4.1 footprint was one pad short on the upper long row. R7 corrects the Teensy footprint while keeping the R6 electrical fixes.

R5 was the first revision publicly shared; R7 is the recommended ordering/procurement candidate.

Start here:

- `CURRENT_STATUS.md` — current truth/status
- `R7_PROCUREMENT_BOM_EU.md` — R7 procurement and ordering notes
- `BOM_R7_PROCUREMENT_EU.csv` — EU-capable procurement BOM with exact manufacturer part numbers
- `R5_PIGTAIL_DIPSWITCH_MANUFACTURING.md` — historical R5 pigtail/DIP-switch notes, superseded by R7

Authoritative R7 PCB:

- `teensy-41-can-lin-r7-teensy-footprint-corrected-routed.kicad_pcb`

Preferred fabrication package:

- `r7_teensy_footprint_corrected_fabrication_minimal_gerbers.zip`

DRC report:

- `reports/teensy-41-can-lin-r7-teensy-footprint-corrected-routed-drc.rpt`

Preview SVGs:

- `previews/r7_teensy_footprint_corrected_svg/`

Gerber/drill directory:

- `gerbers/r7_teensy_footprint_corrected_fabrication_minimal/`

## Verification summary

R7 was generated with KiCad/pcbnew automation, routed with local FreeRouting, and verified with KiCad CLI.

Result:

- KiCad CLI: 10.0.3
- DRC violations: 0
- Unconnected pads: 0
- Footprint errors: 0
- Gerber/drill export: passed
- Teensy U1 long-row pad counts: 23 upper / 24 lower, matching the intended PJRC Teensy 4.1 side-row asymmetry

## R7 key electrical/mechanical decisions

- U1 Teensy footprint: corrected upper row to GND, VIN, 23..13, GND, 41..33; lower row remains GND, 0..12, 3.3V, 24..32.
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

## Prototype warning / disclaimer

R7 is the current manufacturing/procurement candidate, but it is still first-run hardware. Order a small PCB batch first, bench-test carefully, and do not connect to a car until all power and wiring checks pass.

The project was AI-assisted and should be treated as a prototype. Independent review and constructive feedback are welcome.
