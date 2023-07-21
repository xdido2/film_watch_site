migrate:
	python manage.py makemigrations
	python manage.py migrate
del_mig:
	rm -rf apps/movies/migrations/*
	rm -rf apps/users/migrations/*
	rm -rf apps/site_info/migrations/*
	touch apps/movies/migrations/__init__.py
	touch apps/users/migrations/__init__.py
	touch apps/site_info/migrations/__init__.py

both:
	make del_mig
	make migrate