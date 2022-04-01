#You are at /CME_TEAM6 in the yml file
FROM python:3.8-alpine
WORKDIR /usr/src/app
COPY requirements.txt .
#COPY ./api/orders/secrets_manager.py .
RUN pip3 install -r requirements.txt
COPY ./api/orders/orders.py .
CMD [ "python3", "./orders.py"]