FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN cp .env.dist .env

CMD ["gunicorn","-b","0.0.0.0:80","garryarts.wsgi"]