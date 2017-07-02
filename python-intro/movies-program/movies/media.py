import webbrowser

class Movie():
    """ The Movie Class creates a movie instance parsing four variables, 'movie_title', 'storyline', poster_image' and 'trailer_youtube' """

    MOVIE_RATINGS = ["G", "PG", "M", "MA15+", "R"]

    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


    # display information
