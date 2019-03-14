# Space Invaders

Basic Implementation of the game Space Invaders using `pygame` library in python3

## How to run
* Run all the commands in one terminal tab
* Create a virtual environment
```console
sudo apt install python3 python3-venv
python3 -m venv env
```
* Activate the environment and install dependencies
```console
source env/bin/activate
python3 -m pip install -r requirements.txt
```
* To play
```console
python3 Main.py
```
* After finished playing, clean up
```console
deactivate
rm -r env/ __pycache__/
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
