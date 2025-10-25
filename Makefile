django@migrate:
	docker exec django-app-chat-bot python manage.py migrate

django@makemigrations:
	docker exec django-app-chat-bot python manage.py makemigrations

django@createsuperuser:
	docker exec -it django-app-chat-bot python manage.py createsuperuser