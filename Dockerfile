FROM python:latest
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY app.py config_update_check.py /
CMD gunicorn -b 0.0.0.0:8000 --log-level debug app:api
