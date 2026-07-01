# OBDee-Wan CANobi

> Open-hardware automotive bus interface for CAN FD, classic CAN, LIN, and K-line exploration.

OBDee-Wan CANobi is a Teensy 4.1 based vehicle-network tool for hackers, makers, reverse engineers, EV converters, and curious learners who want hardware they can inspect and understand.

It is designed as a practical bridge between a laptop and a vehicle or bench module: powerful enough for real CAN FD/LIN/K-line experiments, but documented as a teaching project rather than a black box.

![Status](https://img.shields.io/badge/status-R11%20prototype%20candidate-orange)
![Hardware](https://img.shields.io/badge/hardware-CERN--OHL--P--2.0-blue)
![Software](https://img.shields.io/badge/software-MIT-green)
![Docs](https://img.shields.io/badge/docs-CC--BY--4.0-lightgrey)

## At a glance

| Area | Current R11 target |
| --- | --- |
| Host | Teensy 4.1 |
| CAN FD | 2 external CAN FD controller paths |
| Transceivers | Dual CAN FD transceivers |
| Other buses | LIN / K-line support path |
| Vehicle connection | OBD pigtail-friendly wiring, not a direct-plug dongle |
| Configuration | DIP-switch selectable routing options |
| CAD | KiCad hardware source and generated fabrication packages |
| Readiness | Bare-PCB prototype candidate for bench bring-up |

## What you can use it for

- CAN FD experimentation and learning
- Classic CAN diagnostics and reverse engineering
- LIN and K-line bench experiments
- EV conversion support tooling
- Custom diagnostic interface development
- Teaching automotive networks with inspectable hardware
- Bench testing ECUs, modules, sensors, and harness fragments

## Current status: R11 prototype manufacturing candidate

R11 may be ordered as a small bare-PCB prototype batch for bench bring-up.

It is not approved for direct vehicle testing yet.

### Active release package

`revisions/00_WORK_R11_TRUE_DUAL_CANFD/release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/`

### Manufacturer upload ZIP

`revisions/00_WORK_R11_TRUE_DUAL_CANFD/release/R11_PROTOTYPE_MANUFACTURING_CANDIDATE_20260630/package/JLCPCB_PCBWAY_UPLOAD_R11_MINIMAL_GERBERS_ONLY_20260630.zip`

SHA256:

`434dedf475bb3443f1ffa6384541426fcef9cf96a792c1744b9c1bb7ff68faa8`

### Verification summary

| Check | Result |
| --- | --- |
| KiCad CLI PCB DRC | 0 violations |
| Footprint errors | 0 |
| Known residual | 1 GND zone-to-zone report at 1.0000 mm / 1.0000 mm |
| Gerber/drill export | Successful |
| GND continuity | Visually confirmed in KiCad after refill/highlight |
| Vehicle-use approval | Not yet; bench validation required first |

The remaining GND item is a reviewed KiCad zone-report artifact for prototype PCB ordering. It is not a blanket safety approval for vehicle connection.

## Safety first

Vehicle electrical systems can damage tools, modules, or the car if connected incorrectly. Treat every first assembly as experimental hardware.

Before connecting to a vehicle:

1. Inspect the bare PCB.
2. Check for rail shorts with a multimeter.
3. Assemble and test the power section first.
4. Power up from a current-limited bench supply.
5. Verify OBD/pigtail pin mapping manually.
6. Confirm DIP-switch defaults and intended routing.
7. Test CAN/LIN/K behavior on bench modules first.
8. Use fusing and current limiting for any later vehicle test.

## Repository map

| Path | Purpose |
| --- | --- |
| `README_START_HERE.txt` | Short navigation and safety guide |
| `CURRENT_STATUS.md` | Current revision status, ordering notes, and verification summary |
| `revisions/00_WORK_R11_TRUE_DUAL_CANFD/` | Active R11 prototype candidate source and release package |
| `revisions/00_ACTIVE_R10_TRUE_DUAL_CANFD/` | Previous R10 archive, not for fabrication |
| `revisions/01_R9_CLASSIC_CAN_ARCHIVE/` | Historical R9 classic-CAN reference |
| `LICENSE` | Main hardware license: CERN-OHL-P-2.0 |
| `LICENSES/` | Full license texts and license split documentation |

## Recommended first order

For the first prototype batch, use conservative bare-board settings:

| Option | Recommendation |
| --- | --- |
| Quantity | 5 or smallest economical batch |
| Layers | 2 |
| Material | FR-4 |
| Thickness | 1.6 mm |
| Copper | 1 oz |
| Surface finish | Standard low-cost prototype finish is acceptable |
| Electrical test | Yes |
| Assembly | No; hand-assemble and validate first |

## Naming note

The project name is a small joke:

OBDee-Wan CANobi: an OBD/CAN interface that helps you feel disturbances in the bus.

## License

This project is open source and open hardware.

| Content | License |
| --- | --- |
| Hardware design files, KiCad sources, PCB/manufacturing files | CERN-OHL-P-2.0 |
| Firmware, scripts, and software | MIT |
| Documentation | CC-BY-4.0 |

You are free to study, modify, build, remix, and share this project. Attribution is required where applicable: please credit the original project and author when reusing or publishing derivative work.

See `LICENSES/README.md` for the full license split and SPDX identifiers.
