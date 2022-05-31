import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page  = requests.get(START_URL)
soup = bs(page.text, "html.parser")

star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')

    row = [i.text.rstrip() for i in td]
    
    temp_list.append(row)

name = []
distance = []
mass = []
radius = []

for i in range(1, len(temp_list)):
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns = ['Dwarf_name', 'Distance', 'Mass', 'Radius'])

print(df)
df.to_csv('brown_dwarfs.csv')