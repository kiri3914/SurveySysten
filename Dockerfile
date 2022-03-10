FROM python:3.8 as builder
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /opt/app
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x /opt/app/entrypoint.sh
ENTRYPOINT ["/opt/app/entrypoint.sh"]



