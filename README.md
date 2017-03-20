# About happy-logs
Learning Logs takes its name (and most of its structure and functionality) from the Python/Django web application tutorial found in Chapters 18 - 20 in the beginner's python programming book [_Python Crash Course_](https://ehmatthes.github.io/pcc/index.html) by Eric Matthes. Users track what they've learned in entries that are grouped by a user-defined topic.

Some modifications have been made to the original design at the request of potential users (me, my son, and the hubs):

- used bootstrap3's [ fixed-top navbar ](https://getbootstrap.com/components/#navbar-fixed-top) instead of a static-top navbar
- added some more bootstrap3 [ buttons ](http://getbootstrap.com/css/#buttons)
- added an "about" page with [ panels ](http://getbootstrap.com/components/#panels)
- sorted user's topics alphabetically instead of by date added: required learning more about [ Django's QuerySet API ](https://docs.djangoproject.com/en/1.10/ref/models/querysets/) and the [ ordered_by method ](https://docs.djangoproject.com/en/1.10/ref/models/querysets/#order-by)
- added the image of a happy log on the index page: original image found on March 11, 2016 on kingofwallpapers.com via a google search for images of logs; modified by me using Adobe Photoshop CS5.
- added timezone aware dates for entry views rendered client-side on the "topic" page: required some javascript code (suggested by the hubs) and installation of [ moment.js ](https://momentjs.com/) (an amazing little package that I found which provides formatting options for javascript date objects! ... required downloading and using moment.min.js as a [ static file ](https://docs.djangoproject.com/en/1.10/howto/static-files/))
- used a [ markdown ](https://daringfireball.net/projects/markdown/syntax) editor/viewer for the "new entry", "edit entry", and "topic" pages: required installation of the projects [ django-pagedown ](https://github.com/timmyomahony/django-pagedown) (for the markdown editing) and [ django-markdown-deux ](https://github.com/trentm/django-markdown-deux) (for viewing markdown entries ... and for safely escaping raw HTML)

# Project Website
[https://happy-logs.herokuapp.com/](https://happy-logs.herokuapp.com/)
