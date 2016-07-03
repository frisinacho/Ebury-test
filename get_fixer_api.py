import urllib
import json

from trades.models import Rates

# Retrieve EUR rates
eur_url = "http://api.fixer.io/latest?base=EUR"
response = urllib.urlopen(eur_url)
eur = json.loads(response.read())
eur2usd = eur['rates']['USD']
eur2gbp = eur['rates']['GBP']

Rates.eur2usd = eur2usd
Rates.eur2usd.save()
Rates.eur2gbp = eur2gbp
Rates.eur2gbp.save()


# Retrieve GBP rates
gbp_url = "http://api.fixer.io/latest?base=GBP"
response = urllib.urlopen(gbp_url)
gbp = json.loads(response.read())
gbp2usd = gbp['rates']['USD']
gbp2eur = gbp['rates']['EUR']

Rates.gbp2usd = gbp2usd
Rates.gbp2usd.save()
Rates.gbp2eur = gbp2eur
Rates.gbp2eur.save()


# Retrieve USD rates
usd_url = "http://api.fixer.io/latest?base=USD"
response = urllib.urlopen(usd_url)
usd = json.loads(response.read())
usd2eur = usd['rates']['EUR']
usd2gbp = usd['rates']['GBP']

Rates.usd2eur = usd2eur
Rates.usd2eur.save()
Rates.usd2gbp = usd2gbp
Rates.usd2gbp.save()
