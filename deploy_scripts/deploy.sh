#!/bin/bash

pgrep -f manage.py runserver | xargs kill

rm -rf ~/deploy
mkdir ~/deploy

cd ~/deploy

git clone https://github.com/treevesvarndell/dashboard.git

cd ~/deploy/dashboard

virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

python manage.py bower install
python manage.py runserver 0.0.0.0:8080

