#!/usr/bin/env bash

# Exit if anything fails
set -e

# Update OS packages
apt-get update

# Install libraries needed for Pillow
apt-get install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev \
                   libtiff5-dev tcl8.6-dev tk8.6-dev python3-tk

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
