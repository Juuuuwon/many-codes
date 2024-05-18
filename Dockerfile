FROM python:3.8-slim

COPY . . 

RUN pip install fastapi uvicorn

EXPOSE 8080

CMD python3 fastapi-template.py