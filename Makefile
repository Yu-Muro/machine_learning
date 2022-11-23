up:
	sudo docker-compose up -d --build app
	sudo docker-compose exec app /bin/bash

down:
	sudo docker stop python_env
	sudo docker-compose down --rmi all
	sudo docker image prune -a -f
	sudo docker volume prune -f
