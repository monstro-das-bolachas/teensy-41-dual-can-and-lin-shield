# R11 implementation status

Status: PROTOTYPE_MANUFACTURING_CANDIDATE for small bare-PCB bench bring-up batch.
Vehicle status: NOT VEHICLE-READY.

## Active source

- `../kicad/teensy-41-true-dual-canfd-lin-r11_JARVIS_ROUTED_CLEAN_V2_GND_STITCH.kicad_pcb`
- `../kicad/teensy-41-true-dual-canfd-lin-r11_JARVIS_ROUTED_CLEAN_V2_GND_STITCH.kicad_pro`

## Release package

- `../release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/`

Use this manufacturer upload ZIP:

- `../release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/package/JLCPCB_PCBWAY_UPLOAD_R11_MINIMAL_GERBERS_ONLY_20260630.zip`

## KiCad verification

Reports:

- `../release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/reports/R11_PROTOTYPE_CANDIDATE_DRC.rpt`
- `../release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/reports/R11_PROTOTYPE_CANDIDATE_CLEAN_RELEASE_COPY_DRC.rpt`

Result:

- DRC violations: 0
- Footprint errors: 0
- Known residual: one GND zone-to-zone unconnected report at 1.0000 mm / 1.0000 mm
- GND continuity: visually confirmed in KiCad after zone refill/highlight
- Gerbers/drill: exported successfully by KiCad CLI

## Safety status

Acceptable next step:

- Order a small bare-PCB prototype batch for bench bring-up.

Not acceptable yet:

- Do not order assembly.
- Do not connect to a vehicle.
- Do not call this final/fab-ready for general use.

Before vehicle testing, verify bare board continuity, power rails, OBD/pigtail pin mapping, DIP switch defaults, CAN/LIN/K behavior on bench hardware, and fused OBD connection procedure.
