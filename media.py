import webbrowser

class Video():

    """ This class provides a way to store a video related information

	Args:
	    title: The title of the videp.
	    duration: The duration of the video in minutes.
    """

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        
class Movie(Video):

    """ This class provides a way to store movie related information

	Args:
	    title: The title of the movie.
	    duration: The duration of the movie in minutes.
	    storyline: The description of the movie in one line.
	    poster: Movie box art (poster).
	    trailer: URL of the youtube trailer.
	    release_year: The release year of the movie
    """
    
    # movie ratings to be used and stored for future work
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, duration, storyline, poster, trailer, release_year):
        Video.__init__(self, title, duration)
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer
        self.release_year = release_year

    # opens the trailer of a movie object in the web browser
    def show_trailer(self):
        webbrowser.open(self.trailer)

		
# TV Show class to be used in future work
class TvShow(Video):

    """ This class provides a way to store tv show related information """
        
    def __init__(self, title, duration, season, episode, tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        print("title = " + title
              + "duration = " + duration
              + "season = " + season
              + "episode = " + episode
              + "tv_station = " + tv_station)
