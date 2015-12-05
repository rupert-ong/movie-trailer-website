import media
import fresh_tomatoes


# Create Movie instances for the webpage template.
old_boy = media.Movie("Oldboy",
                      ("After being kidnapped and imprisoned for 15 years, Oh "
                       "Dae-Su is released, only to find that he must find "
                       "his captor in 5 days."),
                      2003,
                      "R",
                      "https://upload.wikimedia.org/wikipedia/en/6/67/Oldboykoreanposter.jpg",
                      "https://www.youtube.com/watch?v=mNgyOueZIEo")

a_girl_walks = media.Movie("A Girl Walks Home Alone at Night",
                           ("In the Iranian ghost-town Bad City, a place that "
                            "reeks of death and loneliness, the townspeople "
                            "are unaware they are being stalked by a lonesome "
                            "vampire."),
                           2014,
                           "R",
                           "https://upload.wikimedia.org/wikipedia/en/1/18/AGWHAN_poster.jpg",
                           "https://www.youtube.com/watch?v=_YGmTdo3vuY")

five_venoms = media.Movie("5 Deadly Venoms",
                          ("A dying teacher instructs his final student to "
                           "check on the activities of five former pupils."),
                          1978,
                          "PG-13",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/1/1e/Fivedeadlyvenoms.jpg/220px-Fivedeadlyvenoms.jpg",
                          "https://www.youtube.com/watch?v=3aEl8kyCs-4")

black_dynamite = media.Movie("Black Dynamite",
                             ("Black Dynamite is the greatest African-American "
                              "action star of the 1970s. When his only brother "
                              "is killed by The Man it's up to him to find "
                              "justice."),
                             2009,
                             "R",
                             "https://upload.wikimedia.org/wikipedia/en/8/84/Black_dynamite_poster.jpg",
                             "https://www.youtube.com/watch?v=96Y24a0cyCE")

what_we_do_shadows = media.Movie("What We Do In The Shadows",
                                 ("Vampires who are finding that modern life "
                                  "has them struggling with the mundane."),
                                 2014,
                                 "R",
                                 "https://upload.wikimedia.org/wikipedia/en/7/70/What_We_Do_in_the_Shadows_poster.jpg",
                                 "https://www.youtube.com/watch?v=IAZEWtyhpes")

death_proof = media.Movie("Death Proof",
                          ("Two separate sets of voluptuous women are stalked "
                           "at different times by a scarred stuntman who uses "
                           "his 'death proof' cars to execute his murderous "
                           "plans."),
                          2007,
                          "R",
                          "https://upload.wikimedia.org/wikipedia/en/e/e1/Death_Proof_%28Netherlands%29.jpg",
                          "https://www.youtube.com/watch?v=sJas3Z7MAlY")

movies = [old_boy, a_girl_walks, five_venoms, black_dynamite, what_we_do_shadows, death_proof]

# Create page template
fresh_tomatoes.open_movies_page(movies)
