FROM python:3.12.1
 
WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./ /code/app

COPY markets_requests.py /code/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]