# R6 EU Procurement BOM

Status: procurement BOM for the corrected R6 manufacturing candidate.

Use this with the R6 board files, not the older R5 files.

Primary fabrication ZIP:

- `r6_complete_power_fabrication_minimal_gerbers.zip`

Procurement CSV:

- `BOM_R6_PROCUREMENT_EU.csv`

## Why R6 replaced R5

During BOM audit I found that R5 was DRC-clean but did not include the required external LM2596 buck-regulator components. R6 corrects this by adding:

- L1 buck inductor
- D2 Schottky catch diode
- C1 input electrolytic capacitor
- C3 output electrolytic capacitor
- C2/C4 ceramic input/output capacitors
- C5/C6/C7 local decoupling capacitors for CAN/LIN ICs
- R1 10k pull-up for the TLIN1029 open-drain LIN RXD output

R6 also changes the selected communication ICs to parts that are better aligned with Teensy 4.1 3.3 V logic:

- U2/U3: Microchip MCP2562FD-E/SN CAN transceivers with VIO on pin 5 connected to Teensy +3.3 V.
- U4: TI TLIN1029DRQ1 LIN transceiver, whose RXD is open-drain and pulled up to +3.3 V by R1.

## Suppliers

The BOM uses exact manufacturer part numbers. Suitable Europe-capable suppliers include:

- Mouser Europe
- DigiKey Europe
- Farnell / element14
- RS Components Europe
- TI store / MicrochipDirect where appropriate
- Pimoroni or other European PJRC/SparkFun distributors for Teensy 4.1

For best results, paste the exact MPN from the CSV into the supplier search box. Supplier stock numbers change more often than manufacturer part numbers.

## Critical no-substitution rules

Do not blindly substitute these parts:

- U2/U3 CAN transceivers: must have VIO/3.3 V I/O support on pin 5. Do not use MCP2551, TJA1050, or plain 5 V-only CAN transceivers.
- U4 LIN transceiver: must match TLIN1029DRQ1 SOIC-8 pinout if using this PCB.
- U5 regulator: must be fixed 5 V LM2596S-5.0 in TO-263-5/D2PAK-style package, not the adjustable version, unless the PCB is redesigned.
- SW1/SW2 DIP switches: must be 8-position SPST through-hole DIP, 2.54 mm pitch, 7.62 mm row spacing.
- C1/C3 electrolytics: observe polarity and keep diameter/lead pitch compatible with the footprint.

## Assembly order recommendation

1. Solder power/protection parts first: F1, D1, U5, L1, D2, C1, C2, C3, C4.
2. Bench-test the board from a current-limited 12 V supply.
3. Verify +5 V at TP2 and +3.3 V from the Teensy socket only after the Teensy is installed/powered appropriately.
4. Solder R1, C5/C6/C7, U2/U3/U4.
5. Solder SW1/SW2 and optional J2.
6. Install/socket Teensy 4.1 last.
7. Verify OBD pigtail pin numbering with a multimeter before connecting to a vehicle.

## Vehicle-use warning

This is still a first real hardware prototype. Even with a DRC-clean PCB and procurement BOM, test on the bench before connecting to a vehicle. Start with read-only/silent CAN firmware and no CAN transmission.
