#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pprint

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
pprint(page.contents)
