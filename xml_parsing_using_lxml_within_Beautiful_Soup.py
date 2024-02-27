from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()    #you must indent!!
    print(contents)

#BeautifulSoup is the class

#then, we create an object from that Class, pass in the contents, and then the parser)
soup = BeautifulSoup(contents, "lxml")   # or use HTML, if this doesn't work

print(soup)

print(f"The title tag (soup.title) is: {soup.title}")
print(f"The name of that particular title tag (title.name) is: {soup.title.name}")
print(f"The string that is contained inside the title tag (title.string) is: {soup.title.string}\n")

print(f"The soup.heading (Heading) is: {soup.heading}")
print(f"The soup.h3 (Heading - level 3) is: {soup.h3}")
print(f"The soup.class (Class) is {soup.__class__}")

print(soup.prettify())

# to find the first anchor tag in the website, use:
print(soup.a)

# the first list item (li):
print(soup.li)

#the first paragraph:
print(soup.p)