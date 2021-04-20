release: python manage.py migrate
web: daphne recommendation_system.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=recommendation_system.settings -v2