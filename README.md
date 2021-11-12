<h1 align="center">Machine Learning Engineer Take Home Assignment</h1>


# Challenge
In this task, you'll be working in an imaginary team setup.  

Your colleague Alice found out [this text summarizing model](https://huggingface.co/facebook/bart-large-cnn) helps our customer relations team to understand massive amount of requests.  
You can find what she worked on so far in `ml_task/services/summarizer.py` and `notebooks/playground.ipynb`.  
She uses `poetry` as a package manager.  

Now it's yoru turn to shine. Alice asked you to productionize her findings.  
It's OK to upgrade her codebase if necessary.

## Task 1
Please build a Docker based API that summarizes an input text only if the input is English.  
An expected output is in a JSON format that looks like
```
{"summary": "Summarized text"}
```

## Task 2
Please set up a CICD pipeline using Github Actions that does
- Any tasks that you think are necessary to keep this service healthy and maitainable (a.k.a production ready)
- The last steps of the pipeline are to spin up the service, make some sample requests and then shut down the service (No need to deploy the service)

## Task 3
Please provide a documentation by updating this README.md about what you think important regarding your works in Task 1 & 2.

# Submission
Please create a `private` github repo that contains this folder and share with these users
- `yuki-ch`
- `blabla`
- `blabla`
- `blabla`

So that we can see your commits, Github Actions or any activities you like to demonstrate!
Good luck!