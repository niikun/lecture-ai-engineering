install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py 
	
lint:
	pylint --disable=R,C *.py
	
test:
	python -m pytest -vv --cov=calCli.py --cov=mylib test/test_*.py

	
all: install lint test