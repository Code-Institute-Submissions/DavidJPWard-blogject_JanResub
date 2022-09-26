# Blogject

logject is a blog/news website where users can create and share posts with other users.

the objective of the site is to promote positive engagement between like minded people. the site has a strogn social element where users can like and comment on other users posts and subscribe to users who consistently make good content. each user has there own profile that they can edit to make their own. including a user bio, user profile picture and other social media handles 

you can visit the website here.


## project goals

a responsive design that allows for easy navigation on a vareity of screen sizes

a place where users can post their thoughts and ideas in a blog format

account authorisations to allow engagement between users aswell as a a page where other users can see all your posts.

a simple yet pleasant colour scheme as to promote a fun and relaxed atmosphere

-user goals

as a site admin, i need to manage the content of my site.

as a site user, i want to be able to veiw posts.

as a site user, i want to be able to create posts.

as a site user, i want to be able to edit and delete my existing posts.

as a site user i want to be able to like and comment on posts

as a site user i want to have my own profile

as a site user i want to be able to subscirbe to other users.


-structure

the website revoles around the home page. through here you can navigate to most pages from the site. the navigation bar is consistent throughout the site. both forms and links give clear feedback tot he user through messages. the opportunity to create posts and veiw your profile is available once the user has logged in.


-database model
colour scheme



## Features

### General

responsive design accross all devices.

navigation bar can contains the company logo and links to other pages. the links turn into a hamburger menu when the screen size decreases. 


### home page

the home page displays a paginated list of all articles sorted from newest first. 

the articles are displayed through cards that show all the relevent infomation about the article.

### post detail page

the post detail page shows the main content of the article. the title, author, featured image and post date are at the top in the masthead and followed by the main content. 

users are able to like the post and to subscribe to the author of the post the info box just under the content.

users are able to leave comments ad have them listed with other comments.

### profile page

users can view their and other users profiles

users can gain subscribers if they consistenly post well

users have a user bio section that offers a breif description of that user, they can also upload a profile picture.

from here users can edit thier posts and delete their posts

users can veiw all their posts in a paginated list aswell as the posts from user they are subscribed to.

users can offer media links to their other social media accounts.

### new post page

users can create new posts from here

easily found in the navbar at the top if that user has been authenticated

### edit post page

users can edit their posts from this page

### edit profile page

users can edit their profile from this page

### user authentication pages

using allauth i have implemented user authentication

users can register, log in and log out

## Technologies used

### languages used

- Python
- HTML5
- CSS3
- JavaScript

## Libraries and Frameworks

- Django - a web framework that is the back bone fo the site

- Bootstrap 5 - a front end framework that was used for the styling of most of the site. 

- Google Fonts - google offers a wide range of free fonts. 

- Font Awesome - Font Awesome icons were used throughout the site to make it more visually appealing

## Packages / Dependecies Installed

- Cloudinary - Cloudinary was used to store images online as apposed to statically

- Django Allauth - Django Allauth has been used to handle user authentication

- Django Crispy Form - Django Crispy Form has helped with the rendering froms

- Gunicorn - Gunicorn has been used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.

- Summernote - Summernote was implemented as a WYSIWYG editor.

## software and tools

- Gitpod - he application was written in gitpod, which also helped with pushing and commiting to github

- heroku - the website used to deploy the application

- Youtube - many features ive implemented were taught to me through youtube tutorials

- stack overflow - most bugs and errors were resolved by looking them up through stack overflow

## future features

- plans to introduce social accounts to make authenication easier

- plans to filter posts on the home page by user or category aswell as increase the pagination limit.

## Deployment

This project was developed using a GitPod workspace. The code was commited to Git and pushed to GitHub using the terminal.
Deploying on Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

    Create the Heroku App:
        Select "Create new app" in Heroku.
        Choose a name for your app and select the location.

    Attach the Postgres database:
        In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

    Prepare the environment and settings.py file:
        In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
        In your GitPod workspace, create an env.py file in the main directory.
        Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
        Add the SECRET_KEY value to the Config Vars in Heroku.
        Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
        Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
        In settings.py add the following sections:
            Cloudinary to the INSTALLED_APPS list
            STATICFILE_STORAGE
            STATICFILES_DIRS
            STATIC_ROOT
            MEDIA_URL
            DEFAULT_FILE_STORAGE
            TEMPLATES_DIR
            Update DIRS in TEMPLATES with TEMPLATES_DIR
            Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

    Store Static and Media files in Cloudinary and Deploy to Heroku:
        Create three directories in the main directory; media, storage and templates.
        Create a file named "Procfile" in the main directory and add the following:
            web: gunicorn project-name.wsgi
        Go to Deploy tab on Heroku and connect to the GitHub, then to the required recpository. Click on Delpoy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.

Forking the Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

    Log into GitHub or create an account.
    Locate the GitHub Repository.
    At the top of the repository, on the right side of the page, select "Fork"
    You should now have a copy of the original repository in your GitHub account.

Creating a Clone

How to run this project locally:

    Install the GitPod Browser Extension for Chrome.
    After installation, restart the browser.
    Log into GitHub or create an account.
    Locate the GitHub Repository.
    Click the green "GitPod" button in the top right corner of the repository. This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

How to run this project within a local IDE, such as VSCode:

    Log into GitHub or create an account.
    Locate the GitHub Repository.
    Under the repository name, click "Clone or download".
    In the Clone with HTTPs section, copy the clone URL for the repository.
    In your local IDE open the terminal.
    Change the current working directory to the location where you want the cloned directory to be made.
    Type 'git clone', and then paste the URL you copied in Step 3.

git clone https://github.com/josswe26/code-buddy

    Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub here


## Acknowledgements

### Content

most of the website was written by the developer 

help from the code institute tutorial was used including: 

- setting up the project
- Message implementation an dismissal code 

help from youtube tutorials and google

### known bugs
creating a post with the same name will generate a duplicate slug which will lead to an error. a fix would be to validate the title to make it unique or change how slugs are generated.


many thanks to my mentor marcel, for his guidance throughout this project as well as the code institute tutor team.
