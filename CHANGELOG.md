# Changelog

## 2026-06-30 — R10 status correction: NOT FOR FAB

- Reclassified R10 as an inspection/review revision only after external review.
- Confirmed R10 architecture is correct for true dual CAN FD, but not orderable.
- Added `R10_EXTERNAL_REVIEW_FINDINGS_20260630.md` with blockers for R10A/R11.
- Updated README/status files to warn not to send the R10 JLCPCB Gerber ZIP to fabrication.


## R10 true dual CAN FD active release - 2026-06-30

### Status

R10 is now the active cleaned hardware revision for the true dual CAN FD + LIN/K interface.

### Added

- Added cleaned active revision folder: `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/`.
- Added canonical R10 KiCad source using MCP2518FD controllers and MCP2562FD transceivers.
- Added regenerated JLCPCB/root-upload Gerber ZIP: `R10_TRUE_DUAL_CANFD_JLCPCB_GERBERS.zip`.
- Added full R10 source/handoff ZIP: `R10_TRUE_DUAL_CANFD_FULL_PACKAGE.zip`.
- Added cleanup/reorganization manifests under `99_MANIFESTS/`.
- Added `README_START_HERE.txt` as the top-level project navigation file.

### Verification

R10 was verified from the cleaned active revision folder with KiCad CLI 10.0.3.

- DRC violations: 0
- Unconnected pads/items: 0
- Footprint errors: 0
- Gerber/drill export: passed

### Changed

- Reorganized the repository around explicit revision folders.
- Archived R9 under `revisions/01_R9_CLASSIC_CAN_ARCHIVE/`.
- Updated root README and current status to point to R10 as the active design.

### Removed from current branch layout

- Removed root-level test/draft/intermediate R10 KiCad files.
- Removed failed optimization artifacts.
- Removed FreeRouting scratch directories.
- Removed intermediate R10 DRC reports superseded by the cleaned-folder DRC recheck.
- Removed obsolete root `hardware/`, `docs/`, and `fabrication/` layout after valid contents were moved into revision folders.

## R10 true dual CAN FD target - 2026-06-29

### Status

The project requirement changed to **true dual CAN FD**. R9 is no longer the final target board; it is now bench-only/classic-CAN prototype material.

### Added

- Added R10 redesign planning documents.
- Added R10 MCP2518FD controller architecture notes.
- Updated R9 BOM/netlist docs so they are PCB-derived and no longer describe stale TJA1051/TJA1020/DB9/USB-C content as current hardware.

### Required for R10

- Add MCP2518FD CAN FD controller x2.
- Keep MCP2562FD transceiver x2.
- Route Teensy SPI + CS/INT/RESET to the controllers.
- Create authoritative schematic and updated BOM before any R10 fab-ready claim.

## Repository cleanup - 2026-06-22

### Changed

- Reorganized the public repository around the then-current R9 FAB_READY release.
- Moved authoritative KiCad source and local footprints to `hardware/kicad/`.
- Moved R9 Gerbers, reports, and release package to `fabrication/r9/`.
- Moved public user-facing hardware docs to `docs/`.

### Removed from current branch

- Removed intermediate R5/R6/R7 KiCad variants, Gerbers, preview SVGs, BOMs, and reports from the public tree.
- Removed all tracked generation scripts from the public repository.
- Removed firmware/code example file from the public repository to keep code/scripts private.

## R9 FAB_READY - 2026-06-22

### Status

R9 was the manufacturing prototype candidate for the Teensy 4.1 dual classic CAN + LIN/K automotive interface using CAN-FD-capable transceivers. After the 2026-06-29 true-FD decision, R9 is no longer the final target board.

### Added

- Added explicit R9 final-candidate KiCad PCB/project files.
- Added clean FAB_READY manufacturing ZIP.
- Added R9 Gerber/drill outputs.
- Added R9 verification reports.
- Added project-local footprint library support.

### Verification

R9 was verified from the cleaned project copy with KiCad CLI 10.0.3.

- DRC violations: 0
- Unconnected pads/items: 0
- Footprint errors: 0
- Gerber/drill export: passed

### Notes

- The legacy schematic is not authoritative for R9. Manufacturing confidence is based on the KiCad PCB source, project-local footprints, KiCad CLI DRC, and KiCad-generated Gerber/drill files.
- R9 remains first-run prototype/reference hardware: order a small batch only if intentionally testing the older classic-CAN architecture, bench-test power rails first, start with passive/read-only firmware, and verify the OBD2 pigtail pinout with a multimeter.

## Earlier intermediate revisions

R5, R6, and R7 were development/intermediate variants leading to R9. They are no longer tracked in the current public branch layout.
