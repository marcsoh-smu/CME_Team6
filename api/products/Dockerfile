#You are at /CME_TEAM6 in the yml file
FROM python:3.8-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY config.env .
RUN pip3 install -r requirements.txt
COPY ./api/products/products.py .
CMD [ "python3", "./products.py"]