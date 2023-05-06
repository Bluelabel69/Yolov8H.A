DOMAIN = "Yolov8_custom"

async def async_setup(hass, config):
    return True

async def async_setup_entry(hass, entry):
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "camera"))
    return True

async def async_remove_entry(hass, entry):
    await hass.config_entries.async_forward_entry_unload(entry, "camera")
