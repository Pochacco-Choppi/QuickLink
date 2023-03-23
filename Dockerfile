FROM ubuntu:latest
FROM python

COPY . .

EXPOSE 8000

RUN apt-get update -y

RUN pip install -r requirements.txt
WORKDIR quick_link
CMD ["python", "main.py"]
