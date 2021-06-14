from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


def news():
    news_url = "https://redplanetscience.com/"
    browser.visit(news_url)
    html = browser.html
    soup = bs(html, "html.parser")
    news_title = soup.find("div", id="news")
    news_title_only = news_title.find("div", class_ = "content_title").text
    news_para = news_title.find("div", class_ = "article_teaser_body").text
    news_data = [news_title_only,news_para]
    return news_data

def mars_images():
    img_url = "https://spaceimages-mars.com/"
    browser.visit(img_url)
    img_html = browser.html
    soup = bs(img_html, "html.parser")
    img = soup.find("div", class_ ="header")
    img_src = img.find("img", class_ = "headerimage")["src"]
    featured_image_url = img_url + img_src
    return featured_image_url

def facts():
    facts_url = "https://galaxyfacts-mars.com/"
    browser.visit(facts_url)
    html = browser.html
    soup = bs(html, "html.parser")
    mars_facts = pd.read_html(facts_url)
    mars_facts= pd.DataFrame(mars_facts[0])
    mars_data = mars_facts.to_html()
    return mars_data

def hemispheres():
    hemis_url = "https://marshemispheres.com/"
    browser.visit(hemis_url)
    html = browser.html
    soup = bs(html, "html.parser")
    hemi  = soup.find_all("div", class_ = "item")
    hemispheres = []

    for hemisphere in hemi:
        title = hemisphere.find("h3").text
        link_html = hemisphere.find("a")["href"]
        img_url = hemis_url+link_html
        browser.visit(img_url)
        html = browser.html
        soup = bs(html, "html.parser")
        full_img = soup.find("div", class_ = "downloads")
        fullimg_link = full_img.find("a")["href"]
        hemispheres.append({'title':title, "img_url":hemis_url+fullimg_link})
    return hemispheres

    
def scrape():
    all_data = {}
    news_data = news()
    all_data["news"] = news_data[0]
    all_data["news_para"] = news_data[1]
    all_data["images"] = mars_images()
    all_data["facts"] = facts()
    all_data["hemispheres"] = hemispheres()

    browser.quit()

    return all_data

