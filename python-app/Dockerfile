FROM python:3.9-slim

WORKDIR /python-app

COPY . /python-app
COPY requirements.txt /python-app
ADD swagger.yml /python-app
RUN python -m pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

CMD python app.py
