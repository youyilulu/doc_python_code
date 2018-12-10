FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /demo
COPY . /demo
WORKDIR /demo
RUN pip install -r requirements.txt
CMD ["python","demo.py"]