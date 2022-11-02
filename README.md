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
### Site visitor's Goal
- Site visitors are able to see the profile and professional experience/journey of nurses who registered
- Site visitors are able to read the various blog posts on the site.

## User Stories

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

