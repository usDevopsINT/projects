FROM ubuntu
WORKDIR /app
COPY flask3.py .
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install flask
EXPOSE 5000
CMD  FLASK_APP=/app/app.py flask run --host=0.0.0.0