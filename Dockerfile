FROM python:3.11.0

RUN pip install django mysqlclient django-cors-headers djangorestframework
RUN mkdir -p library_management_system

COPY . /library_management_system

CMD [ "python","/library_management_system/manage.py" ,"runserver"]