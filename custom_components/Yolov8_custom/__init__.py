DOMAIN = "Yolov8_custom"

from .config_flow import YOLOv8ConfigFlow

async def async_setup(hass, config):
    hass.data[DOMAIN] = {}
    return True

async def async_setup_entry(hass, entry):
    hass.data[DOMAIN][entry.entry_id] = entry.data
    hass.async_add_executor_job(main)
    return True

async def async_remove_entry(hass, entry):
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
