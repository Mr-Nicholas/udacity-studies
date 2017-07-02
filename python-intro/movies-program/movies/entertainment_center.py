import media
import fresh_tomatoes

taxi_driver = media.Movie("Taxi Driver",
                          "A Vietnam veteran operates a Taxi in 1970's New York",
                          "https://images-na.ssl-images-amazon.com/images/I/51trIj-CsjL._SY450_.jpg",
                          "https://www.youtube.com/watch?v=sLpMx8_TYOo")

godfather = media.Movie("The Godfather",
                        "The saga of a Sicilian crime family in New York City",
                        "https://movietalkexpress.files.wordpress.com/2015/12/the-godfather.jpeg",
                        "https://www.youtube.com/watch?v=w0VGcWHkNeA")

mean_streets = media.Movie("Mean Streets",
                           "A small time crook finds himself in debt to a loanshark",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMWNmNGY3ZGMtYWQ3OC00Zjg4LWFiN2EtZjM2MDI1YzRiNjg3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY1200_CR87,0,630,1200_AL_.jpg",
                           "https://www.youtube.com/watch?v=GAQZzfwQGHQ")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "A man meets his past in Long Island",
                               "http://www.impawards.com/2004/posters/eternal_sunshine_of_the_spotless_mind_ver4.jpg",
                               "https://www.youtube.com/watch?v=yE-f1alkq9I")

new_jack_city = media.Movie("New Jack City",
                            "The ascension of a drug lord in 1980's New York",
                            "http://atlantablackstar.com/wp-content/uploads/2017/04/11171606_800.jpg",
                            "https://www.youtube.com/watch?v=pumf6m7d14w")

gangs_of_new_york = media.Movie("Gangs of New York",
                                "The bloody battle for New York's identity",
                                "https://images-na.ssl-images-amazon.com/images/I/51bTWMS2nNL._SY355_.jpg",
                                "https://www.youtube.com/watch?v=qHVUPri5tjA")

# save all the below movies into an array
movies = [taxi_driver, godfather, mean_streets, eternal_sunshine, new_jack_city, gangs_of_new_york]
# fresh_tomatoes.open_movies_page(movies)

print(media.Movie.MOVIE_RATINGS)
