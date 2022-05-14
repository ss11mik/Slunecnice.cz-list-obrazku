#!/usr/bin/env python3
#
# Slunecnice.cz Images Grabber
#
# (c) ss11mik 2021-2022
# works as of 14/05/2021
#

import re
import urllib.request, urllib.error, urllib.parse
from time import sleep
import sys


url = 'https://www.slunecnice.cz/'

category = sys.argv[1]


# optional cooldown to avoid triggering DoS protection
# in seconds
delay = 0


emptyPageSign = "Pro zadané filtrování nebyly nalezeny žádné produkty."


html_page = '\
<!doctype html>\n\
<html>\n\
    <head>\n\
        <title>Slunecnice.cz Images Grabber</title>\n\
    </head>\n\
    <body>\n\
    {}\n\
    </body>\n\
</html>\n'




sw_links = []
img_links = {}


print("<!-- Phase 1: grabbing list of SW -->")
# grab links to SW

i = 0
while True:
    i += 1
    sleep(delay)

    tmpurl = "{}{}{}{}".format(url, category, '/?pi=', i)
    print("<!-- [", i, "] ", tmpurl, " -->")


    response = urllib.request.urlopen(tmpurl)
    webContent = response.read().decode('UTF-8')

    if emptyPageSign in webContent:
        # a page without results. end grabbing list and move on
        print("<!-- end of results on page No.", i, " -->")
        break

    for a in re.findall(r"<a class=\"product__heading__link\" href=\".*\">", webContent):
        # dirty workaround around "https://www.slunecnice.cz/sw/seznam-cz-prohlizec/" link
        if "https://" in a:
            continue


        link = a.replace("<a class=\"product__heading__link\" href=\"", "")
        link = link.replace("\">", "")

        sw_links.append(link)



print("<!-- Phase 2: grabbing details of SW -->")
# grab links to images from pages of SW

for link in sw_links:
    sleep(delay)

    tmpurl = "{}{}".format(url, link)
    print("<!-- ", tmpurl, " -->")


    response = urllib.request.urlopen(tmpurl)
    webContent = response.read().decode('UTF-8')

    for a in re.findall(r"<img\nclass=\"product-gallery__image\"\nsrc=\".*\"\nalt=\".*\">", webContent):

        img_link = a.replace("<img\nclass=\"product-gallery__image\"\nsrc=\"", "")
        img_link = re.sub(r"\"\nalt=\".*\">", "", img_link)

        img_links[img_link] = link

        break # grab only 1st link in this sw




print("<!-- Phase 3: create page with images only -->")
# grab links to images from pages of SW

html_body = ""
for img_link, sw_link in img_links.items():
    html_body += "<a href=\"https://slunecnice.cz{}\"><img src=\"{}\"></a>".format(sw_link, img_link)

print(html_page.format(html_body))
