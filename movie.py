class Movie:
    id = 0
    title = "movieTitle"
    url = "url"
    year = 0
    budget = 0
    gross = 0

    def __init__(self, id, title, url, year, budget, gross):
        self.id = id
        self.title = title
        self.url = url
        self.year = year
        self.budget = budget
        self.gross = gross

    def get_attributes(self):
        movie_dict = {'id': self.id,
                      'title': self.title,
                      'url': self.url,
                      'year': self.year,
                      'budget': self.budget,
                      'gross': self.gross}
        return movie_dict
    
    def print_attributes(self):
        movie_dict = self.get_attributes()
        for i in movie_dict:
            print(f'{i} : {movie_dict[i]}')
