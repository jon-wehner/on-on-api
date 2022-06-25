FROM python:3.10

# Setup Flask environment
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV SQLALCHEMY_ECHO=True

EXPOSE 8000

WORKDIR /var/www
COPY . .

# Install Python Dependencies
RUN pip install -r requirements.txt
RUN pip install psycopg2

# Run flask environment
CMD gunicorn app:app