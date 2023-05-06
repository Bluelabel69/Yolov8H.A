DOMAIN = "Yolov8_custom"

from .config_flow import YOLOv8ConfigFlow

async def async_setup(hass, config):
    hass.data[DOMAIN] = {}
    return True

async def async_setup_entry(hass, entry):
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Carregue o componente da câmera
    hass.async_create_task(hass.config_entries.async_forward_entry_setup(entry, "camera"))

    return True

async def async_remove_entry(hass, entry):
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
