pip install virtualenv
virtualenv venv
venv/scripts/activate
pip install --upgrade pip
pip install -r requirements.txt

set -x
pythoncommand = ("python3 execute_wrapper.py )
echo "calling: ${pythoncommand}"