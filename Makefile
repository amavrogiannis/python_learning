# SHELL := /bin/zsh

# export PYTEST_V = $(shell pytest --version | grep -oE '\d+\.\d+\.\d+')

check_install: 
	pytest --version

jenkins-network:
	docker network create jenkins

jenkins-run:
	docker run \
	--name jenkins-docker \
	--rm \
	--detach \
	--privileged \
	--network jenkins \
	--network-alias docker \
	--env DOCKER_TLS_CERTDIR=/certs \
	--volume jenkins-docker-certs:/certs/client \
	--volume jenkins-data:/var/jenkins_home \
	--publish 2376:2376 \
	docker:dind \
	--storage-driver overlay2

jenkins-build:
	docker build -t jenkins-blueocean:version1 .

jenkins-ui:
	docker run \
	--name jenkins-blueocean \
	--restart=on-failure \
	--detach \
	--network jenkins \
	--env DOCKER_HOST=tcp://docker:2376 \
	--env DOCKER_CERT_PATH=/certs/client \
	--env DOCKER_TLS_VERIFY=1 \
	--publish 8080:8080 \
	--publish 50000:50000 \
	--volume jenkins-data:/var/jenkins_home \
	--volume jenkins-docker-certs:/certs/client:ro \
	jenkins-blueocean:version1

jenkins-stop:
	docker stop jenkins-docker
	docker stop jenkins-blueocean

jenkins-start:
	docker start jenkins-docker
	docker start jenkins-blueocean