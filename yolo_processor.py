import asyncio
import cv2
import json
import numpy as np
import os
from ultralytics import YOLO
from homeassistant.components.camera import async_get_image

async def process_camera_image(hass, camera_entity_id, model):
    # Obter imagem da câmera do Home Assistant
    image = await async_get_image(hass, camera_entity_id)

    # Converter a imagem para um formato que o YOLO possa processar
    img_array = np.frombuffer(image, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Processar a imagem com o modelo YOLO
    results = model.predict(img)

    # Exibir a imagem processada (opcional)
    cv2.imshow("YOLO Processed Image", results.render())
    cv2.waitKey(0)
    cv2.destroyAllWindows()

async def main():
    # Configurar o modelo YOLO
    model = YOLO("D:\\Python\\Programa Principal\\runs\\detect\\train32\\weights\\best.pt")

    # Carregar as opções do add-on
    with open("/data/options.json") as f:
        options = json.load(f)

    camera_entity_id = options["camera_entity_id"]

    # Inicializar o Home Assistant API e processar a imagem da câmera
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.core import HomeAssistant

    hass = HomeAssistant()
    await hass.async_add_executor_job(process_camera_image, hass, camera_entity_id, model)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
