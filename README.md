# Text summarization app
Repository for a personal which serves a containarized text summarization application and implements a CI CD pipeline with linting and testing. The idea is to slowly familiarize myself with MLOps and client/server architectures by taking on these small projects.

**Contents**:
1. [Development Environment](#development-environment)
2. [Building the server with docker](#building-the-server-with-docker)

## **Recreate Development Environment (OPTIONAL)**

In order to run through all the steps of this README you must make sure you have `Docker` working on your machine. 
The stack used for this project was:
 - [Windows 10 host machine]
 - [Windows Subsystem for Linux 2](https://docs.microsoft.com/en-us/windows/wsl/install)
 - [Docker Desktop](https://www.docker.com/products/docker-desktop)
 - [Ubuntu 18.06](https://www.microsoft.com/store/productId/9N9TNGVNDL3Q)
 - [Poetry](https://python-poetry.org/)


You don't need to have this exact stack, however you do need to have a linux machine, docker and preferably a virtual environment.

To start, clone this repo:

`git clone https://github.com/joaoguerreiro779/text_summarization_app.git`

Download poetry:

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`

Install packages:

`cd text_summarization_app`

`poetry install`

Note: Poetry will always work isolated from the global Python installation by creating its own virtual environment. We can access this by running:

`poetry shell`

## **Building the server with Docker**

To build the server with docker, navigate to the server directory and build the docker image with:

`docker build -t text_summarization_server .`

Then run this image on a container exposing host port 5000 to container port 3000

`docker run -p 5000:3000 text_summarization_server`

## **Dataset source**

BBC News summary:

`https://www.kaggle.com/pariza/bbc-news-summary`

## **Evaluation Metrics**

ROUGE - Recall Oriented Understudy for Gisting Evaluation, measures recall that is how much the words (and/or n-grams) in the machine generated summaries appear in the machine generated summaries.

BERT score
Ideally, with GPU enabled it would be interesting to explore  text summarization evaluation. Having said this, the truth and summarized text would have to be of the exact same number of sentences which makes it impractical. You can read more about it in the following [paper](https://arxiv.org/pdf/1904.09675.pdf)
 or check the project's [repository](https://github.com/Tiiiger/bert_score).

## **Next steps**

- Include option to add inputs as files
- Migrate to uwsgi
- Support GPU capabilities
- Add linting as a cicd pipeline step
- Investigate options to prevent server overload.
