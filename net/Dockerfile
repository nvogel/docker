FROM python:2.7


COPY files/requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

ADD files/app /app
ADD files/app.py /
ADD files/multicast.py /

EXPOSE 8080

WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
