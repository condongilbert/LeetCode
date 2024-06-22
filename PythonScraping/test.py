from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
print(page)