#!/bin/sh

MODULE=${MODULE:-website}
NGINX_CONF=/etc/nginx/nginx.conf

# Specify Django module name
sed -i "s#module=website.wsgi:application#module=${MODULE}.wsgi:application#g" uwsgi.ini
sed -i "s#pidfile=/tmp/website.pid#pidfile=/tmp/${MODULE}.pid#g" uwsgi.ini
sed -i "s#daemonize=/var/log/uwsgi/website.log#daemonize=/var/log/uwsgi/${MODULE}.log#g" uwsgi.ini

# Check Django framework structure
if [ ! -f "manage.py" ]
then
    echo "creating basic django project (module: ${MODULE})"
    django-admin.py startproject ${MODULE} 
fi

# Initialize system
python manage.py collectstatic --noinput
# Check availability of MySQL instance
while ! nc -z mysql 3306; do sleep 1; done
python manage.py migrate --noinput --fake-initial

# Generate nginx.conf
mkdir -p /run
cat > $NGINX_CONF << END
worker_processes 4;
pid /run/nginx.pid;

events {
    worker_connections 1024;
}

http {
    include mime.types;
    default_type application/octet-stream;
    sendfile on;
    keepalive_timeout 65;

    include /etc/nginx/conf.d/*.conf;
}
END

# Run nginx
/usr/sbin/nginx

# Start uwsgi
uwsgi --ini uwsgi.ini --touch-reload reload
