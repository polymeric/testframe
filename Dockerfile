FROM python:3

WORKDIR /usr/src/app

RUN git clone https://github.com/polymeric/testframe.git
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pwd;ls testframe
RUN X=$("testframe/utils/django-secret-keygen.py");echo "SECRET_KEY="$X"" > testframe/testframe/settings_secrets.py


COPY . .

EXPOSE 8000
CMD ["python", "testframe/manage.py", "runserver", "0.0.0.0:8000"]