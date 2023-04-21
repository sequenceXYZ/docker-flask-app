FROM python:3.9-slim

WORKDIR /python-app

EXPOSE 5000

COPY . /python-app
COPY requirements.txt /python-app
ADD swagger.yml /python-app
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv

CMD python app.py
