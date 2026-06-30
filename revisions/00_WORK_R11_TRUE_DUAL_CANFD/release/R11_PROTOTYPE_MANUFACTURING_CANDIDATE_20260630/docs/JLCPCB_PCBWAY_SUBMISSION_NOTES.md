# R11 prototype PCB submission notes

Status: PROTOTYPE_MANUFACTURING_CANDIDATE, not vehicle-ready.

Use this upload ZIP for JLCPCB or PCBWay:

`package/JLCPCB_PCBWAY_UPLOAD_R11_MINIMAL_GERBERS_ONLY_20260630.zip`

Verification basis:
- KiCad CLI: see `reports/kicad_version.txt`
- Source board: `kicad/teensy-41-true-dual-canfd-lin-r11_JARVIS_ROUTED_CLEAN_V2_GND_STITCH.kicad_pcb`
- DRC report: `reports/R11_PROTOTYPE_CANDIDATE_DRC.rpt`
- DRC result: 0 DRC violations; 1 unconnected item remains, the known GND F.Cu/B.Cu zone self-report at 1.0000 mm / 1.0000 mm.
- User visually confirmed GND continuity in KiCad after refill/highlight.
- Gerbers/drill exported by KiCad CLI.

Recommended first order:
- Quantity: 5 PCBs, or smallest cheap prototype batch
- Layers: 2
- Material: FR-4
- Thickness: 1.6 mm
- Copper: 1 oz
- Finish: Lead-free HASL for cost, ENIG if price difference is acceptable
- Electrical test: yes / flying probe
- Assembly: no, bare PCBs only for first order
- Panelization: no

Portal preview checks before paying:
1. Board outline appears correct.
2. Top and bottom copper are visible.
3. Drill holes/vias are present.
4. No obvious copper shorts between OBD/pigtail pads.
5. Silkscreen labels do not cover pads critically.
6. If the portal warns about the known GND zone artifact, do not treat it as vehicle approval; it is only acceptable for prototype PCB manufacture because continuity was visually confirmed.

Bring-up warning:
- Do not connect the first assembled board directly to a vehicle.
- First test bare PCB continuity with a multimeter.
- Then assemble/power in stages with bench supply current limiting.
- Vehicle testing requires fused OBD pigtail and pin-map verification.
