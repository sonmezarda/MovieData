from movie import Movie
from selenium import webdriver
import time
import csv
from selenium.webdriver.common.by import By

def get_movie_data(driver,page_url):
    driver.get(page_url)
    movie_list = []

    for url_counter in range(101,6102,100):
        movies = driver.find_elements(By.XPATH, '//tbody/tr')
        for i in range(1, len(movies)):
            child_elements = movies[i].find_elements(By.XPATH, './/*')
            movie_id = int(child_elements[0].text.replace(',',''))
            try:
                year = int(child_elements[1].find_element(
                    By.TAG_NAME, 'a').text.split(', ')[1])
            except:
                year = 0
            url = child_elements[5].get_attribute('href')

            title = child_elements[3].text
            print(title)
            budget = int(child_elements[6].text[2:].replace(',', ''))
            gross = int(child_elements[8].text[2:].replace(',', ''))

            movie_list.append(Movie(movie_id, title, url, year, budget, gross))
        driver.get(page_url+f'/{url_counter}')
    
    return movie_list

def save_movie_data(movie_list, file_name="movie_data"):
    with open(file_name+".csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(movie_list[0].get_attributes().keys())
        for i in movie_list:
            try:
                csv_writer.writerow(i.get_attributes().values())
            except:
                pass


if __name__ == '__main__':
    page_url = 'https://www.the-numbers.com/movie/budgets/all'
    driver = webdriver.Firefox()
    movie_data = get_movie_data(driver, page_url)
    save_movie_data(movie_data,"movie_data")
    """
    m1 = Movie(1,"a","u1",2000,1,2)
    m2 = Movie(2,"b","u2",3000,3,4)
    movie_data = [m1,m2]
    save_movie_data(movie_data, 'deneme')
    """


