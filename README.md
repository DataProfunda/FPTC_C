# FPTC - from page to csv file.
 Scrape statistical data about pandemic in each country.   
 Add CapitalLatitude and CapitalLongitude for later display on a map.
 Used page: worldometers.info/coronavirus/.
 Web scrape with BeautifulSoup. 


# 1. Downloads coronavirus table from Worldometers.info.
Some pages have protection from scrapping so we add header "{"User-Agent": "Mozilla/5.0"}"
![f1](https://user-images.githubusercontent.com/69935274/101418066-4b7fbf80-38ed-11eb-8bff-3b5b1b00d2ec.png)
  
# 2. Clean raw table.
We use function findAll() to find tables.
Container[0] is new table, container[1] is old.
![fa2](https://user-images.githubusercontent.com/69935274/101418080-53d7fa80-38ed-11eb-8dd2-442e6542506c.png)

Function findChildren is used to find columns names
![fb2](https://user-images.githubusercontent.com/69935274/101418091-5c303580-38ed-11eb-8853-065be7be7c66.png)

Extract raw table
![fc2](https://user-images.githubusercontent.com/69935274/101418101-62261680-38ed-11eb-8a69-31a2f524f9d7.png)

Find country names
![fd2](https://user-images.githubusercontent.com/69935274/101418118-6b16e800-38ed-11eb-9fda-a89ae783a0f9.png)

# 3. Drop unwanted columns.
Table_ext will be final csv file.
![f3](https://user-images.githubusercontent.com/69935274/101418139-7538e680-38ed-11eb-9781-43a3ba46df5f.png)

# 4. Drop rows with Nan values.
Preprocessing data
![f4](https://user-images.githubusercontent.com/69935274/101418155-7c5ff480-38ed-11eb-9e39-3f724872ce5d.png)

# 5. Add CapitalLatitude and  CapitalLongitude do the table.
Fill country's data with CapitalLatitude and CapitalLongitude for further placing on the map.
![f5](https://user-images.githubusercontent.com/69935274/101418166-81bd3f00-38ed-11eb-8cdf-697ec4853f6a.png)

# 6a. Save table to csv file
# 6b.Send csv file to ftp server.
![f6](https://user-images.githubusercontent.com/69935274/101418176-871a8980-38ed-11eb-95ae-3036e01dcd79.png)


