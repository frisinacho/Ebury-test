from celery.schedules import crontab
from celery.task import periodic_task


# Executes every 5 minutes
@periodic_task(run_every=(crontab(minute='*/5')), name="retrieve_fixer_api")
def retrieve_fixer_api(self):
    """ TODO: Implements fixer.io API """
