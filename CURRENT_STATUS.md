# Current project status

Last checked/updated: 2026-06-30

## Executive summary

The active hardware revision is now **R11 true dual CAN FD + LIN/K prototype manufacturing candidate**.

R11 may be ordered as a small bare-PCB prototype batch for bench bring-up. It is **not approved for direct vehicle testing** until assembled boards pass continuity, power, pin-map, and fused OBD bench checks.

## Active R11 files

Active working revision folder:

- `revisions/00_WORK_R11_TRUE_DUAL_CANFD/`

Clean release package folder:

- `revisions/00_WORK_R11_TRUE_DUAL_CANFD/release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/`

Active KiCad source:

- `revisions/00_WORK_R11_TRUE_DUAL_CANFD/kicad/teensy-41-true-dual-canfd-lin-r11_JARVIS_ROUTED_CLEAN_V2_GND_STITCH.kicad_pcb`
- `revisions/00_WORK_R11_TRUE_DUAL_CANFD/kicad/teensy-41-true-dual-canfd-lin-r11_JARVIS_ROUTED_CLEAN_V2_GND_STITCH.kicad_pro`

JLCPCB / PCBWay upload ZIP:

- `revisions/00_WORK_R11_TRUE_DUAL_CANFD/release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/package/JLCPCB_PCBWAY_UPLOAD_R11_MINIMAL_GERBERS_ONLY_20260630.zip`

Full release ZIP:

- `revisions/00_WORK_R11_TRUE_DUAL_CANFD/release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/package/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630_FULL_RELEASE.zip`

## R11 verification

KiCad CLI DRC was run against the active board and the clean release-copy board.

Reports:

- `revisions/00_WORK_R11_TRUE_DUAL_CANFD/release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/reports/R11_PROTOTYPE_CANDIDATE_DRC.rpt`
- `revisions/00_WORK_R11_TRUE_DUAL_CANFD/release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/reports/R11_PROTOTYPE_CANDIDATE_CLEAN_RELEASE_COPY_DRC.rpt`

Result:

- DRC violations: 0
- Known residual: 1 GND F.Cu/B.Cu zone-to-zone unconnected report at 1.0000 mm / 1.0000 mm
- Footprint errors: 0
- Gerber/drill export: successful
- GND continuity: visually confirmed in KiCad after zone refill/highlight

The residual GND item is treated as a reviewed KiCad zone-report artifact for prototype PCB ordering, not as approval for vehicle use.

## R11 prototype ordering guidance

Order only a small bare-PCB batch first:

- 2 layers
- FR-4
- 1.6 mm
- 1 oz copper
- 5 pieces or smallest economical batch
- electrical test enabled
- no assembly for first order

Before vehicle testing:

1. Inspect bare PCBs.
2. Check GND continuity and rail shorts with a multimeter.
3. Assemble power section first.
4. Power from a current-limited bench supply.
5. Verify OBD/pigtail pin mapping with a multimeter.
6. Verify DIP switch safe/default positions.
7. Test CAN/LIN/K behavior on bench hardware before a fused OBD vehicle connection.

## R10/R9 status

R10 remains archived as `NOT FOR FAB` after external review. R9 remains historical/reference material only and is not true dual CAN FD.
