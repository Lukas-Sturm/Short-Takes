# Short Takes

Django Application.  
Simple Twitter clone with the ability to post private "Takes".  
Private Takes are visible only to the Author's friends and the Author of the original Take if the Take is a reply.

# Install
Create a venv `python -m venv my_venv`  
Activate the venv > depends on system architecture  
Install dependencies (__requirements.txt__) `pip install -r requirements.txt`  
Check `short_takes/app.py` for Database connection and change accordingly  

For initial install a migration needs to be run `python manage.py migrate`  
Then start the application `python manage.py runserver`  

## Architecture
### Django
> Note: This is my first ever Django Application. This project was a submission for a course

I tried to build it as idiomatic as possible.   
Everything is packed into modules.

### HTMX
This Application is a Hypermedia Driven Application. All views are served either in the context of a Full Page, or if HTMX is enabled as a partial render.   
Full Page rendering required some passing of URL parameters in order to retain page state for pages containing multiple paginated feeds with different pagination states (lists of Takes).
