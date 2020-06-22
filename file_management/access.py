file-sharing

invonitin@212.227.175.234
Winner!@#0505
username: invonitin
Password: Winner!@#$%0505


Link: https://212.227.175.234:8443/login_up.php
Username: admin
pwd: Xce34!Lm@2020G19


anoop@212.227.175.234
zC9@m7o8


Okay
E-mail: register@invocont.com
Passwort: AXY735@AAE!2020ae

IMAP
imap.ionos.de
PORT: 993

smtp.ionos.de
PORT: 587
==========================

POP3 
——————
pop.ionos.de
PORT: 995

smtp.ionos.de
PORT: 587


<VirtualHost *:80>
    . . .

    Alias /static /var/www/vhosts/invocont.com/myproject/static
    <Directory /var/www/vhosts/invocont.com/myproject/static>
        Require all granted
    </Directory>

    <Directory /var/www/vhosts/invocont.com/myproject/myproject>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess myproject python-home=/var/www/vhosts/invocont.com/myproject/myprojectenv python-path=/var/www/vhosts/invocont.com/myproject
    WSGIProcessGroup myproject
    WSGIScriptAlias / /var/www/vhosts/invocont.com/myproject/myproject/wsgi.py

</VirtualHost>



#!/bin/bash

NAME="myblog"                                   # Name of the application
DJANGODIR=/var/www/myproject/myblog             # Django project directory
SOCKFILE=/var/www/myproject/run/gunicorn.sock   # we will communicate using this unix socket
USER=nginx                                      # The user to run as
GROUP=webdata                                   # The group to run as
NUM_WORKERS=4                                   # How many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=myblog.settings          # Which settings file should Django use
DJANGO_WSGI_MODULE=myblog.wsgi                  # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /var/www/myproject/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user $USER \
  --bind=unix:$SOCKFILE



 <VirtualHost *:80> 
 ServerName mysite.example.com 
 DocumentRoot /home/meetu/p_p/mysite/mysite 
 WSGIScriptAlias / /home/meetu/p_p/mysite/wsgi.py 
 
 # adjust the following line to match your Python path 
 WSGIDaemonProcess mysite.example.com processes=2 threads=15 display-name=%{GROUP} python-home=/var/www/vhosts/mysite/venv/lib/python3.5 
 WSGIProcessGroup mysite.example.com 
 
 <directory /var/www/vhosts/mysite> 
   AllowOverride all 
   Require all granted 
   Options FollowSymlinks 
 </directory> 
 
 Alias /static/ /var/www/vhosts/mysite/static/ 
 
 <Directory /var/www/vhosts/mysite/static> 
  Require all granted 
 </Directory> 
</VirtualHost> 




<VirtualHost *:80>
    ServerName 127.0.0.1
    ServerAlias localhost

    Alias /static /home/meetu/myproject/static/
    WSGIScriptAlias / /home/meetu/myproject/myproject/wsgi.py

    <Directory /home/meetu/myproject/>
            Order deny,allow
            Allow from all
    </Directory>

    DocumentRoot /home/meetu/myproject
    
    ErrorLog /home/meetu/myproject/error.log
    CustomLog /home/meetu/myprojectcustom.log combined
</VirtualHost>



sudo apt-get install libapache2-mod-wsgi-py3

<VirtualHost *:80> 
 # ServerName mysite.example.com 
 ServerName localhost 
 DocumentRoot /home/meetu/myproject/error.log 
 WSGIScriptAlias / /home/meetu/myproject/myproject/wsgi.py 
 
 # adjust the following line to match your Python path 
 WSGIDaemonProcess localhost processes=2 threads=15 display-name=%{GROUP} python-home=/home/meetu/myproject/myprojectenv/lib/python3.6 
 WSGIProcessGroup localhost 
 
 <directory /home/meetu/myproject> 
   AllowOverride all 
   Require all granted 
   Options FollowSymlinks 
 </directory> 
 
 Alias /static/ /home/meetu/myproject/static/ 
 
 <Directory /home/meetu/myproject/static> 
  Require all granted 
 </Directory> 
</VirtualHost>



LIVE


<VirtualHost *:80> 
 ServerName mysite.example.com 
 DocumentRoot /var/www/mysite.example.com
 
 
 #WSGIPythonHome var/www/mysite.example.com/myprojectenv
 #WSGIPythonPath var/www/mysite.example.com
 
 # adjust the following line to match your Python path 
 WSGIDaemonProcess mysite.example.com processes=2 threads=15 display-name=%{GROUP} python-home=/var/www/mysite.example.com/myprojectenv/lib/python3.6 python-path=/var/www/mysite.example.com
 WSGIProcessGroup mysite.example.com 
 
 WSGIScriptAlias / /var/www/mysite.example.com/myproject/wsgi.py process-group=mysite.example.com


#WSGIScriptAlias / /path/to/mysite.com/mysite/wsgi.py
#WSGIPythonHome /var/www/mysite.example.com/myprojectenv
#WSGIPythonPath /var/www/mysite.example.com

<Directory /var/www/mysite.example.com/myproject>
	<Files wsgi.py>
		Require all granted
	</Files>
</Directory>



 <directory /var/www/mysite.example.com> 
   AllowOverride all 
   Require all granted 
   Options FollowSymlinks 
 </directory> 
 
 Alias /static/ /var/www/mysite.example.com/static/ 
 
 <Directory /var/www/mysite.example.com/static> 
  Require all granted 
 </Directory> 
</VirtualHost>
