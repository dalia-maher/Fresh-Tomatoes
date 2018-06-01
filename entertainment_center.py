import media
import fresh_tomatoes

# Creating Movie objects to be displayed on the page

toy_story = media.Movie("Toy Story",
                        "120 minutes",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=Ny_hRfvsmU8",
                        1995)

avatar = media.Movie("Avatar",
                     "115 minutes",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4",
                     2009)

school_of_rock = media.Movie("School of Rock",
                             "119 minutes",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=3PsUJFEBC74",
                             2003)

ratatouille = media.Movie("Ratatouille",
                          "125 minutes",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50"
                          "/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          2007)

midnight_in_paris = media.Movie("Midnight in Paris",
                                "100 minutes",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=dtiklALGz20",
                                2011)

the_hunger_games = media.Movie("The Hunger Games",
                               "130 minutes",
                               "A really real reality show",
                               "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=mfmrPu43DF8",
                               2012)

avengers = media.Movie("The Avengers",
                       "Earth's mightiest heroes must come together and learn"
                       "to fight as a team to save humanity.",
                       "143 minutes",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=a-7MWYqicC0",
                       2012)

divergent = media.Movie("Divergent",
                        "In a world divided by factions based on virtues,"
                        " Tris learns she's Divergent and won't fit in.",
                        "140 minutes",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=sutgWjz10sM",
                        2014)

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in "
                           "space in an attempt to ensure humanity's "
                           "survival.",
                           "169 minutes",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA",
                           2014)

# fill the movie objects created into an array (python data structure)
movies = [toy_story, avatar, school_of_rock, ratatouille,
          midnight_in_paris, the_hunger_games, avengers,
          divergent, interstellar]

# pass the array to the open_movies_page() method to render them
# on the website page.
fresh_tomatoes.open_movies_page(movies)
