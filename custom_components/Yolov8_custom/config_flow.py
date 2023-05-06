from homeassistant import config_entries

DOMAIN = "Yolov8_custom"

class YOLOv8ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="YOLOv8", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("camera_entity_id"): str,
                    vol.Required("weights_path"): str,
                }
            ),
        )
