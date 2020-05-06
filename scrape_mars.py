from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import os
import warnings 
warnings.filterwarnings('ignore')

mars_data = {}

def chrome_driver();=:
    executable_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def mars_news_scraper():
    browser = chrome_driver()

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html

    soup = BeautifulSoup(html, 'lxml')

    list_text = soup.find('div', class_='list_text')

    news_title = list_text.find('div', class_='content_title').text

    news_p = soup.find('div', class_='article_teaser_body').text

    mars_data['News Title'] = news_title

    mars_data['News Paragraph'] = news_p

    return mars_data

    browser.quit()

def mars_image_scraper():
    browser = chrome_driver()

    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    html2 = browser.html

    soup = BeautifulSoup(html2, 'lxml')

    find_url = soup.find('div', class_ = 'carousel_items')

    url_ending  = find_url.find('article')['style'].replace('background-image: url(','')
    url_ending2 = url_ending.replace(');', '')[1:-1]

    
    url3 = "https://www.jpl.nasa.gov"

    featured_image_url = url3 + url_ending2

    featured_image_url

    mars_data['Featured URL'] = featured_image_url

    return mars_data

    browser.quit()

def mars_weather_scraper():

    browser2 = chrome_driver()

    executable_path = {'executable_path': 'chromedriver'}
    browser2 = Browser('chrome', **executable_path, headless=False)

    url4 = 'https://twitter.com/marswxreport?lang=en'
    browser2.visit(url4)

    html3 = browser2.html

    soup = BeautifulSoup(html3, 'lxml')

    weather_data = soup.find('div', class_='css-1dbjc4n').text

    weather_data2 = weather_data.replace('Log inSign upSee new TweetsFollowMars Weather@MarsWxReportUpdates as avail from the REMS weather instrument aboard @MarsCuriosity.  Data credit: Centro deAstrobiologia, FMI, JPL/NASA, Not an official acct.Gale Crater, Marsmars.nasa.gov/news/8415/insi…Joined August 201251 Following57.2K FollowersTweetsTweets & repliesMediaLikesTweetsTweets & repliesMediaLikesMars Weather’s TweetsMars Weather@MarsWxReport·16h', '')

    mars_weather= weather_data2.replace('412Mars Weather RetweetedSean Sublette@SeanSublette·May 4A little something from our @ClimateCentral office. #MayThe4thBeWithYou #ClimateChange0:23988 views1915Mars Weather@MarsWxReport·May 4InSight sol 510 (2020-05-03) low -93.0ºC (-135.5ºF) high -1.5ºC (29.2ºF)\nwinds from the WNW at 4.5 m/s (10.2 mph) gusting to 16.0 m/s (35.9 mph)\npressure at 6.80 hPa1715Mars Weather@MarsWxReport·May 4InSight sol 509 (2020-05-02) low -93.2ºC (-135.7ºF) high -2.2ºC (28.1ºF)\nwinds from the SW at 5.1 m/s (11.5 mph) gusting to 17.9 m/s (40.0 mph)\npressure at 6.80 hPa723Mars Weather@MarsWxReport·May 2On this day in 1982, the @weatherchannel  went on the air.1533', '')

    mars_data['Mars Weather'] = mars_weather

    return mars_data

    browser.quit()


def mars_facts_scraper():

    browser = chrome_driver()

    url15 = 'https://space-facts.com/mars/'

    browser.visit(url5)

    data = 'pd.read_html(url5)'

    df = data[0]

    df.rename(columns={'0': 'Parameter', '1': 'Value'}, inplace=True)

    table_html = df.to_html()

    table_html2 = table_html.replace('\n', '')

    mars_data['Mars Facts'] = table_html2

    return mars_data

    browser.quit()


def mars_hemispheres_scraper():

    browser3 = chrome_driver()

    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser3.visit(url5)

    hrml4 = browser3.html

    soup = BeautifulSoup(html4,'lxml')

    objects = soup.find_all('div', class_='item')

    img_url_ending = []
    url6 ='https://astrogeology.usgs.gov'

    for object in objects:
        img_url_ending = object.find('a', class_='itemLink product-item')['href']
        title=object.find('h3').text
        img_url = url6 + img_url_ending
        browser3.visit(img_url)
        html5 = browser3.html
        soup = BeautifulSoup(html5, 'lxml')
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

    mars_info['Hemisphere Image UTLs'] = hemisphere_image_urls

    return mars_data

    browser.quit()

    