# Pupper Keyboard Controller

## Install
### Install PyGame
```bash
pip install pygame
```

### Install UDPComms
```bash
git clone https://github.com/stanfordroboticsclub/UDPComms.git
sudo bash UDPComms/install.sh
```

To set up UDPComms since there are no hardware devices actually attached run:

```bash
sudo ifconfig en1 10.0.0.52 netmask 255.255.255.0
```

## Controls
* wasd: left joystick
* arrow keys: right joystick
* q: L1
* e: R1
* ijkl: d-pad
* x: X
* square: u
* triangle: t
* circle: c