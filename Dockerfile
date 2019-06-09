FROM python:latest

LABEL Name=examine_files Version=0.1.0

WORKDIR /app
COPY ./Samples/ /app/Samples
COPY ./dist/ /app/dist

RUN pip install dist/*