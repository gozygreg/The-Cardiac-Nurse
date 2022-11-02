# THE CARDIAC NURSE
The Cardiac Nurse website is go-to platform for every nurse that specialise in anything that has to do with the cardiovascular system. It is an educational medium that all nurses can learn from, particularly those with keen intrest in cardiology.

# Table of Contents
- [UX](#ux)
- [User Stories](#user)
- [Design](#design)
- [Features](#features)
- [Testing](#testing)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Credits](#credits)

## Ux
### Site Aim
The purpose of the cardiac nurse website is to bring together nurses with intrest in all areas of cardiology care. Its aim is to provide educational support through extensive and research oriented blog post.
### Site Goals
- create a medium where nurses can be inspired, enlightened and informed about new developments in heart health.
- create a platfrom where cardiac nurses can be found and can also find collegues.
### User Goals
- User/nurse is able to join platform, create a profile and update their professional experience/journey as a cardiac nurse
- User/nurse is able to access blogpost and stay up-to-date with treatment guildelines in various aspect of cardiology
### Site visitors' Goals
- Site visitors are able to see the profile and professional experience/journey of nurses who registered
- Site visitors are able to read the various blog posts on the site.

## User Stories
### Admin stories
As the site administrator (For Nurse Blog app):
- I can create, read, update and delete post so that I can manage the contents and flow of the site
- I can create draft posts so that I can finish writing the content later
- I can approve or disapprove comments so that prevent sharing inappropriate/offensive comments

As the site administrator (For Nurse Profile app):
- I can verify and accept new nurses that what to join the platform so that they can be viewed by site visitors
- I can add a new nurse profile, update or delete an existing nurse profile so that i can manage the content and flow of nurses in the site 
### Nurse stories
As a nurse registered on the platform:
- I can upload my profile picture so that other site users can see what I look like
- I can create a user profile and write about my career journey as a cardiac nurse so that I can be found and viewed on the site
### Site visitors' stories
As a visitor of the site:
- I can view any nurse profile so that see their career journey
- I can signup for an account so that I can like and comment on posts as well as create a profile if I am a cardiac nurse
- I can view a list of post so that I can select one to read
- I can click to open a post so that read the content of the post
- 1 can view a paginated list of post so that I can select a post to view
- I can be able to like or unlike post so that I can interact with the content
- I can view the number of likes on individual post so that know the most popular post
- I can be able to comment on post so that I can be able to leave feedback and engage further
- I can view comments on each post so that know the most engaging post

## Design

## Features

## Testing

## Technologies
### Programming Languages
- HTML
- CSS
- JavaScript
- Python
- SQL
- Postgres
### Frameworks and Libraries
- Django
- Bootstap
- Gitpod
- Github
- Google Fonts
- Font Awesome
- Balsamqid
- Am I Resposive
- Adobe stock images
- Image resizer
### Installed Packages
- 'django<4' gunicorn
- dj_database_url psycopg2
- dj3-cloudinary-storage
- django-summernote
- django-allauth
- django-cripsy-forms

## Deployment
The site was deployed to Heroku. The steps used are as follows:
- Install Django and Gunicorn: pip3 install 'django<4' gunicorn
- Install Django database and psycopg: pip3 install dj_database_url psycopg2
- Install Cloudinary: pip3 install dj3-cloudinary-storage
- Creating the requirements.txt file with the following command: pip3 freeze --local > requirements.txt
- a django project was created using: django-admin startproject thecardiacnurse .
- the blog app was then created with: python3 manage.py startapp cardiacnurseblog
- which was then added to the settings.py file within our project directory.
- the changes were then migrated using: python3 manage.py migrate
- navigated to Heroku & created a new app called cardiacnurseprofile.
- added the Heroku Postgres database to the Resources tab.
- navigated to the Settings Tab, to add my key/value pairs configvars
- added the DATABASE_URL, SECRET_KEY & CLOUDINARY_URL to the settings.py file
- add an import os statement for the env.py file.
- added Heroku to the ALLOWED_HOSTS in settings.py
- created the Procfile
- pushed the project to Github
- connected my github account to Heroku through the Deploy tab
- connected my github project repository, and then clicked on the "Deploy" button

## Credits

