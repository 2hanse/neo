build:
	docker build -t health_test .
run:
	docker run -it -d --name health health_test
history:
	docker history health
exec:
	docker exec -it health /bin/bash
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
