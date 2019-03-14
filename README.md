# Space Invaders

Basic Implementation of the game Space Invaders using `pygame` library in python3

## How to run
* Run all the commands in one terminal tab
* Install python3 and python3-venv
```console
sudo apt install python3 python3-venv
```
* Create a virtual environment, activate the environment and install dependencies
```console
python3 -m venv env
source env/bin/activate
pip install --upgrade pip && pip install -r requirements.txt
```
* Play the game
```console
python3 src/Main.py
```
* After finishing playing, deactivate environment and clean up
```console
deactivate
rm -r env/ src/__pycache__/
```

## Controls
* <kbd>A</kbd> - Move left
* <kbd>D</kbd> - Move Right
* <kbd>SPACE</kbd> - Shoot missile A
* <kbd>S</kbd> - Shoot missile B
* <kbd>Q</kbd> - Quit

## Details
* Missile A kills alien instantly increasing score by 1
* Missile B freezes the enemy for till 5 seconds after it hits the alien
* Aliens spawn randomly around the top region of the screen
