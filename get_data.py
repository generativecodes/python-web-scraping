from bs4 import BeautifulSoup
# import re

with open(f"website.html","rb") as f:
    soup = BeautifulSoup(f.read(), "html.parser")
    
# only an example:
main_part = soup.find('div', class_='post-content')
stuff = main_part.find_all('tr')
