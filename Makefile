# SHELL := /bin/zsh

# export PYTEST_V = $(shell pytest --version | grep -oE '\d+\.\d+\.\d+')

check_install: 
	pytest --version
