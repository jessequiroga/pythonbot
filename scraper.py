from selenium import webdriver
import random



class Scraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)

    def get_articles(self, url="http://www.dev.to"):
        self.driver.get(url)
        els = self.driver.find_elements_by_class_name("single-article")
        articles = []
        random.shuffle(els)

        for el in els[0:5]:
            if el.find_element_by_tag_name("h3") and el.find_elements_by_class_name("index-article-link"):
                articles.append(
                    {
                        "title": el.find_element_by_tag_name("h3").text,
                        "link": el.find_element_by_class_name("index-article-link").get_attribute("href")
                    }
                )
            else:
                pass

        return articles

