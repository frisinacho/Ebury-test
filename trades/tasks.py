from celery.schedules import crontab
from celery.task import periodic_task
from trades.models import Rates

import request


# Executes every 5 minutes
@periodic_task(run_every=(crontab(minute='*/5')), name="retrieve_fixer_api")
def retrieve_fixer_api(self):
    eur = request.GET('http://api.fixer.io/latest?base=EUR')
    eur2usd = eur['rates']['USD']
    eur2gbp = eur['rates']['GBP']

    Rates.eur2usd = eur2usd
    Rates.eur2usd.save()
    Rates.eur2gbp = eur2gbp
    Rates.eur2gbp.save()

    gbp = request.GET('http://api.fixer.io/latest?base=GBP')
    gbp2usd = gbp['rates']['USD']
    gbp2eur = gbp['rates']['EUR']

    Rates.gbp2usd = gbp2usd
    Rates.gbp2usd.save()
    Rates.gbp2eur = gbp2eur
    Rates.gbp2eur.save()

    usd = request.GET('http://api.fixer.io/latest?base=USD')
    usd2eur = usd['rates']['EUR']
    usd2gbp = usd['rates']['GBP']

    Rates.usd2eur = usd2eur
    Rates.usd2eur.save()
    Rates.usd2gbp = usd2gbp
    Rates.usd2gbp.save()

    """
    # Automatic requests
    for currency in CURRENCIES:
        r = request.get('http://api.fixer.io/latest?base=' + currency)

        return None
    """
