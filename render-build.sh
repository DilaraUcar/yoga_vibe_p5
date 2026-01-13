#!/usr/bin/env bash
set -e  # Exit if anything fails

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Run Django migrations
python manage.py makemigrations
python manage.py migrate



# Collect static files
python manage.py collectstatic --noinput
