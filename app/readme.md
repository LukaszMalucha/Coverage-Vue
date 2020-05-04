## Django Vue





HEROKU


AZURE


## Vue

Django + Vue.js

python manage.py runserver --insecure

NPM & VUE setup

npm i -g @vue/cli

npm install vue-chartjs chart.js --save npm install webpack-bundle-tracker

vue create frontend > Manually > Add Router > Y > Lint on save > In package.json > N

cd frontend. npm run serve

vue ui > project > dependencies > webpack-bundle-tracker


## TESTY

cd core/tests


sudo pip install virtualenv
virtualenv venv
virtualenv --python=/usr/bin/python3 venv
source venv/bin/activate

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
./Miniconda3-latest-Linux-x86_64.sh
conda create -n env


conda activate env


coverage run --source=core manage.py test
coverage run --source=user manage.py test
coverage run --source=db_manager manage.py test
coverage run --source=portfolio manage.py test
coverage run --source=api manage.py test
coverage report
coverage html

coverage erase

deactivate (to close your virtualenv)

