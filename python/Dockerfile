from python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install mysqlclient
COPY . .
WORKDIR /usr/src/app/flaskFiles

CMD ["flask", "run", "--host=0.0.0.0"]
