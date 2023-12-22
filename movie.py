import requests
from bs4 import BeautifulSoup
import csv

def scrape_imdb(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = []

    for movie_div in soup.find_all('div', class_='lister-item-content'):
        title = movie_div.find('a').text
        year = movie_div.find('span', class_='lister-item-year').text.strip('()')
        director = movie_div.find('p', class_='text-muted').find_all('a')[0].text
        stars = [star.text for star in movie_div.find('p', class_='').find_all('a')[1:]]
        rating = movie_div.find('strong').text

        movie_data = {
            'Title': title,
            'Year': year,
            'Director': director,
            'Stars': ', '.join(stars),
            'Rating': rating
        }

        movies.append(movie_data)

    return movies

def save_to_csv(movies, filename):
    fieldnames = ['Title', 'Year', 'Director', 'Stars', 'Rating']

    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for movie in movies:
            writer.writerow(movie)

if __name__ == "__main__":
    target_url = 'https://www.imdb.com/chart/top'

    try:
        movies_data = scrape_imdb(target_url)
        save_to_csv(movies_data, 'movie_ratings.csv')
        print("Data scraped and saved successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")