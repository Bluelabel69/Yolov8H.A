"""import asyncio
import cv2
import io
import logging
import numpy as np
from homeassistant.components.camera import Camera
from homeassistant.helpers import aiohttp_client
from ultralytics import YOLO

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    camera_entity_id = config_entry.data["camera_entity_id"]
    yolo_weights_path = config_entry.data["best.py"]

    camera = YoloCamera(hass, camera_entity_id, yolo_weights_path)
    async_add_entities([camera])

class YoloCamera(Camera):
    def __init__(self, hass, camera_entity_id, yolo_weights_path):
        super().__init__()
        self._hass = hass
        self._camera_entity_id = camera_entity_id
        self._yolo_weights_path = yolo_weights_path
        self._yolo_model = YOLO(yolo_weights_path)

    async def async_camera_image(self):
        image = await self._hass.components.camera.async_get_image(self._camera_entity_id)
        img_array = np.frombuffer(image.content, dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        results = self._yolo_model.predict(img)
        _, img_buffer = cv2.imencode(".jpg", results.render())
        return img_buffer.tobytes()
"""


from homeassistant.components.camera import Camera
from homeassistant.const import CONF_NAME
from . import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    camera_entity_id = entry.data["camera_entity_id"]
    yolov8_camera = YOLOv8Camera(hass, camera_entity_id)
    async_add_entities([yolov8_camera])

class YOLOv8Camera(Camera):
    def __init__(self, hass, camera_entity_id):
        super().__init__()
        self._hass = hass
        self._camera_entity_id = camera_entity_id
        self._name = f"{DOMAIN.capitalize()} {CONF_NAME}"

    async def async_camera_image(self):
        processed_image_path = self._hass.data[DOMAIN]["processed_image_path"]
        with open(processed_image_path, "rb") as file:
            return file.read()

    @property
    def name(self):
        return self._name
