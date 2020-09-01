#.:DataProfunda:. 
#Downloads table from Worldometers.info and makes csv file from it

#From Page To Csv (FPTC)
from urllib.request import urlopen as uReq       
from urllib.request import Request        
from bs4 import BeautifulSoup as soup 
import numpy as np
import pandas as pd
import ftplib

print("Connecting...")

page_url = 'https://www.worldometers.info/coronavirus/'

req = Request(page_url, headers = {"User-Agent": "Mozilla/5.0"})

uClient = uReq(req)
page_html = uClient.read()
uClient.close() 

page_soup = soup(page_html, "html.parser")


print("Analyzing...")
#Finds table 
#container[0] is new, container[1] is old
container = page_soup.findAll("div",{"class":"main_table_countries_div"}) 

new_table = container[0]

#Find columns names
columns_names = new_table.findChildren(['th'])
for i, name in enumerate(columns_names):
    columns_names[i] = name.get_text()


#Extract raw table
raw_table = new_table.findChildren(['th', 'tr'])


table_done = pd.DataFrame([np.arange(len(columns_names))],np.arange(len(raw_table)))
table_done[:] = np.nan

#Finds country names
for n_row, row in enumerate(raw_table):
    
    cells = row.findChildren('td')
    
    for n_cell,cell in enumerate(cells):
        if((columns_names[n_cell] == 'Population') and (cell.find('a') != None)):
            value = cell.find('a').string    
            table_done.iloc[n_row, n_cell] = value    
        else:          
            value = cell.string
            table_done.iloc[n_row, n_cell] = value
    

table_done = table_done.dropna(how='all').copy()
table_done.columns = columns_names

table_done = table_done.reset_index(drop=True)

#Makes LatIng table

wanted_columns = ['CountryName','TotalCases','NewCases','TotalDeaths','NewDeaths','ActiveCases','Population']

table_concap = pd.read_csv('concap.csv')

#Table_ext will be final csv file.
table_ext = table_done.copy()
table_ext.columns.values[1] = "CountryName"
table_ext = table_ext.dropna(how='all')

table_ext = table_ext.loc[:,wanted_columns]

#Preprocessing data
table_ext = table_ext.loc[table_ext["CountryName"].isna() == False, :] 
table_ext = table_ext.loc[table_ext["CountryName"] != 'World', :] 
table_ext = table_ext.loc[table_ext["CountryName"] != 'Total:', :] 

table_ext = table_ext.reset_index(drop=True)


table_ext.loc[:,"CapitalLatitude"] = np.arange(len(table_ext))
table_ext.loc[:,"CapitalLongitude"] = np.arange(len(table_ext))

#Fill country's data with CapitalLatitude and CapitalLongitude
for x, value in enumerate(table_ext.iloc[:,0]):
    for i, value_i in enumerate(table_concap.iloc[:,0]):
        if(value == value_i):
            table_ext.loc[x,"CapitalLatitude"] = table_concap.loc[i,"CapitalLatitude"]
            table_ext.loc[x,"CapitalLongitude"] = table_concap.loc[i,"CapitalLongitude"]

table_ext.to_csv("concap_ct.csv", index=False)


filename = "concap_ct.csv"
ftp = ftplib.FTP("ftp-adress")
ftp.login("user","password")

ftp.cwd("www")

myfile = open(filename, 'rb')


ftp.storlines('STOR ' + filename, myfile)

ftp.quit()

print("Success!")