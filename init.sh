# linking conf files and restarting nginx and gunicorn

# ln - make links between files
# ln [OPTION]... [-T] TARGET LINK_NAME   (1st form)

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
# sudo /etc/init.d/gunicorn restart
