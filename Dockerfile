From python:3

ENV PYTHONBUFFERED=1

WORKDIR /merchapp

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver"]