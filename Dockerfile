FROM python:3.11
WORKDIR /django_app
COPY app app
COPY core core
COPY manage.py /django_app/manage.py
COPY requirements.txt /django_app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]