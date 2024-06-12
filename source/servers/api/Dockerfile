FROM python:3

COPY app/ /app/
COPY ../../_config/ /app/config
COPY ../../datafiles/ /app/datafiles
ADD requirements.txt /app/

RUN pip install -r /app/requirements.txt

EXPOSE 7301

CMD [ "python", "/app/app.py" ]