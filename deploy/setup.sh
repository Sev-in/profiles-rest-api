#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/Sev-in/profiles-rest-api.git'

PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'

# Set Ubuntu Language
locale-gen en_GB.UTF-8


# Install Python, SQLite and pip
echo "Installing dependencies..."
apt-get update


# We install the necessary tool to add PPA (external repository).
apt-get install -y software-properties-common
# We add the 'deadsnakes' repository to the system so it can find Python 3.8.
add-apt-repository ppa:deadsnakes/ppa -y
# After adding the new repository, we update the package list again.
apt-get update


# CORRECT FORM ✅
apt-get install -y python3.8 python3.8-venv python3.8-dev python3-pip sqlite3 nginx git build-essential

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

python3.8 -m venv $PROJECT_BASE_PATH/env

## Remove the uWSGI version lock to make pip install the latest version
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirement.txt uwsgi

# Run migrations
$PROJECT_BASE_PATH/env/bin/python $PROJECT_BASE_PATH/manage.py migrate

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/deploy/supervisor_profiles_api.conf /etc/supervisor/conf.d/profiles_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart profiles_api

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/deploy/nginx_profiles_api.conf /etc/nginx/sites-available/profiles_api.conf
rm -f /etc/nginx/sites-enabled/default
ln -s -f /etc/nginx/sites-available/profiles_api.conf /etc/nginx/sites-enabled/profiles_api.conf
systemctl restart nginx.service

echo "DONE! :)"