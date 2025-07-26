FROM python:3.11.0

RUN pip install django mysqlclient django-cors-headers djangorestframework
RUN mkdir -p library_management_system

WORKDIR /library_management_system

COPY . /library_management_system

EXPOSE 8000
CMD [ "python","manage.py","runserver" ]

