FROM python:3.4-alpine
MAINTAINER ddMax <logumb@gmail.com>

# Install dependencies
RUN apk update && \
    apk add --no-cache nginx mariadb-dev

# Install Python requirements
RUN apk add --no-cache build-base linux-headers pcre-dev
ADD requirements.txt /opt/django/
WORKDIR /opt/django/
RUN pip install -r requirements.txt

# Remove libraries
RUN apk del build-base linux-headers pcre-dev

# Setup
ADD . /opt/django
RUN chown -R nginx:www-data /var/lib/nginx && \
    ln -s /opt/django/zjnucloud-api.conf /etc/nginx/conf.d/ && \
    chmod +x /opt/django/run.sh

EXPOSE 80
CMD ["/opt/django/run.sh"]
