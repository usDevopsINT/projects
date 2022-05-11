mkdir Tirgul && cd Tirgul
echo "---download and install chrome---"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
echo "please write your user password:"
sudo dpkg -i google-chrome-stable_current_amd64.deb
echo "---download and install LibreOffice---"
wget https://mirror.isoc.org.il/pub/tdf/libreoffice/stable/7.3.3/deb/x86_64/LibreOffice_7.3.3_Linux_x86-64_deb.tar.gz
tar -xvf LibreOffice_7.3.3_Linux_x86-64_deb.tar.gz
cd LibreOffice_7.3.3.2_Linux_x86-64_deb/DEBs
sudo dpkg -i *.deb
touch excelFile.ods
FILENAME=excelFile.ods
mv $FILENAME $FILENAME.jpg
FILENAME=$FILENAME.jpg
file $FILENAME
echo "yes, because the mv commmand change it"
echo "---flask---"
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv 
mkdir flask_app && cd flask_app
python3 -m venv venv
sh 
pip3 install Flask
cat > flask_GET.py << EOF

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def home():
    if request.method == "GET":
        return "GET request"
    else:
        return "not a GET request"


if __name__ == "__main__":
    app.run()
EOF

python3 flask_GET.py &
curl -v http://127.0.0.1:5000
pkill python

alias curl_flask="curl -v http://127.0.0.1:5000"
python3 flask_GET.py &
curl_flask
pkill python

cd
rm -rf Tirgul

$SHELL
