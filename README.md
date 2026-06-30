# Teensy 4.1 true dual CAN FD + LIN/K interface

This repository contains hardware work for a Teensy 4.1 based automotive diagnostics and reverse-engineering interface.

## Current status — R10 is NOT FOR FAB

The active revision is **R10 true dual CAN FD + LIN/K**, but it is an **inspection/review revision only**.

**Do not order R10 boards. Do not upload the R10 Gerber ZIP to JLCPCB.**

R10 corrected the major architecture problem by adding true external CAN FD controllers:

```text
Teensy 4.1 SPI bus
  -> MCP2518FD CAN FD controller A -> MCP2562FD CAN transceiver A
  -> MCP2518FD CAN FD controller B -> MCP2562FD CAN transceiver B
LIN/K interface retained
OBD pigtail pads and DIP-switch routing retained
```

However, an external review found that R10 is not fabrication-ready because it lacks an authoritative `.kicad_sch` schematic/ERC and still has power, protection, default-state, layout, decoupling, USB/VIN isolation, and documentation blockers.

Authoritative active folder:

- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/`

Active KiCad PCB-only inspection board:

- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/kicad/teensy-41-true-dual-canfd-lin-r10.kicad_pcb`
- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/kicad/teensy-41-true-dual-canfd-lin-r10.kicad_pro`

Important blocker document:

- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/docs/R10_EXTERNAL_REVIEW_FINDINGS_20260630.md`

## Verification summary

KiCad CLI DRC from the cleaned active revision folder reported:

- DRC violations: 0
- Unconnected pads/items: 0
- Footprint errors: 0

This DRC result proves that the existing PCB geometry is internally routable. It does **not** prove the design is safe or fabrication-ready. R10 has no real schematic, no meaningful ERC, and unresolved automotive/power-layout blockers.

## Package warning

The existing R10 ZIPs are retained only for inspection/archive unless superseded by R10A/R11.

Do not use `R10_TRUE_DUAL_CANFD_JLCPCB_GERBERS.zip` for ordering.

## Repository layout

- `README_START_HERE.txt` — short navigation guide.
- `CURRENT_STATUS.md` — current revision status and safety notes.
- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/` — active R10 inspection/review material.
- `revisions/01_R9_CLASSIC_CAN_ARCHIVE/` — previous R9 classic-CAN archive retained for historical/reference purposes.
- `99_MANIFESTS/` — cleanup and reorganization manifests.
- `CHANGELOG.md` — revision notes.

## R9 archive note

R9 is retained only as a historical/classic-CAN archive. R9 used MCP2562FD CAN-FD-capable physical transceivers, but did not include external CAN FD controllers. Therefore R9 is not true dual CAN FD.

## Next target

The next orderable target should be **R10A/R11**, with a real schematic/ERC, corrected LIN/CAN default states, corrected buck/power layout, GND pours, local decoupling, ESD protection, USB/VIN isolation, and regenerated manufacturing outputs.
