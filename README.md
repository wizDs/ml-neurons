# Building workflow involving multiple tasks with LLMs
The purpose of this project is to build a workflow able to describe and assess an ad (picture) using Python, LangChain and OpenAPI.

It has been implemented in two applications, a front-end (Streamlit) and a backend (FastAPI), which each possess a seperate Dockerfile.


# Quick start (based on bash shell):
1. install [Python 3.10](https://www.python.org/downloads/release/python-3124/)
2. install [Docker](https://www.docker.com/)
3. clone this repository `git clone https://github.com/wizDs/ml-neurons.git`
4. change directory to cloned repository `cd {path to directory}`
5. set a .env file with environment variables `touch .env`. Then add `OPENAI_API_KEY` defining the api-key. Optional variable is `MODEL` where default is `gpt-4o` if env variable not set (for overview look at [OpenAI models](https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4))
6. run using `docker compose up`

