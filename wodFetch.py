# Script to fetch the WOD from www.crossfit.com daily

import datetime
from lxml import html
import requests

now = datetime.datetime.now()

year = str(now.year)+'/'
month = str(now.month)+'/'
day = str(now.day)

url = "http://www.crossfit.com/"
todays_url = url + year + month + day
id = str(now.year) + str(now.month) + str(now.day)

webpage = requests.get(url)
tree = html.fromstring(webpage.content)

p_tags = tree.xpath("//p")
p_content = [p.text_content() for p in p_tags]

wod = []

for p in p_content:
   if p == "Post time to comments.":
      break
   else:
      	wod.append(p)

filename = "wod_"+id+".txt"

file = open(filename, "w")

for i in wod:
   file.write("%s\n" % i)
 
file.close()
