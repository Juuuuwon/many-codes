FROM python:3.8-slim

RUN pip install fastapi uvicorn

EXPOSE 8080

CMD python3 fastapi-template.py