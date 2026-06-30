# Current project status

Last checked/updated: 2026-06-30

## Executive summary

The active hardware revision is **R10 true dual CAN FD + LIN/K**, but R10 is **NOT FOR FAB**.

Do not order R10. Do not send the R10 JLCPCB Gerber ZIP to a board house.

R10 includes the required external CAN FD controller architecture:

```text
Teensy 4.1 SPI bus
  -> MCP2518FD controller A -> MCP2562FD transceiver A
  -> MCP2518FD controller B -> MCP2562FD transceiver B
TLIN1029 LIN/K interface retained
```

That fixes the previous R8/R9 architecture problem. The remaining blockers are schematic discipline, ERC, LIN/CAN safe defaults, buck/power layout, decoupling, crystal placement, ESD protection, USB/VIN isolation, and safer selector UX.

## Active R10 files

Active revision folder:

- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/`

KiCad PCB-only inspection source:

- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/kicad/teensy-41-true-dual-canfd-lin-r10.kicad_pcb`
- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/kicad/teensy-41-true-dual-canfd-lin-r10.kicad_pro`

There is currently no authoritative `.kicad_sch`; therefore there is no meaningful ERC and no schematic-driven BOM/netlist authority.

## R10 verification

KiCad CLI DRC was run from the cleaned active revision folder.

Report:

- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/reports/R10_TRUE_DUAL_CANFD_DRC_RECHECK.rpt`

Result:

- DRC violations: 0
- Unconnected pads/items: 0
- Footprint errors: 0

This is a geometry/routing check only. It does not override the external review blockers.

## R10 blockers

See:

- `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/docs/R10_EXTERNAL_REVIEW_FINDINGS_20260630.md`

Minimum R10A/R11 work:

1. Create real `.kicad_sch` and run ERC.
2. Fix TLIN1029 VSUP decoupling.
3. Add LIN commander pull-up option.
4. Add LIN_EN pull-down.
5. Add CAN STBY/XSTBY pull-ups.
6. Add MCP2518FD nCS pull-ups.
7. Connect LM2596 thermal tab to GND.
8. Redo buck/power routing and add GND pours.
9. Move decoupling capacitors local to ICs.
10. Move MCP2518FD crystals/load caps close to controllers and finalize load capacitance.
11. Add CAN/LIN/K ESD protection.
12. Resolve USB/VIN isolation.
13. Improve DIP-switch safety/truth-table documentation.
14. Regenerate BOM, ERC, DRC, Gerbers, drill files, and final package.

## R9 status

R9 is archived here:

- `revisions/01_R9_CLASSIC_CAN_ARCHIVE/`

R9 remains historical/reference material only and should not be presented as true dual CAN FD.
