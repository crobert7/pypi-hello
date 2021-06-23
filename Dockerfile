FROM python:3.9.5
LABEL maintainer="Roberto Garcia"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["flask", "run"]