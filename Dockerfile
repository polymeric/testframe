FROM python:3

WORKDIR /usr/src/app

RUN git clone https://github.com/polymeric/testframe.git
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN X=$("testframe/utils/django-secret-keygen.py");echo "SECRET_KEY="$X"" > testframe/testframe/settings_secrets.py;cp /usr/src/app/testframe/testframe/


COPY . .

EXPOSE 8000
# To run gunicorn server to run django dev server comment out these two lines
WORKDIR /usr/src/app/testframe/
CMD ./start.sh

# To run django dev server uncomment line below and comment out two lines above
#CMD ["python", "testframe/manage.py", "runserver", "0.0.0.0:8000"]