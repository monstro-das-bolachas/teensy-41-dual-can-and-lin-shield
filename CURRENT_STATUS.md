# Current project status

Last checked/updated: 2026-06-21

## Executive summary

The active design is now R6: a Teensy 4.1 dual-CAN + LIN/K automotive interface using OBD2 pigtail/cable solder pads and DIP-switch configurable routing.

R6 supersedes R5.

Reason: R5 was DRC-clean and manufacturable as a PCB, but the procurement audit found it lacked the required external LM2596 buck-regulator support parts. R6 adds those parts and updates the transceiver selections for Teensy 4.1 3.3 V logic compatibility.

Authoritative routed board:

- `teensy-41-can-lin-r6-complete-power-routed.kicad_pcb`

Preferred fabrication ZIP:

- `r6_complete_power_fabrication_minimal_gerbers.zip`

Main R6 documentation:

- `R6_PROCUREMENT_BOM_EU.md`
- `BOM_R6_PROCUREMENT_EU.csv`

## KiCad verification

Verified with:

- KiCad CLI version: 10.0.3
- pcbnew Python build: 10.0.3+dfsg-1
- FreeRouting: 2.2.4 local app

Latest authoritative DRC report:

- `reports/teensy-41-can-lin-r6-complete-power-routed-drc.rpt`

Result:

- DRC violations: 0
- Unconnected pads: 0
- Footprint errors: 0

Generated fabrication files:

- `gerbers/r6_complete_power_fabrication_minimal/`
- `r6_complete_power_fabrication_minimal_gerbers.zip`

Generated preview files:

- `previews/r6_complete_power_svg/`

## R6 feature summary

### Mechanical form

R6 uses an OBD2 cable/pigtail instead of a board-mounted OBD connector.

The user should:

1. Buy or make an OBD2 male pigtail cable.
2. Verify every OBD pin/wire with a multimeter.
3. Solder wires to the labeled J1 pads.
4. Use the strain-relief holes with a zip tie.

### Teensy 4.1

Key assignments:

- CAN A / CAN1: Teensy pins 22 TX and 23 RX
- CAN B / CAN2: Teensy pins 1 TX and 0 RX
- LIN/K UART: Teensy pins 8 TX and 7 RX
- CAN standby/control: pins 5 and 4
- LIN enable/control: pin 6
- Teensy +3.3 V is used for CAN VIO and LIN RX pull-up logic compatibility

### Communication ICs

- CAN A/B: MCP2562FD-E/SN, SOIC-8, VIO pin connected to +3.3 V.
- LIN/K: TLIN1029DRQ1, SOIC-8, RXD open-drain pulled up to +3.3 V through R1.

### Power section

R6 includes the complete LM2596S-5.0 fixed 5 V buck-regulator support circuit:

- F1: 500 mA resettable fuse
- D1: SMBJ24CA input TVS
- U5: LM2596S-5.0 fixed 5 V buck regulator
- L1: 33 uH buck inductor
- D2: Schottky catch diode
- C1/C3: input/output electrolytic bulk capacitors
- C2/C4: input/output ceramic decoupling capacitors
- C5/C6/C7: CAN/LIN IC local decoupling capacitors

### DIP switches

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

PCB fabrication status: ready to upload as a first-run fabrication candidate.

Use:

- `r6_complete_power_fabrication_minimal_gerbers.zip`

Recommended order settings:

- 2-layer FR4
- 1.6 mm thickness
- 1 oz copper
- HASL lead-free or ENIG
- Small prototype quantity first, e.g. 5 boards

Remaining practical checks before vehicle use:

1. Confirm exact OBD2 pigtail/cable pinout with a multimeter.
2. Assemble and test the power section on a current-limited bench supply.
3. Verify +5 V before installing the Teensy.
4. Confirm DIP switch settings.
5. Start with read-only/silent CAN firmware.

## Previous revisions

R5:

- `teensy-41-can-lin-r5-pigtail-dipswitch-routed.kicad_pcb`
- Introduced the safer OBD2 pigtail/DIP-switch mechanical concept.
- Superseded by R6 because it lacked required LM2596 support components and procurement-ready IC choices.

R4:

- `teensy-41-can-lin-r4-universal-routing-matrix.kicad_pcb`
- Implemented CAN/LIN routing matrix, but still used a board-mounted OBD connector approach.

R6 supersedes R4/R5 for ordering and procurement.
