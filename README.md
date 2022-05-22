# DSTI DevOps with Adaltas, Spring 2022: Final Project 

This is the final assignment for the DevOps class taught at Data ScienceTech Institute in Paris in Spring 2022. 

The project contains a simple web API written in Python that is deployed using a variety of DevOps tools and processes.

## Installation
1. Clone this repository: ```$ git clone mralbertk/dsti-devops-final```
2. Install redis: [Installing Redis](https://redis.io/docs/getting-started/installation/)
3. Install Docker: [Get Docker](https://docs.docker.com/get-docker/)
4. [Install Python 3](https://www.python.org/downloads/) and dependencies:

```bash 
# Install dependencies
cd your/local/repository
python3 -m pip install -r requirements.txt
```

## Run

### On localhost
```bash
# Launch a local redis instance 
redis-server --daemonize yes

# Launch the API in local
cd .\src\api
uvicorn api:app
```

### Via Docker
```bash
# In repository root
docker-compose up 
```

## Alternative Deployments 
Additional installation, deployment and run instructions:

- [Vagrant](./iac/)


## Use
The API supports the following endpoints:

- `root`: Accepts `get` method.
- `/health`: Accepts `get` method.
- `/user`: Accepts `get`, `post`, `update` and `delete` methods.

Full documentation is available at `/docs`. _(Note: FastAPI supports Swagger by default.)_

## Report 

### Task 1: Create a Web Application
- Re-built the example `userapi` in Python using FastAPI
- Using a redis db instance

### Task 2: Apply CI/CD Pipeline
- Unit & Integration tests implemented with [pytest](https://docs.pytest.org/en/7.1.x/) in `./tests` 
- Run locally from root directory with `pytest -v` 
- _Note: Dependencies must be installed & redis-server must be running for tests to work_

![](images/cicd-local-testing.png)

### Task 3: Infrastructure as Code with Vagrant & Ansible
- Configured a Centos/7 VM using Vagrant and Virtualbox

![](images/virtualbox-in-use.png)

- Provisioned the box using Ansible local

![](images/vagrant-ansible.png)

### Task 4: Build Docker Image
- Available on [dockerhub](https://hub.docker.com/repository/docker/mralbertk/dsti-devops-fastapi)
- Using a multi-stage build

### Task 5: Container Orchestration with Docker Compose
- Configured two containers and a docker volume to persist redis data dump

![](images/docker-compose.png)

### Worthy Mentions

#### Web Application

- I initially built a tasklist in NodeJS with a MongoDB backend based on [this tutorial](url) but 
switched to Python when I could not get the tests to work properly after hours of trying. 

#### Vagrant & Ansible
- It was unexpectedly difficult to find a version of Centos/7 that could run with _sync folders_ on a windows file
system. I ended up using a custom box uploaded by a community member that had the required guest tools installed.
- Centos/7 was not the best choice for my application: My application uses FastAPI which requires Python 3.7, Centos/7 
by default comes with Python 3.6.x. Installing Python 3.8 on the virtual box was interesting, but I would avoid doing
this for a real project.

## Author
**Albert KONRAD**  
Student, Applied MSc in Data Engineering for AI  
albert.konrad@edu.dsti.institute  

## Instructor
**Sergei KUDINOV**  
Big Data Engineer  
sergei@adaltas.com 