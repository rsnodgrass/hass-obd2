"""
OBD-II OBD-II for Home Assistant
See https://github.com/rsnodgrass/hass-obd2
"""
import logging

import time
import voluptuous as vol
from datetime import datetime, timedelta
import dateutil.parser
from requests.exceptions import HTTPError, ConnectTimeout

from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv, discovery
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.dispatcher import dispatcher_send, async_dispatcher_connect
from homeassistant.helpers.event import track_time_interval
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.const import CONF_NAME, CONF_SCAN_INTERVAL

from .const import (ATTR_BATTERY_VOLTAGE, 
                    ATTR_ATTRIBUTION, ATTRIBUTION
                    DOMAIN)

LOG = logging.getLogger(__name__)

MIN_SCAN_INTERVAL_IN_SECONDS = 30

CONFIG_SCHEMA = vol.Schema({
        DOMAIN: vol.Schema({
            vol.Optional(CONF_SCAN_INTERVAL, default=60):
                vol.All(vol.Coerce(int), vol.Range(min=MIN_SCAN_INTERVAL_IN_SECONDS))
        })
    }, extra=vol.ALLOW_EXTRA
)

def setup(hass, config):
    """Initialize the OBD-II integration"""
    hass.data[DOMAIN] = {}
    conf = config[DOMAIN]

#    try:
#        obd2_service = PyOBD-II(username, password)
#        hass.data[OBD-II_SERVICE] = obd2_service

#    except (ConnectTimeout, HTTPError) as ex:
#        LOG.error("Unable to connect to OBD-II: %s", str(ex))
#        return False

    def refresh_data(event_time):
        """Call OBD-II service to refresh latest data"""
        return

class OBD-IIEntity(RestoreEntity):
    """Base Entity class for OBD-II devices"""

    def __init__(self, hass, config, name_suffix, sensor_info, unit_system, measure):
        self.hass = hass

        self._device_id = sensor_info.get('id')

        self._attrs = {}
        self._name = f"{sensor_info.get('name')} {name_suffix}"

    @property
    def name(self):
        """Return the display name for this sensor"""
        return self._name

    @property
    def icon(self):
        return MEASURES[self._field_name].get('icon') or 'mdi:gauge'

    @property
    def state(self):
        return self._state

    @property
    def device_state_attributes(self):
        """Return the device state attributes."""
        return self._attrs

    @callback
    def _update_callback(self):
        return

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()        

    @callback
    def _schedule_immediate_update(self):
        self.async_schedule_update_ha_state(True)
