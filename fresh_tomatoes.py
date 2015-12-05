import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Movie Trailer Website</title>

    <!-- Google Fonts -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:400,700" />

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" />
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 400;
            background-color: #373b3e;
        }
        b, strong, h1, h2, h3, h4, h5, h6 {
            font-weight: 700;
        }
        h1, h2, h3, h4, h5, h6, .text-uppercase {
            text-transform: uppercase;
        }
        .navbar {
            background-color: #fff;
        }
            .navbar, .navbar a {
                color: #373b3e
            }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
            .scale-media iframe {
                border: none;
                height: 100%;
                position: absolute;
                width: 100%;
                left: 0;
                top: 0;
                background-color: white;
            }

        /* Custom Styles */
        .movie-card-container {
            padding: 0;
        }
        .movie-ready .movie-card-container:hover .movie-column {
            -webkit-transform: scale(0.9) translateZ(0);
            -ms-transform: scale(0.9) translateZ(0);
            transform: scale(0.9) translateZ(0);
            opacity: 0.4;
        }

        .movie-ready .movie-card-container:hover .movie-column:hover {
            -webkit-transform: scale(1) translateZ(0);
            -ms-transform: scale(1) translateZ(0);
            transform: scale(1) translateZ(0);
            opacity: 1;
        }

        .movie-column {
            padding: 0;
        }

            .movie-ready .movie-column {
                -webkit-transition: all 0.2s ease-out;
                transition: all 0.2s ease-out;
                -webkit-transform: translateZ(0);
                -ms-transform: translateZ(0);
                transform: translateZ(0);
            }

        .movie-card {
            margin: 0 auto 30px;
            max-width: 220px;
            border-radius: 5px;
        }
            .movie-card .movie-card-poster {
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
            }
            .movie-card .movie-card-meta {
                background-color: #fff;
                border-bottom-left-radius: 5px;
                border-bottom-right-radius: 5px;
                padding: 20px 0;
            }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });

        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.btn-show-trailer-modal', function (event) {
            var $this = $(this),
                $parentCard = $this.closest('.movie-card'),
                trailerYouTubeId = $parentCard.attr('data-trailer-youtube-id')
                sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        // Populate Info Modal
        $(document).on('click', '.btn-show-info-modal', function (event) {
            var $this = $(this),
                $parentCard = $this.closest('.movie-card'),
                movieTitle = $parentCard.attr('data-movie-title'),
                movieStoryline = $parentCard.attr('data-movie-storyline'),
                movieYear = $parentCard.attr('data-movie-year'),
                movieRating = $parentCard.attr('data-movie-rating');

            $("#info-modal-title").html(movieTitle);
            $("#info-modal-storyline").html(movieStoryline);
            $("#info-modal-year").html(movieYear);
            $("#info-modal-rating").html(movieRating);
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-column').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
            if($(this).next("div").length < 1) {
                $('body').addClass('movie-ready');
            }
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal fade" id="movie-trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Info Modal -->
    <div class="modal fade" id="movie-info">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h3 id="info-modal-title" class="modal-title">Movie Title</h3>
          </div>
          <div class="modal-body">
            <dl>
                <dt>Storyline</dt><dd id="info-modal-storyline">Storyline</dd>
                <hr>
                <dt>Year Released</dt><dd id="info-modal-year">Year</dd>
                <hr>
                <dt>Rating</dt><dd id="info-modal-rating">Rating</dd>
            </dl>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#"><small class="text-uppercase">Movie Trailer Website</small></a>
          </div>
        </div>
      </div>
    </div>
    <div class="container movie-card-container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_column_content = '''
<div class="col-md-6 col-lg-4 movie-column">
    <div class="movie-card text-center" data-movie-title="{movie_title}" data-movie-storyline="{movie_storyline}" data-movie-year="{movie_year}" data-movie-rating="{movie_rating}" data-trailer-youtube-id="{trailer_youtube_id}">
        <img class="movie-card-poster" src="{poster_image_url}" width="220" height="342">
        <div class="movie-card-meta">
            <button type="button" class="btn btn-default btn-sm btn-show-info-modal" data-toggle="modal" data-target="#movie-info">Show Info</button>
            <button type="button" class="btn btn-primary btn-sm btn-show-trailer-modal" data-toggle="modal" data-target="#movie-trailer">Play Trailer</button>
        </div>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_column_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_year=str(movie.year),
            movie_rating=movie.rating,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
