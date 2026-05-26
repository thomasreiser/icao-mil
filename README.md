# icao-mil
Exhaustive list of military ICAO hex ranges

## Global military ICAO 24-bit hex ranges

The table below lists ICAO 24-bit aircraft address ranges reserved for, or commonly used by, military aircraft worldwide. There is no single official global registry of military allocations — this list is compiled from community-maintained sources (primarily the `MIL_RANGES` table in [readsb](https://github.com/wiedehopf/readsb), which is the de facto standard used by tar1090, ADSB Exchange, and most open-source ADS-B decoders).

Ranges are sorted ascending by hex start. The "Unit / Branch" column is left empty where the specific service is not publicly documented.

> This file is generated from [`data/military-ranges.yaml`](data/military-ranges.yaml). Do not edit by hand.

| Hex Range | Country | Unit / Branch |
|-----------|---------|---------------|
| `010070`–`01008F` | Egypt | Egyptian Armed Forces |
| `0A4000`–`0A4FFF` | Algeria | Algerian Air Force |
| `33FF00`–`33FFFF` | Italy | Aeronautica Militare / Marina Militare / Aviazione dell'Esercito |
| `350000`–`37FFFF` | Spain | Ejército del Aire / Armada / FAMET |
| `3AA000`–`3AFFFF` | France | Armée de l'Air et de l'Espace / Aéronavale / ALAT |
| `3B7000`–`3BFFFF` | France | Armée de l'Air et de l'Espace / Aéronavale / ALAT |
| `3EA000`–`3EBFFF` | Germany | Bundeswehr (Luftwaffe / Heer / Marine) |
| `3F4000`–`3F7FFF` | Germany | Bundeswehr (Luftwaffe / Heer / Marine) |
| `3F8000`–`3FBFFF` | Germany | Bundeswehr (Luftwaffe / Heer / Marine) |
| `400000`–`40003F` | United Kingdom | RAF / RN / AAC |
| `43C000`–`43CFFF` | United Kingdom | RAF / RN / AAC |
| `444000`–`446FFF` | Austria | Österreichisches Bundesheer / Luftstreitkräfte |
| `44F000`–`44FFFF` | Belgium | Belgian Air Component |
| `457000`–`457FFF` | Bulgaria | Bulgarian Air Force |
| `45F400`–`45F4FF` | Denmark | Flyvevåbnet |
| `468000`–`4683FF` | Greece | Hellenic Air Force |
| `473C00`–`473C0F` | Hungary | Magyar Légierő |
| `478100`–`4781FF` | Norway | Luftforsvaret |
| `480000`–`480FFF` | Netherlands | Koninklijke Luchtmacht |
| `48D800`–`48D87F` | Poland | Siły Powietrzne |
| `497C00`–`497CFF` | Portugal | Força Aérea Portuguesa |
| `498420`–`49842F` | Czech Republic | Vzdušné síly Armády ČR |
| `4B7000`–`4B7FFF` | Switzerland | Schweizer Luftwaffe |
| `4B8200`–`4B82FF` | Turkey | Türk Hava Kuvvetleri |
| `70C070`–`70C07F` | Oman | Royal Air Force of Oman |
| `710258`–`71028F` | Saudi Arabia | Royal Saudi Air Force |
| `710380`–`71039F` | Saudi Arabia | Royal Saudi Air Force |
| `738A00`–`738AFF` | Israel | Israeli Air Force / IDF |
| `7CF800`–`7CFAFF` | Australia | RAAF / RAN / Australian Army |
| `800200`–`8002FF` | India | Indian Air Force / Indian Navy / Indian Army |
| `ADF7C8`–`ADF7CF` | United States | US Military (sub-block) |
| `ADF7D0`–`ADF7DF` | United States | US Military (sub-block) |
| `ADF7E0`–`ADF7FF` | United States | US Military (sub-block) |
| `ADF800`–`ADFFFF` | United States | US Military (sub-block) |
| `AE0000`–`AFFFFF` | United States | USAF / USN / USMC / US Army / USCG (main DoD block) |
| `C20000`–`C3FFFF` | Canada | Royal Canadian Air Force |
| `E40000`–`E41FFF` | Brazil | Força Aérea Brasileira / Marinha / Exército |

### Disabled / collision-prone ranges

The following ranges appear in older lists but are disabled in the upstream community source because they overlap with civilian aircraft and would generate false positives:

| Hex Range | Country | Notes |
|-----------|---------|-------|
| `506F32`–`506FFF` | Slovenia | Disabled — civilian collisions |
| `E80600`–`E806FF` | Chile | Disabled — civilian collisions |

### Notable gaps

Several major military operators do not have dedicated published sub-allocations in the community lists, either because they share the national civilian block, do not broadcast distinguishably on ADS-B, or their assignments are not publicly documented:

- Russia
- China
- North Korea
- Iran
- Pakistan
- Ukraine
- South Korea (ROKAF)
- Japan (JASDF / JMSDF / JGSDF)
- Most of Africa, Central Asia, and South-East Asia

## Sources

- [readsb `aircraft.c` — `MIL_RANGES`](https://github.com/wiedehopf/readsb/blob/dev/aircraft.c) (canonical community list)
- [tar1090-db `ranges.json`](https://github.com/wiedehopf/tar1090-db/blob/master/ranges.json)
- [Mictronics aircraft database](https://mictronics.de/aircraft-database/)
- [Eurocontrol Mode S / ADS-B Military Compendium](https://www.eurocontrol.int/sites/default/files/2024-05/eurocontrol-compendium-mode-s-ads-b-military.pdf)
- [sdr-enthusiasts/plane-alert-db](https://github.com/sdr-enthusiasts/plane-alert-db)
