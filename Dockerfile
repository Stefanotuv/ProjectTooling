# file to create a container for Django
FROM python:3

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir /project

WORKDIR /project

COPY . .

RUN pip install -r requirements.txt

WORKDIR /project/DTS/

CMD ["ls"]

CMD ["python", "manage.py", "makemigrations", "masterdata"]

CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "createsuperuser", "stefanot", "ste.tuveri@gmail.com", "Pinocchi0", "Pinocchi0"]

CMD ["python", "manage.py",  "runserver", "0.0.0.0:8000"]
