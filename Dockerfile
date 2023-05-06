ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3 py3-pip \
    && pip3 install --no-cache --upgrade pip setuptools wheel \
    && pip3 install --no-cache ultralytics_yolov5 homeassistant

# Copie os arquivos do projeto
COPY run.sh /
COPY yolo_processor.py /

# Torne o script executável
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
