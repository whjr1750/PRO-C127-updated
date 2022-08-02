from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Edge("msedgedriver.exe")

# passing the path to the exe file
# 7,12 allows program to launch the chrome browser&launch the website

browser.get(starturl)
time.sleep(10)

def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    for i in range(1,423):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # "browser.page_source" finds the data & puts it in soup 
        # we use "html.parser" to tell the computer what the websit is coded in

        for ul_tag in soup.find_all("ul", attrs = {"class", "exoplanet"}):
            #print(ul_tag) / not written 7/31/22
            li_tags = ul_tag.find_all("li")

            # all 5 li tags in the ul tag will be put in the var "li_tags"

            temp_list = []
            for index,li_tag in enumerate(li_tags):

                # we want back both the index value & the value of the li tag
                # so we use enumerate

                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])

                    # find_all returns a list so when we want a value from
                    # that list we use square brackets and the index value
                    # .contents is also a list so we have to use square brackets & the index value  

                    # anchor = li_tag.find_all("a")

                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    
                    except:

                        # if that doesn't work, then /
                        # it would not work because if there is no value, how do we put nothing in our list?
                        # so we write:

                        temp_list.append("")
            planet_data.append(temp_list)
        # browser.find_element("xpath", '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click() #for chrome browser
        browser.find_element("xpath", value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("grape.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()

# calling the function
# planet_data = [[11 Comae Berenices b,304,19.4 Jupiters,4.72307,2007], [11 Ursae Minoris b,409,14.74 Jupiters,5.013,2009]]
# temp_list = [11 Comae Berenices b,304,19.4 Jupiters,4.72307,2007]

