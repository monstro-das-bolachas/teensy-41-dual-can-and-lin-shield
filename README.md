# Teensy 4.1 CAN/LIN Interface for automotive diagnostics

This project contains a Teensy 4.1 based dual-CAN + LIN/K automotive interface for diagnostic/reverse-engineering use.

## Current active revision

This is the fifth revision but the first to be publicly shared.

Start here:

- `CURRENT_STATUS.md` — current truth/status
- `R5_PIGTAIL_DIPSWITCH_MANUFACTURING.md` — R5 manufacturing and configuration notes
- `BOM_R5_PIGTAIL_DIPSWITCH.csv` — practical parts/BOM reference

Authoritative R5 PCB:

- `teensy-41-can-lin-r5-pigtail-dipswitch-routed.kicad_pcb`

Preferred fabrication package:

- `r5_pigtail_dipswitch_fabrication_minimal_gerbers.zip`

Full KiCad layer export, kept for reference:

- `r5_pigtail_dipswitch_fabrication_gerbers.zip`

DRC report:

- `reports/teensy-41-can-lin-r5-pigtail-dipswitch-routed-drc.rpt`

Preview SVGs:

- `previews/r5_pigtail_dipswitch_svg/`

Gerber/drill directory:

- `gerbers/r5_pigtail_dipswitch_fabrication/`

## Verification summary

R5 was generated with KiCad/pcbnew automation, routed with local FreeRouting, and verified with KiCad CLI.

Result:

- KiCad CLI: 10.0.3
- DRC violations: 0
- Unconnected pads: 0
- Footprint errors: 0
- Gerber/drill export: passed

## Configuration summary

SW1 selects CAN routing:

- 1+2: CAN A normal, OBD6/14
- 3+4: CAN A crossed, OBD6/14
- 5+6: CAN B normal, OBD3/11
- 7+8: CAN B crossed, OBD3/11

SW2 selects LIN/K source:

- 1: OBD7
- 2: OBD15
- 3: OBD1
- 4: OBD8
- 5: OBD9
- 6: OBD12
- 7: OBD13
- 8: AUX_LIN_K_IO

Rule: enable exactly one LIN/K source at a time.

## Safety

Before connecting to a vehicle:

1. Verify OBD cable pinout with a multimeter.
2. Verify +5 V rail without Teensy installed.
3. Confirm DIP switch settings.
4. Start with passive/read-only firmware.
5. Do not enable termination or transmit frames unless intentionally testing.

## Disclaimer

I do not have experience in PCB design/manufacturing nor in complex electronics.
This entire project was designed by AI, with me steering it to the goals.
I am always learning and I welcome constructive feedback.
Treat this as a prototype and make some checks!
