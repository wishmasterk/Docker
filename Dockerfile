# base image
FROM python:3.9

# Workdir
WORKDIR /app

# copy
COPY . /app

# run
RUN pip install -r requirements.txt

# Port
EXPOSE 5000

# command
CMD ["python", "./app.py"]