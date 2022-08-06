from movie import Movie
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def get_movie_data(page_url):
    driver.get(page_url)
    movie_list = []

    for url_counter in range(101,6202,100):
        movies = driver.find_elements(By.XPATH, '//tbody/tr')
        for i in range(1, len(movies)):
            child_elements = movies[i].find_elements(By.XPATH, './/*')
            movie_id = int(child_elements[0].text)
            try:
                year = int(child_elements[1].find_element(
                    By.TAG_NAME, 'a').text.split(', ')[1])
            except:
                year = 0
            # print(child_elements[2])
            url = child_elements[5].get_attribute('href')

            title = child_elements[3].text
            print(title)
            budget = int(child_elements[6].text[2:].replace(',', ''))
            gross = int(child_elements[8].text[2:].replace(',', ''))

            movie_list.append(Movie(movie_id, title, url, year, budget, gross))
        driver.get(page_url+f'/{url_counter}')
    
    return movie_list

def save_movie_data(movie_list):
    pass

if __name__ == 'main':
    page_url = 'https://www.the-numbers.com/movie/budgets/all'
    driver = webdriver.Firefox()
    movie_data = get_movie_data(page_url)


