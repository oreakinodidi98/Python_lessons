# CI/CD with Jenkins

CI/CD: streamlining the Software Release Process
SDLC: Software Development Lifecycle
deployment phase: ship to end users

## CI (continous integration)

- **Continuous Integration (CI)**: Integrating code changes into a shared repository frequently to detect and fix integration issues early.
- build pipeline
- developer -> VC -> Compile -> package -> Unit/UI teesting
- What is integration:
  - multiple developers working on the same codebase indepenently and on the same time
  - developers frequently merge theit code changes into a shared repo
  - executes automated tests to identify bugs and regressions early
  - each integration is verified by an automated build
  - automated process to allow multiple developers to have the code merged

## CD

- **Continuous Deployment/Delivery (CD)**: Automating the deployment process so that code changes can be released to production or a test
environment seamlessly and frequently.
- Release/deployment pipeline
- Opertations team -> Auto Script -> Test Enviroment -> Testig -> Public/GA
- continous deployment: pushed the approved changes to production
- faster release cycles
- delivery : manual approval
- Deployment : authomated
- deployment Stratergies:
- Blue -green deployment: 2 identical enviroments , one active (blue) and one idle (green) . Traffic is switched to green enviroment after successful deployment
- Canary Release: Gradually roll out the new version to a small subset of users before a full scale release
- [Build -> Test] -> Acceptance test(code works end to tend with the platform) -> Deploy to staging -> Deploy to production

## CI/CD Pipeline

- plan -> code -> build -> test -> Release -> Deploy -> operate -> monitor

## Branching Stratergy

- main
- pre-prod
- staging
- develop
- feature

## Jenkins

- Open-Source: Freely available and customizable to specific needs.
- can be hosted on an online server or your own server
- Plugins: Extensive library of plugins for various tools and integrations.
  - you have a Docke and Kubernetes plugin 
- Build Automation: Automates tasks like compiling code and running tests.
- Continuous Integration/Deployment (CI/CD): Supports automating the CI/CD pipeline
- Pipeline as Code: Defines workflows using declarative syntax for improved readability.
- Job Scheduling: Schedules builds and deployments at specific times or intervals
- Reporting and Monitoring: Provides detailed reports and visualizations of build history and test results.

### Key Concept Definition

- Jobs: Define the tasks to be automated in the CI/CD pipeline
- Plugins: Extend Jenkins functionality and integrate with different tools
- Builds: The process of compiling and packaging the source code
- Pipelines: A sequence of jobs that define the entire CI/CD workflow
- Node: A machine where Jenkins runs tasks.

### Key Architecture

- Master-agent architecture
- Master: manages build jobs, schedules builds, allocates agents
- Agents: perform the actual builds, can be on different machines
- Plugins extend core functionality

### Basic Jenkins Workflow

1. Developers commit code to the repository
2. Jenkins detects changes and triggers a build
3. Build is executed (compile, test, package)
4. Results are reported
5. If successful, the build is deployed
![Jenkins WorkFlow](image.png)

### SetUp

1. Download Docker
2. docker -v : check version
3. docker network ls : check network
4. docker network create jenkins : create jenkins network
5. [Follow these instructions](https://www.jenkins.io/doc/book/installing/docker/)
6. Create Dockerfile
7. include python3-pip, python3 to be downloaded
8. Build a new docker image from this Dockerfile, and assign the image a meaningful name
9. docker build -t myjenkins-blueocean:2.452.2-1 .
10. Store in Github Repo
11. docker images -t myjenkins-blueocean:2.452.
12. Run myjenkins-blueocean:2.452.2-1 image as a container in Docker
13. From the Jenkins console log output, copy the automatically-generated alphanumeric
14. Browse to http://localhost:8080 (or whichever port you configured for Jenkins when installing it)
15. Login to the Jenkins
16. Now server is running

```docker
docker run --name jenkins-blueocean --restart=on-failure `
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 `
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 `
  --volume jenkins-data:/var/jenkins_home `
  --volume jenkins-docker-certs:/certs/client:ro `
  --publish 8080:8080 --publish 50000:50000 myjenkins-blueocean:2.452.2-1
```

## To run tests

- Create App with Functions to perform basic calulations
- Create test.py file
- Include pytest in requirements file
- Run: pytest -vvvv

## Create a Jenkins Build

- New item
- Frestyle project
- Configure
  - include : Delete workspace before build starts
  - Build Steps: Execute shell commands -> echo "hello world"
- Click "Build now" to test build