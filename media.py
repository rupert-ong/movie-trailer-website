class Movie():
    """Movie object for trailer website.

    Creates an object to hold the data for each movie tile in the webpage.

    Attributes:
        title: A string for the movie's title
        storyline: A string for the movie's plot
        year: An integer for the movie's year of release
        rating: A string for the movie's rating. Must be in VALID_RATINGS
            constant
        poster_image_url: A string for the image URL for movie's poster
        trailer_youtube_url: A string for the YouTube URL for movie's trailer
    """

    VALID_RATINGS = ["G", "PG-13", "AA", "R", "No rating"]

    def __init__(self, movie_title, movie_storyline, movie_year, movie_rating,
                 poster_image_url, trailer_youtube_url):
        """Inits Movie with aforementioned attributes."""
        self.title = movie_title
        self.storyline = movie_storyline
        if(isinstance(movie_year, int) and movie_year >= 0):
            self.year = movie_year
        else:
            self.year = "Unknown"
        if(movie_rating in Movie.VALID_RATINGS):
            self.rating = movie_rating
        else:
            self.rating = "No rating"
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
