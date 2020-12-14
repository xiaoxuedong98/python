from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
page

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

#Once you have the HTML as text, you can extract information from it in a couple of different ways.

#Extract Text from HTML with String Methods
title_index = html.find("<title>")
print(title_index)
start_index = title_index + len("<title>")
print(start_index)
end_index = html.find("</title>")
end_index
title = html[start_index:end_index]
print(title)

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
#print(html)
title_index = html.find("<title >")
print(title_index)
start_index = title_index + len("<title >")
print(start_index)
end_index = html.find("</title>")
print(end_index)
title = html[start_index:end_index]
print(title)

# A primer on regular expressions
import re
a = re.findall("ab*c", "ac")
print(a)
b = re.findall("ab*c", "abcd")
print(b)
c = re.findall("ab*c","abcac")
print(c)
d = re.findall("ab*c","abdc")
print(d)
# If you want to match this pattern regardless of the case, then you can pass a third argument with the value re.IGNORECASE
re.findall("ab*c","ABC")
x = re.findall("ab*c","ABC",re.IGNORECASE)
print(x)

# Use period(.)to stand for any SINGLE character in a regular expression
a = re.findall("a.c", "abc")
print(a) #['abc']
b = re.findall("a.c", "abbd")
print(b)#[]
c = re.findall("a.c","ac")
print(c)#[]
d = re.findall("a.c","acc")
print(d)#['acc']

#re.search() could search for a particular pattern inside a string, it returns every possible result
match_results = re.search("ab*c","ABC",re.IGNORECASE)
match_results.group() #‘ABC’

#re.sub(), replace text in a string that matches a regular expression with new text
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "Elephants", string)
print(string)  #Everything is Elephants.
#"<.*>": everything between the first < and last >

string = string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
print(string) #"Everything is ELEPHANTS if it's in ELEPHANTS."
#*?: it matches the shortest possible string of text



 