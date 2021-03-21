FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# Configuracion de los drivers de oracle
RUN apt update && apt install -y libaio1 unzip wget
RUN mkdir -p /opt/oracle
RUN wget -O /opt/oracle/instantclient_21_1.zip https://download.oracle.com/otn_software/linux/instantclient/211000/instantclient-basiclite-linux.x64-21.1.0.0.0.zip
RUN unzip /opt/oracle/instantclient_21_1.zip -d /opt/oracle
ENV PATH="/opt/oracle/instantclient_21_1:${PATH}"
ENV LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/opt/oracle/instantclient_21_1"

# administracion de los requerimientos del proyecto
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# proyecto y config del mismo
COPY ./app /app/app
COPY ./.env-prod /app/.env
COPY ./server_conf.py /app/app/gunicorn_conf.py
COPY ./logging.conf /app/logging.conf
