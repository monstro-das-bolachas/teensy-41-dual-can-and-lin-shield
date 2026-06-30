R10 TRUE DUAL CAN FD / LIN-K - NOT FOR FAB

Active board:
  kicad/teensy-41-true-dual-canfd-lin-r10.kicad_pcb

Architecture:
  Teensy 4.1 SPI -> two MCP2518FD CAN FD controllers -> MCP2562FD transceivers
  LIN/K interface and DIP/pigtail routing options retained from project requirements.

Current order status:
  NOT FOR FAB.
  DO NOT ORDER R10.
  DO NOT SEND package/R10_TRUE_DUAL_CANFD_JLCPCB_GERBERS.zip TO JLCPCB.

Why:
  R10 has the correct high-level true dual CAN FD architecture, but external review found remaining blockers:
    - no real .kicad_sch schematic / no meaningful ERC;
    - TLIN1029 VSUP decoupling wrong;
    - missing LIN commander pull-up option;
    - missing LIN_EN safe-default pull-down;
    - missing CAN STBY/XSTBY safe-default pull-ups;
    - missing MCP2518FD nCS pull-ups;
    - LM2596 TO-263 tab not explicitly tied to GND;
    - buck/power routing too weak;
    - no GND pours;
    - decoupling and crystal placement not local enough;
    - missing CAN/LIN/K ESD protection;
    - USB/VIN isolation unresolved;
    - DIP-switch routing can be user-error-prone.

Verification status after cleanup:
  KiCad CLI DRC recheck from this cleaned folder is stored in:
    reports/R10_TRUE_DUAL_CANFD_DRC_RECHECK.rpt

DRC result:
  0 DRC violations
  0 unconnected pads
  0 footprint errors

Important interpretation:
  The DRC result proves PCB geometry/routing cleanliness only. It does not make R10 safe or fabrication-ready.

Primary blocker document:
  docs/R10_EXTERNAL_REVIEW_FINDINGS_20260630.md

Next target:
  R10A/R11 with real schematic/ERC, corrected power/protection/default states, improved layout, and regenerated manufacturing package.
