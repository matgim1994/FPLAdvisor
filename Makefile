build:
	docker build -t fpl:latest .

run: build
	docker run --name fpl --rm -it -v .:/app/ -p 8000:8000 -p 8889:8889 fpl:latest

jupyter:
	docker exec -it fpl python3 -m jupyterlab --ip=0.0.0.0 --allow-root --port 8889 --no-browser

test:
	pass

remove_dangling:
	docker image prune