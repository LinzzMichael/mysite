!/bin/bash
echo "conf the web server"
nginx -c /home/workspace/mysite/conf/nginx/nginx.conf
uwsgi /home/workspace/mysite/conf/uwsgi/mysite_uwsgi.ini -d /home/workspace/mysite/conf/uwsgi/uwsgi.log
