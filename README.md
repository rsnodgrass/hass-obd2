# OBD-II Car Sensors for Home Assistant

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=WREP29UDAMB6G)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
![beta_badge](https://img.shields.io/badge/maturity-Beta-yellow.png)

Home Assistant integration for wireless ODB-II sensors such as the [ELM327 Mini Bluetooth LE Interface](https://www.amazon.com/obdator-Bluetooth-Scanner-Automotive-Diagnostic/dp/B074DWH8JR/?tag=rynoshark-20) or the [ELM 326 WiFi Interface](https://smile.amazon.com/Interface-Scanner-Diagnostic-Original-Support/dp/B07L4926C1?tag=rynoshark-20). This is not designed for more advanced car diagnostics or for changing settings via OBD-2. This is designed only as exposing a series of available sensors such as battery voltage, temperature, last time car was started, fault and engine codes.

## NOTE: THIS IS NOT IMPLEMENTED, JUST A STUB FOR AN IDEA! LOOKING FOR CONTRIBUTORS TO HELP.

## Support

If you have trouble with installation and configuration, visit the [ELM327 Home Assistant community discussion](https://community.home-assistant.io/t/https://community.home-assistant.io/t/my-new-android-app-bridge-between-car-obd2-and-home-assistant/101425).

This integration was developed to cover use cases for my home integration and released as a contribution to the community. Implementing new features beyond what exists is the responsibility of the community to contribute.

## Installation

### Step 1: Install Custom Components

Mkae sure [Home Assistant Community Store (HACS)](https://github.com/custom-components/hacs) is installed,  then add the "Integration" repository: *rsnodgrass/hass-obd2*.

#### Versions

The 'master' branch of this custom component is considered unstable, alpha quality, and not guaranteed to work.
Please make sure to use one of the official release branches when installing using HACS, see [what has changed in each version](https://github.com/rsnodgrass/hass-sensorpush/releases).

### Step 2: Install an *OBD to JSON* service somewhere (could be a Home Assistant Add-on):

See [OBD-to-JSON ELM327](https://github.com/EstevanTH/OBD-to-JSON_ELM327)

### Step 3: Configure OBD-II integration

Example configuration.yaml entry:



```yaml
obd2:
  json:
    - https://obd2-to-json-elm327.local
    - https://obd2-proxy.local
#### Lovelace

```yaml
entities:
  - sensor.bmw_e30_m3_battery
title: Car Battery Levels
type: entities
```

## Hardware Requirements

* [ELM327 Mini Bluetooth LE Interface](https://www.amazon.com/obdator-Bluetooth-Scanner-Automotive-Diagnostic/dp/B074DWH8JR/?tag=rynoshark-20)
* Bluetooth 4.0 or WiFi hardware compatible with Home Assistant (such as [ELM327 Mini Bluetooth LE Interface](https://www.amazon.com/obdator-Bluetooth-Scanner-Automotive-Diagnostic/dp/B074DWH8JR/?tag=rynoshark-20) or the [ELM 326 WiFi Interface](https://smile.amazon.com/Interface-Scanner-Diagnostic-Original-Support/dp/B07L4926C1?tag=rynoshark-20).
* NOTE: Ideally the ELM327 ODB-II device would hold history and not just return current state (so HA could pull data from while the car was previously driven)


## See Also

* [Community support for Home Assistant ELM327](https://community.home-assistant.io/t/https://community.home-assistant.io/t/my-new-android-app-bridge-between-car-obd2-and-home-assistant/101425)

### Possible projects to leverage

* [Python-OBD](https://pypi.org/project/obd/)
* https://www.npmjs.com/package/react-native-obd2-core?activeTab=readme



## Known Issues

* Not yet implemented!
* detect when the car is actually driven (there is supposedly an engine start detection)

## Rough Notes


ALL LOGIC for communicating with ELM327 or WiFi OBD-2 devices should not existing inside the integration. Something like the [OBD to JSON ELM327](https://github.com/EstevanTH/OBD-to-JSON_ELM327) should be running which exposes JSON data that this plugin accesses "remotely".  This allow innovation and new ways of communicating with OBD-II devices in the future without having to modify the integration itself.

It seems combining a few existing projects, along with a Bluetooth ELM327 receiver (and transmitters from cars) might give us a very interesting ODB-II integration into Home Assistant.

Here are some relevant things I found:

EstevanTH/OBD-to-JSON_ELM327
Relay reading OBD data from an ELM327 chip, producing HTTP + WebSocket JSON outputs & CSV log - EstevanTH/OBD-to-JSON_ELM327

This is really interesting as it exposes the ODB-II data as JSON through a small locally web service. I’m not sure how this would work with Bluetooth ELM327 transmitter devices…and certainly would have to be modified to allow polling data from several cars at the same time.

https://python-obd.readthedocs.io/en/latest/

This works with various ODB-II adapters and streams “real time sensor data, perform diagnostics (such as reading check-engine codes)”.

https://www.amazon.com/obdator-Bluetooth-Scanner-Automotive-Diagnostic/dp/B074DWH8JR/?tag=rynoshark-20

This Bluetooth scanner would be perfect for Home Assistant, since you could just leave these plugged into your car’s ODB-II port all the time. When your car was in range of Home Assistant, the Bluetooth values would be interrogated and would update a bunch of sensors in HA.

Would love to see a hass-elm327 custom_component created that could monitor several cars at once that had ODB-II Bluetooth adapters. This could all be natively done, without need for an iOS or Android app to act as a bridge.
