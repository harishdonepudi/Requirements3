FROM python
FROM httpd:2.4
COPY [^\.]* /usr/local/apache2/htdocs/


WORKDIR /app
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt .

ENV DB_URL=DummyURL
ENV ACCESS_KEY=DummyURL
ENV SECRET_KEY=DummyURL
#this runs when image is built
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python" ,"app.py" ]
