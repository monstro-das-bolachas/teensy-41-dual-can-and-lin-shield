R11 TRUE DUAL CAN FD / LIN-K - PROTOTYPE MANUFACTURING CANDIDATE

Status: PROTOTYPE_MANUFACTURING_CANDIDATE for small bare-PCB bench bring-up batch.
Vehicle status: NOT VEHICLE-READY.

Active R11 board:
  kicad/teensy-41-true-dual-canfd-lin-r11_JARVIS_ROUTED_CLEAN_V2_GND_STITCH.kicad_pcb

Clean release package:
  release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/

JLCPCB / PCBWay upload ZIP:
  release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/package/JLCPCB_PCBWAY_UPLOAD_R11_MINIMAL_GERBERS_ONLY_20260630.zip

Verification:
  - KiCad CLI: 10.0.3
  - DRC violations: 0
  - Known residual: 1 GND F.Cu/B.Cu zone-to-zone unconnected report at 1.0000 mm / 1.0000 mm
  - GND continuity: visually confirmed in KiCad after zone refill/highlight
  - Footprint errors: 0
  - Gerber/drill export: PASS

Ordering guidance:
  OK to order 2-5 bare prototype PCBs for bench validation only.
  Do not order assembly yet.
  Do not connect to a vehicle until continuity, power, OBD pin mapping, DIP switch defaults, and fused bench/OBD checks pass.

Project cleanup:
  Non-active KiCad routing experiments were moved locally into work/archived_non_active_kicad_files_20260630/ and are intentionally not published.
  The kicad/ folder now keeps the active R11 board/project plus required local libraries.
