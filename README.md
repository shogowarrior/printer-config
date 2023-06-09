# printer-config
All configs related to printer

## New printer setup

All printers are klipper based. Klipper can be setup by either
* Docker containers
* SBCs like RPI, CB1 etc.

Assuming klipper is setup, let's go through setting up:
* passwordless ssh for SBCs
* setup passwordless git in for each printer `printer_data/config`.
* setup autocommit
* Setup git submodule to link all printer configs at [config](config/printers)

