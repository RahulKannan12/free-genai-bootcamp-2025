# Task 2

## Description

Try orchestrating multiple services together - Choose a megaservice and try deploying in local machine

Outcome - How megaservice orchestrated multiple services together, document it

## Working Notes

I chose **code-translation application** (megaservice) to play around

[OPEA documentation for Code Translation Application¶](https://opea-project.github.io/latest/GenAIExamples/CodeTrans/README.html)

## Observations


### Easy method first

Tried using the megaservice docker [image](https://hub.docker.com/r/opea/codetrans)

```
docker pull opea/codetrans:latest

docker run opea/codetrans:latest
```

Did some environment variable setup as per the [doc](https://opea-project.github.io/latest/GenAIExamples/CodeTrans/README.html)

Services aren't running 👎

### Running each microservices seperately 

Reference - [Running Each Microservices Seperately](https://opea-project.github.io/latest/GenAIExamples/CodeTrans/docker_compose/intel/cpu/xeon/README.html)

Cloned GenAIExamples Repo

```
git clone https://github.com/opea-project/GenAIComps.git
```

```
meta-llama/Llama-3.2-1B-Instruct

docker run -e LLM_MODEL_ID=meta-llama/Llama-3.2-1B-Instruct -p 7777:7777 -p 8000:8000 opea/codetrans:latest
```

⛳ Tried multiple ways, couldn't able to run the megaservice completely in Mac, it is closely binded to run only intel xeon / gaudi processors

Dockers are composed in such a way

```
no matching manifest for linux/arm64/v8 in the manifest list entries
```

the usual error message I'm getting trying multiple ways