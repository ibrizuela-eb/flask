FROM python:3.8-slim

WORKDIR /flask
COPY requirements.txt /flask
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /flask

EXPOSE 5000

CMD [ "python", "app.py" ]
