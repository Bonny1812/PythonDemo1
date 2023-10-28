
py -3 -m venv .venv

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

pip install -r requirements.txt

.venv\scripts\activate

 pip install --upgrade setuptools wheel


python setup.py sdist

python setup.py bdist_wheel