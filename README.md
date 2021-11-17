# Coach Hub Interview Challenge
Repository for the technical assignment for Coach Hub

**Contents**:
1. [Development Environment](#development-environment)
2. [Building the server with docker](#building-the-server-with-docker)

## **Development Environment**

In order to run through all the steps of this README you must make sure you have `Docker` working on your machine. 
The stack used for this project was:
 - [Windows 10 host machine]
 - [Windows Subsystem for Linux 2](https://docs.microsoft.com/en-us/windows/wsl/install)
 - [Docker Desktop](https://www.docker.com/products/docker-desktop)
 - [Ubuntu 18.06](https://www.microsoft.com/store/productId/9N9TNGVNDL3Q)
 - [Pyenv (Python 3.8.7)](https://pypi.org/project/pyenv/)
 - [Poetry](https://python-poetry.org/)


You don't need to have this exact stack, however you do need to have a linux machine, docker and preferably a virtual environment.

To start, clone this repo:

`git clone https://github.com/joaoguerreiro779/coachhub_challenge.git`

Make sure you have the necessary dependencies for pyenv:

`sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \`
`libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \`
`libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev`

Get pyenv installer:

`curl https://pyenv.run | bash`

Optionally, add `pyenv` to path by adding the following to the ~/.bashrc file:

`export PATH="$HOME/.pyenv/bin:$PATH"`

`export PATH="$PYENV_ROOT/bin:$PATH"`

`eval "$(pyenv init --path)"`

Then, to install the specific `python` version (we will install `python 3.8.7`) run:

`pyenv install 3.8.7`

Activate pyenv on the project's home directory:

`pyenv local 3.8.7`

Download and install poetry:

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

`poetry install`

Note: Poetry will always work isolated from the global Python installation. To achieve this, it will first check if it’s currently running inside a virtual environment. If it is, it will use it directly without creating a new one. 

## **Building the server with Docker**

To build the server with docker, navigate to the server directory and build the docker image with:

`docker build -t coachhub_challenge_server .`

Then run this image on a container exposing host port 5000 to container port 3000

`docker run -p 5000:3000 coachhub_challenge_server`
