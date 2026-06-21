# Current project status

Last checked/updated: 2026-06-21

## Executive summary

The active design is now R5: a Teensy 4.1 CAN/LIN automotive interface using an OBD2 pigtail/cable solder-pad entry and DIP-switch configurable routing.

R5 is the first PCB fabrication candidate in this project because it removes the previous unknown board-mounted OBD connector footprint risk.

Authoritative routed board:

- `teensy-41-can-lin-r5-pigtail-dipswitch-routed.kicad_pcb`

Preferred fabrication ZIP:

- `r5_pigtail_dipswitch_fabrication_minimal_gerbers.zip`

Full KiCad layer export ZIP, kept for reference:

- `r5_pigtail_dipswitch_fabrication_gerbers.zip`

Main R5 documentation:

- `R5_PIGTAIL_DIPSWITCH_MANUFACTURING.md`
- `BOM_R5_PIGTAIL_DIPSWITCH.csv`

## KiCad verification

Verified with:

- KiCad CLI version: 10.0.3
- pcbnew Python build: 10.0.3+dfsg-1
- FreeRouting: 2.2.4 local app

Latest authoritative DRC report:

- `reports/teensy-41-can-lin-r5-pigtail-dipswitch-routed-drc.rpt`

Result:

- DRC violations: 0
- Unconnected pads: 0
- Footprint errors: 0

Generated fabrication files:

- `gerbers/r5_pigtail_dipswitch_fabrication/`
- `r5_pigtail_dipswitch_fabrication_gerbers.zip`

Generated preview files:

- `previews/r5_pigtail_dipswitch_svg/`

## R5 feature summary

### Mechanical form

R5 uses an OBD2 cable/pigtail instead of a board-mounted OBD connector.

This avoids the previous blocker where no reliable datasheet/mechanical drawing existed for the board-mounted OBD connector.

The user should:

1. Buy or make an OBD2 male pigtail cable.
2. Verify every OBD pin/wire with a multimeter.
3. Solder wires to the labeled J1 pads.
4. Use the strain-relief holes with a zip tie.

### Teensy 4.1

The R5 Teensy footprint/pin assignment was audited against PJRC Teensy 4.1 information.

Key assignments:

- CAN A / CAN1: Teensy pins 22 TX and 23 RX
- CAN B / CAN2: Teensy pins 1 TX and 0 RX
- LIN/K UART: Teensy pins 8 TX and 7 RX
- CAN standby/control: pins 5 and 4
- LIN enable/control: pin 6

### DIP switches

R5 uses two 8-position DIP switches.

SW1 configures CAN routing:

- SW1-1 + SW1-2: CAN A normal, OBD6/14
- SW1-3 + SW1-4: CAN A crossed, OBD6/14
- SW1-5 + SW1-6: CAN B normal, OBD3/11
- SW1-7 + SW1-8: CAN B crossed, OBD3/11

SW2 configures LIN/K source selection:

- SW2-1: OBD7
- SW2-2: OBD15
- SW2-3: OBD1
- SW2-4: OBD8
- SW2-5: OBD9
- SW2-6: OBD12
- SW2-7: OBD13
- SW2-8: AUX_LIN_K_IO

Rule: enable exactly one LIN/K source at a time.

## Manufacturing status

PCB fabrication status: ready to upload as a fabrication candidate.

Use:

- `r5_pigtail_dipswitch_fabrication_gerbers.zip`

Remaining practical checks before ordering/assembling:

1. Confirm desired PCB fab settings: 2-layer FR4, 1.6 mm, 1 oz copper.
2. Confirm the exact DIP switch, transceiver, regulator, TVS, fuse, and header parts to buy.
3. Confirm the OBD2 pigtail cable pinout with a multimeter before soldering.
4. Perform bench power testing before installing Teensy or connecting to a car.

## Previous revisions

R4:

- `teensy-41-can-lin-r4-universal-routing-matrix.kicad_pcb`
- Implemented CAN/LIN routing matrix, but still used a board-mounted OBD connector approach.

R5 supersedes R4 for fabrication because R5 avoids the uncertain OBD connector footprint and uses easier DIP switch configuration.
