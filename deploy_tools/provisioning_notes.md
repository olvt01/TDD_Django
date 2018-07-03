Provisioning a new site
=======================

## Required packages:

* nginx
* pyenv
* Python 3.6
* pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git pyenv python3.6

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
└── sites
     ├── DOMAIN1 (eg. staging.my-domain.com)
     │    ├── .env
     │    ├── db.sqlite3
     │    ├── manage.py etc
     │    ├── static
     │    └── virtualenv
     └── DOMAIN2
           ├── .env
           ├── db.sqlite3
           ├── etc
