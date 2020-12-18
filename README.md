# Limitless gaming
[![Ilionx Logo](assets/ilionx-logo.svg)](https://www.ilionx.com)

## Intro
This project started as my ([Philip Bollen](https://github.com/trik-flip)) internship assignment, but since it's not finished and more people could benefit from this project the idea was to publish it. but the project itself start way before this date.
have a look at [the background](#background)

<!-- BADGES -->
[![Contributor Covenant](https://img.shields.io/badge/Contributor_Covenant-v2.0_adopted-blue.svg)](CODE_OF_CONDUCT.md)
[![GitHub License badge](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build with Love](https://img.shields.io/badge/built_with-💖-f98888.svg)](CONTRIBUTERS.md)

## Table Of Content
- [Limitless gaming](#limitless-gaming)
  - [Intro](#intro)
  - [Table Of Content](#table-of-content)
  - [Background](#background)
  - [License](#license)
  - [INSTALL](#install)
    - [Preparation (Windows and MacOS)](#preparation-windows-and-macos)
    - [Preparation (Linux)](#preparation-linux)
    - [Assumptions](#assumptions)
      - [Step-1: Set up a virtualenv](#step-1-set-up-a-virtualenv)
      - [Step-2: Get the source code](#step-2-get-the-source-code)
      - [Step-3: Activate Virtual env](#step-3-activate-virtual-env)
      - [Step-4: Install python packages](#step-4-install-python-packages)
  - [USAGE](#usage)
    - [Conditions](#conditions)
    - [Why this hardware?](#why-this-hardware)
    - [Using the program](#using-the-program)
  - [DEVELOPMENT](#development)
  - [WIKI](#wiki)
  - [CONTRIBUTE](#contribute)
    - [Code of Conduct](#code-of-conduct)
- [Many Thanks](#many-thanks)
  
## Background
The assignment started as developing a solution for a Boy called Job, he has ceberal paresis. 
And he, like everybody else, wants to game every now and then. but with his CP he's not able to compete with other people.  
With this project we try to help him, and possibly others. by using not only his hands and fingers as input via the controller, but by adding a camera and/ or microphone, we're able to create more triggers.

## License
We use the [MIT-License](LICENSE) for this project.

## INSTALL
We'll use [Python 3](https://www.python.org/downloads/release/python-386/)
### Preparation (Windows and MacOS)
You can download python [here](https://www.python.org/downloads/)
> NOTE: the installer will ask if you want to install pip, check this box  

follow the installation, once done check if python is installed correct, by searching for python and executing.
### Preparation (Linux)
most Linux user probably know how to install python, but for those who don't go to the terminal and type `sudo apt update && sudo apt install python3 python3-pip`  
It will prompt for a password, gather for some more info and then will prompt again to start the download. enter `Y` and hit ENTER.
once done, check if python and pip are installed correct  
run `python3 --version && pip3 --version`  
the result should look something like 
```bash
Python 3.8.6
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

### Assumptions
- you have python 3.x installed (current version python 3.9, we'll use 3.8.6 since not every packages is updated to 3.9)
- you have pip installed, and know how to install packages with pip
#### Step-1: Set up a virtualenv
Run the following commands to set up a virtualenvironment:
```bash
python3 -m pip install virtualenv
python3 -m venv --system-site-packages limitless-gaming
```
you should now have a virtualenv and activated.
#### Step-2: Get the source code
run the following command the pull the source code from github
`git clone https://github.com/Ilionx/limitless-gaming.git`

you can also clone via ssh or GitHub CLI, 
but if you've setup those you also know how to use them😉
#### Step-3: Activate Virtual env
```bash
cd ./limitless-gaming
# Linux
source ./bin/activate
# Windows
./scripts/activate.ps1
```
> NOTE: This step needs to be repeated everytime you want to use this repo  
#### Step-4: Install python packages
```bash
pip install wheel pylint autopep8 
pip install -r requirements.txt
```
this should install all the packages needed inside the virtualenv, the installation can take a while, depending on you internet speed. the total download size is about 500MB.

## USAGE
### Conditions
You'll need the following hardware to use the system as designed
- a Jetson nano development kit
- a Xbox one or a newer series
- a Xbox adaptive controller
There are workarounds to use the [Xbox adaptive controller on the playstation 4](https://www.youtube.com/watch?v=p3p1RTpW4SI), but these aren't tested.
### Why this hardware?
We use a [Jetson nano development kit](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/), as this [SBC](https://en.wikipedia.org/wiki/Single-board_computer) is strong enough to run realtime AI models.  
And it also has [GPIO](https://en.wikipedia.org/wiki/General-purpose_input/output) ports, which enables it to capture and send electrical signals.

We use the xbox adaptive controller, because it enables us to mimic a press of a button. 
### Using the program
Currently there is only one piece of code which could be classified as functional. this is working with the camera.
To start this program use the following commands:
```bash
python ./src/limitless-gaming.py
```

## DEVELOPMENT
Current there are 2 main programs, one who uses a Camera feed and OpenCV to analyse the feed. this way we could use stickers to trigger an action, it may also be possible to link it to a Neural network, or anything else which could work.

and a module using a microphone, this way we could use voice or sound recognition to detect triggers. the code present uses [MFCC](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum) with [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) to classify sounds.
for more info about how to help develop this project see [Contribute](#contribute)

## WIKI
We believe in [clean code](https://www.freecodecamp.org/news/clean-coding-for-beginners/), so the code should be writen good enough to explain itself.
This however is not always the case, it's not always easy to explain complex code, not matter the amount of comments you place next to it.

## CONTRIBUTE
Your able to contribute by opening a new issue, or reacting to an excisting issue or opening a pull request agains the master branch, thisway the community can disscus the issue, or changes.

for a more detailed view on how to contribute to this project see [Contributing](CONTRUBITING.md)
### Code of Conduct
We are in favour of a safe and fun development environment, that's why we have a [code of conduct](CODE_OF_CONDUCT.md).
this ensures that developers who love to develop can do so.

# Many Thanks
We'd like to thank all of the [contributers](CONTRIBUTERS.md)
