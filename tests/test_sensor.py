"""Tests for the sensor entity."""
from pytest_homeassistant_custom_component.common import MockConfigEntry
from unittest.mock import AsyncMock, Mock

from custom_components.tuya_local.const import (
    CONF_DEVICE_ID,
    CONF_TYPE,
    DOMAIN,
)
from custom_components.tuya_local.generic.sensor import TuyaLocalSensor
from custom_components.tuya_local.sensor import async_setup_entry


async def test_init_entry(hass):
    """Test the initialisation."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        data={
            CONF_TYPE: "goldair_dehumidifier",
            CONF_DEVICE_ID: "dummy",
            "humidifier": False,
            "sensor_current_temperature": True,
            "sensor_current_humidity": False,
        },
    )
    m_add_entities = Mock()
    m_device = AsyncMock()

    hass.data[DOMAIN] = {
        "dummy": {"device": m_device},
    }

    await async_setup_entry(hass, entry, m_add_entities)
    assert (
        type(hass.data[DOMAIN]["dummy"]["sensor_current_temperature"])
        == TuyaLocalSensor
    )
    m_add_entities.assert_called_once()
