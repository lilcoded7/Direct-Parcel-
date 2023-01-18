# build_files.sh
pip install -r requirements.txt

echo 'Building the project...'
python3.9 manage.py collectstatic

echo 'Make Migration...'
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput 

echo 'Collect Static'
python3.9 manage.py collectstatic --noinput --clear 