import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
app = Celery("root")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from apps.shared.tasks.get_movies_task import get_movies_from_api
    sender.add_periodic_task(
        crontab(hour=0, minute=3),
        get_movies_from_api.s(),
        name='refresh content data in db',
    )
