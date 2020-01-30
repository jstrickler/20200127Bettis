#!/usr/bin/env python
import requests

BETTIS_URL = "https://navalnuclearlab.energy.gov/about-us/bettis-atomic-power-laboratory/"


response = requests.get(BETTIS_URL)
if response.status_code == requests.codes.OK:
    print(response.content.decode())
print('-' * 60)

IMAGE_URL = "https://navalnuclearlab.energy.gov/images/testimonials/Herminio.png"


response = requests.get(IMAGE_URL)
if response.status_code == requests.codes.OK:
    with open('herminio.png', 'wb') as herm_out:
        herm_out.write(response.content)
