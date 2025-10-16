sudo apt update
sudo apt install python3-venv python3-full

cd /home/user/Documentos/restapi
python3 -m venv venv

pip install flask

deactivate

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

source venv/bin/activate

python app.py
