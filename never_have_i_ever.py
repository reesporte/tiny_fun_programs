import requests as req
from bs4 import BeautifulSoup as bs
import random

html = req.get("https://ricepurity.github.io")
soup = bs(html.text, features="html.parser")

site = [x.text[0:x.text.find("\n")].strip() for x in soup.select("li")]

x = "good ol shit"
while x != "stop":
    try:
        choose = random.choice(site)
        site.remove(choose)
        print("have you ever", choose.strip()[0:-1].lower(), "?")
        x = input("\n[press RETURN for new prompt]\n")
    except Exception as e:
        x = "stop"
        print("no more prompts! goodbye")
