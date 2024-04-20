build:
	docker build -t fpl:latest .

run: build
	docker run --name fpl --rm -it -v .:/app/ -p 8000:8000 -p 8889:8889 fpl:latest

createsuperuser:
	docker exec -it fpl python3 manage.py createsuperuser

makemigrations:
	docker exec -it fpl python3 manage.py makemigrations

migrate:
	docker exec -it fpl python3 manage.py migrate

jupyter:
	docker exec -it fpl python3 -m jupyterlab --ip=0.0.0.0 --allow-root --port 8889 --no-browser

shell:
	docker exec -it fpl /bin/bash

test:
	docker exec -it fpl python3 manage.py test
	# to run a specific test run e.g. docker exec -it fpl python3 manage.py test fpl.tests.test_views

dumpdata:
	docker exec -it fpl python manage.py dumpdata fpl --indent 4 > fpl/fixtures/fpl.json

loaddata:
	docker exec -it fpl python manage.py loaddata fpl/fixtures/fpl.json

remove_dangling:
	docker image prune