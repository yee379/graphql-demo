PIP ?= ./bin/pip

deps:
	$(PIP) install -r requirements.txt

uvicorn: FORCE
	./bin/uvicorn main:app  --reload

start-mongod: FORCE
	mkdir -p mongodb
	./bin/mongod --config mongod.conf

FORCE: ;
	
