#!/bin/bash
#
# This is a bash script for a specific project, which you can see down this link: 'https://github.com/Gr0ki/ABPZ.git'
# The script automates downloading the Django project from a remote repository that sets everything up for the first run.

if [ "$(ls | grep ABPZ)" != "ABPZ" ]; then
    echo
    echo
    echo "<------- Clonning the repository for the Practical Work 1 ------->"
    echo
    git clone --branch PW1 --single-branch https://github.com/Gr0ki/ABPZ.git
fi

if [[ "$PWD" != "ABPZ" ]]; then
    cd "ABPZ"
fi

echo
echo
echo "<------- Setting up a virtual environment ------->"
echo
if [ "$(ls | grep manage.py)" != "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt

echo
echo
echo "<------- Creating a superuser with a username: \"admin\" and password: \"admin\" ------->"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python3 manage.py shell 2>/dev/null
echo "Done!"

echo
echo
echo "<------- Starting up the server... ------->"
echo
python3 manage.py runserver
