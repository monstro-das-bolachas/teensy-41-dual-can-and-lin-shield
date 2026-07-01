# R11 status

Status: PROTOTYPE_MANUFACTURING_CANDIDATE.

This revision is suitable for ordering a small bare-PCB prototype batch for bench bring-up. It is not approved for direct vehicle testing yet.

Active board:
`kicad/teensy-41-true-dual-canfd-lin-r11_JARVIS_ROUTED_CLEAN_V2_GND_STITCH.kicad_pcb`

Manufacturing upload ZIP:
`package/JLCPCB_PCBWAY_UPLOAD_R11_MINIMAL_GERBERS_ONLY_20260630.zip`

Full release archive:
`package/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630_FULL_RELEASE.zip`

Verification:
- KiCad CLI DRC: 0 DRC violations.
- Known residual: 1 GND zone-to-zone unconnected report at 1.0000 mm / 1.0000 mm.
- GND continuity: visually confirmed in KiCad by user after zone refill/highlight.
- Gerber/drill export: completed by KiCad CLI.

Do not use on a vehicle until:
1. Bare PCB continuity is checked.
2. Power rails are checked for shorts.
3. Board is powered from current-limited bench supply.
4. OBD/pigtail pin mapping is verified with a multimeter.
5. DIP switch default-safe positions are documented and confirmed.
6. CAN/LIN/K-line behavior is tested on bench hardware first.
