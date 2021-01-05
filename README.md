# Q-LABS Limitless gaming
[![Ilionx Logo](assets/ilionx-logo.svg)](https://www.ilionx.com)

## Intro
The project started in 2019 in the Q-LABS, here employees, students and others come to work on innovative projects. this project started when Job came to us and Zuyd University to help him develop a solution for his problem.  But ever since March there has been almost no progress. That's why we're open sourcing the project. This way we hope to contribute to society, help Job get a viable solution quicker, but also making it a more successful project. 

By making this project open source we hope to reach more people, and more people to reach us.

The past 4 months an Intern from Zuyd University has been working on the project, he has mainly been working on the OpenCV and KNN modules.
Also the main choice of hardware and software are further selected by the intern.

[![Contributor Covenant](https://img.shields.io/badge/Contributor_Covenant-v2.0_adopted-blue.svg)](CODE_OF_CONDUCT.md)
[![GitHub License badge](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build with Love](https://img.shields.io/badge/built_with-💖-f98888.svg)](CONTRIBUTERS.md)

## Table Of Content
- [Q-LABS Limitless gaming](#q-labs-limitless-gaming)
  - [Intro](#intro)
  - [Table Of Content](#table-of-content)
  - [Background](#background)
  - [License](#license)
  - [INSTALL](#install)
    - [Preparation (Windows and MacOS)](#preparation-windows-and-macos)
      - [Check installation](#check-installation)
    - [Preparation (Linux)](#preparation-linux)
      - [Check installation](#check-installation-1)
    - [Assumptions](#assumptions)
      - [Step-1: Set up a virtual environment](#step-1-set-up-a-virtual-environment)
      - [Step-2: Get the source code](#step-2-get-the-source-code)
      - [Step-3: Activate virtual environment](#step-3-activate-virtual-environment)
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

Some time ago Job came to Ilionx and Zuyd University with the objective finding a solution for his problem. He, like many others, likes to game every now and then, but his ability to use a normal game controller is limited due to his cerebral paresis.

This is where we (Ilionx) comes into play, as IT-company we've experience with developing new out-of-box solutions for abnormal problems. And with many young developers the spirit is fresh. That's why we adopted this to an Q-LABS project. This is our department where employees can think about and develop out-of-the-box solutions. 

By participating in projects like this, employees get the change to stay a head with new technological developments, stimulate their creativity and gain new knowledge.

The first idea for creating a solution was by using AI and pattern recognition, this way the computer could learn to trigger action when Job wanted to do this, but was unable to do so. 

For more info about the project see [Gaming-with-CP](https://www.ilionx.com/blog/gamen-met-cerebrale-parese-dat-kan-gewoon-bij-q-labs/) and [Alumni-Zuyd](https://www.ilionx.com/wp-content/uploads/2020/01/AZM-ilionx.pdf), both articles are in Dutch.

## License

We use the [MIT-License](LICENSE) for this project.

## INSTALL

We'll use [Python 3](https://www.python.org/downloads/release/python-386/)
### Preparation (Windows and MacOS)

You can download python [here](https://www.python.org/downloads/)

> NOTE: you'll have to check two box which by default aren't checked
>
> 1. `Add Python 3.x to PATH` or `Add Python to environment variables` 
>
> 2. `pip`
>
> in case they are already checked, you don't have to adjust anything

follow the installation, once done check if python is installed correct, by searching for python and executing.

#### Check installation

you should open a terminal window [Windows key] + r, then type `cmd`.

a black terminal should've popped-up 

now type `python --version && pip --version`, if you see something that looks like  

```bash 
Python 3.8.5
pip 20.2.3 from c:\python38\lib\site-packages\pip (python 3.8)
```

then everything is installed correctly.

### Preparation (Linux)

most Linux user probably know how to install python, but for those who don't go to the terminal and type `sudo apt update && sudo apt install python3 python3-pip`  
It will prompt for a password, gather for some more info and then will prompt again to start the download. enter `Y` and hit ENTER.

#### Check installation

once done, check if python and pip are installed correct  
run `python3 --version && pip3 --version`  
the result should look something like 
```bash
Python 3.8.6
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

### Assumptions

- you have python 3.x installed (current version python 3.9, we'll use 3.8.6 since not every packages is updated to 3.9)
  - if something went wrong while or after the installation, try it agian with this guide:[How to install Python 3 on Windows](https://realpython.com/installing-python/#how-to-install-python-on-windows)
- you have pip installed, and know how to install packages with pip
  - if you don't feel confident enough to use pip read this guide: [What is PIP](https://realpython.com/what-is-pip/)

#### Step-1: Set up a virtual environment

Run the following commands to set up a virtual environment:
```bash
python3 -m pip install virtualenv
python3 -m venv --system-site-packages qlabs-limitless-gaming
```
you should now have a virtual environment.

#### Step-2: Get the source code

run the following command the pull the source code from GitHub
`git clone https://github.com/Ilionx/qlabs-limitless-gaming.git`

you can also clone via SSH or GitHub CLI, 
but if you've setup those you also know how to use them😉

#### Step-3: Activate virtual environment

```bash
cd ./qlabs-limitless-gaming
# Linux
source ./bin/activate
# Windows
./scripts/activate.ps1
```
> NOTE: This step needs to be repeated every time you want to use this repo  

#### Step-4: Install python packages

```bash
pip install wheel pylint autopep8 
pip install -r requirements.txt
```
this should install all the packages needed inside the virtual environment, the installation can take a while, depending on you internet speed. the total download size is about 500MB. 

## USAGE

### Conditions

You'll need the following hardware to use the system as designed
- a Jetson Nano development kit
- a Xbox one or a newer series
- a Xbox adaptive controller
There are workarounds to use the [Xbox adaptive controller on the playstation 4](https://www.youtube.com/watch?v=p3p1RTpW4SI), but these aren't tested.

### Why this hardware?

We use a [Jetson nano development kit](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-nano/), as this [SBC](https://en.wikipedia.org/wiki/Single-board_computer) is strong enough to run Realtime AI models.  
And it also has [GPIO](https://en.wikipedia.org/wiki/General-purpose_input/output) ports, which enables it to capture and send electrical signals.

We use the Xbox adaptive controller, because it enables us to mimic a press of a button. 

### Using the program

Currently there is only one piece of code which could be classified as functional. this is working with the camera.
To start this program use the following commands:

```bash
python ./src/limitless-gaming.py
```

## DEVELOPMENT

Current there are 2 main programs, one who uses a Camera feed and OpenCV to analyze the feed. this way we could use stickers to trigger an action, it may also be possible to link it to a Neural network, or anything else which could work.

and a module using a microphone, this way we could use voice or sound recognition to detect triggers. the code present uses [MFCC](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum) with [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) to classify sounds.
for more info about how to help develop this project see [Contribute](#contribute)

## WIKI

We believe in [clean code](https://www.freecodecamp.org/news/clean-coding-for-beginners/), so the code should be written good enough to explain itself.
This however is not always the case, it's not always easy to explain complex code, not matter the amount of comments you place next to it.

## CONTRIBUTE

Your able to contribute by opening a new issue, or reacting to an existing issue or opening a pull request against the master branch, this way the community can discus the issue, or changes.

for a more detailed view on how to contribute to this project see [Contributing](CONTRUBITING.md)

### Code of Conduct

We are in favor of a safe and fun development environment, that's why we have a [code of conduct](CODE_OF_CONDUCT.md).
this ensures that developers who love to develop can do so.

# Many Thanks

We'd like to thank all of the [contributers](CONTRIBUTERS.md)
