# minimal audio control web-interface

## setup

### general

pip install -r requirements.txt

#### ubuntu

sudo apt install libasound2-dev
pip install -r linux.requirements.txt

#### windows

pip install -r windows.requirements.txt

### run

python app.py

<http://127.0.0.1:5000>

#### problems with mouse cursor movements on linux wayland?

sudo -E ./venv/bin/python app.py  
(uinput requires root privileges to create the input device. privileges are dropped upon device creation)

## test

pytest .

## links

<http://larsimmisch.github.io/pyalsaaudio/>

<https://github.com/AndreMiras/pycaw>
