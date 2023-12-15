from bs4 import BeautifulSoup
import time
import pandas as pd 

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

stars_data = []

def scrape():

    for i in range(0, 10):
        print(f'Scrapping page{i+1} ...' )

        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs = {"class", "stars"}):
            li_tags = ul_tag.find_all("li")
            empty_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    empty_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        empty_list.append(li_tag.contents[0])
                    except:
                        empty_list.append("")
            stars_data.append(empty_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

        with open("scraper_2.csv", "w") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(stars_data)

            scrape()

            headers = ["name", "distance", "mass", "radius"]
