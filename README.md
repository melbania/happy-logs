# happy-logs
A Python/Django application based on the web app project tutorial (Ch. 18-20) in _Python Crash Course_ by Eric Matthes.

# Install
- [Clone or download](https://help.github.com/articles/cloning-a-repository/) the happy-logs repository.
- Run secretkey_gen.py:

    ```
    $ python secretkey_gen.py  
    ```
    
- Copy and paste secret key to local environment storage file (e.g., .bash_profile on OSX or ??? on Linux or ??? on Windows).
- Create a virtual environment inside the happy-logs directory.
    
    ```
    $ python -m venv *<virtual environment name>*
    ```
    
- Activate the virtual environment.
    
    ```
    $ source *<virtual environment name>*/bin/activate
    ```
    
- Install the following packages in the active virtual environment:
    * Django
    * django-bootstrap3
    * django-markdown-deux
    * django-pagedown
    * dj-database-url
    * dj-static
    * gunicorn
    
- Create the database.
    
    ```
    $ python manage.py migrate
    ```
    
- Collect static files.

    ```
    $ python manage.py collectstatic
    ```
    
- `runserver` to view the project in a web browser.
    
    ```
    $ python manage.py runserver
    ```
    
- View the project in a web browser.
    * open the web browser of your choice (e.g., Safari, Chrome, Firefox, etc.)
    * Type `localhost:8000` into the address bar
