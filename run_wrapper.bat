pip install virtualenv
virtualenv venv
venv/scripts/activate
pip install --upgrade pip
pip install -r requirements.txt

pythoncommand = ("bat execute_wrapper.py)
echo "calling: ${pythoncommand}"