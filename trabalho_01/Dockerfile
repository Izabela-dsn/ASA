FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./src/main.py /code/main.py
COPY ./src/config.py /code/config.py
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host","0.0.0.0","--port","8000","--reload"]
