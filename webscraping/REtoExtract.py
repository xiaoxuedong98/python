#Extract Text From HTML With Regular Expressions
import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
print(html)

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title1 = match_results.group()
print(title1)

title = re.sub("<.*?>", "", title1) #remove html tags

print(title)


#Excercise: Scrape Data From a Website
import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
print(html)

pattern2 = "<h2.*?>.*?</h2.*?>"
match_results2 = re.search(pattern2, html, re.IGNORECASE)
h2 = match_results2.group()
h2 = re.sub("<.*?>", "", h2)
print(h2[6:])

pattern3 = "Favorite.*?</center.*?>"
match_results3 = re.search(pattern3, html, re.IGNORECASE)
br = match_results3.group()
br = re.sub("<.*?>", "", br)
print(br[1:])

for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)