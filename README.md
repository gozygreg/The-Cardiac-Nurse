# THE CARDIAC NURSE
The Cardiac Nurse website is go-to platform for every nurse that specialise in anything that has to do with the cardiovascular system. It is an educational medium that all nurses can learn from, particularly those with keen intrest in cardiology.

# Table of Contents
- [UX](#ux)
- [User Stories](#user)
- [Design](#design)
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
1. I can create, read, update and delete post so that I can manage the contents and flow of the site. **Story point: 3**
2. I can create draft posts so that I can finish writing the content later. **Story point: 2**
3. I can approve or disapprove comments so that prevent sharing inappropriate/offensive comments. **Story point: 1**

As the site administrator (For Nurse Profile app):
1. I can verify and accept new nurses that what to join the platform so that they can be viewed by site visitors. **Story point: 2**
2. I can add a new nurse profile, update or delete an existing nurse profile so that i can manage the content and flow of nurses in the site. **Story point: 4** 
### Nurse stories
As a nurse registered on the platform:
1. I can upload my profile picture so that other site users can see what I look like. **Story point: 3**
2. I can create a user profile and write about my career journey as a cardiac nurse so that I can be found and viewed on the site. **Story point: 2**
### Site visitors' stories
As a visitor of the site:
1. I can view any nurse profile so that see their career journey. **Story point: 1**
2. I can signup for an account so that I can like and comment on posts as well as create a profile if I am a cardiac nurse. **Story point: 2**
3. I can view a list of post so that I can select one to read. **Story point: 2**
4. I can click to open a post so that read the content of the post. **Story point: 1**
5. 1 can view a paginated list of post so that I can select a post to view. **Story point: 2**
6. I can be able to like or unlike post so that I can interact with the content. **Story point: 2**
7. I can view the number of likes on individual post so that know the most popular post. **Story point: 2**
8. I can be able to comment on post so that I can be able to leave feedback and engage further. **Story point: 2**
9. I can view comments on each post so that know the most engaging post. **Story point: 1**

## Design
### Wireframe
- Home Page
![Home page (Alternate 899t)](https://user-images.githubusercontent.com/69070044/200598172-65bd1d71-965c-43df-bd26-48fdeca7273c.png)

- Nurse Profile Page
![Our Nurse page](https://user-images.githubusercontent.com/69070044/200598318-b714ba7d-2432-4f5f-89c2-2879563d7d2a.png)

- Nurse Profile Detail Page
![Nurse profile page](https://user-images.githubusercontent.com/69070044/200598243-37067813-6ee3-4a6b-bbed-e482a84bc87b.png)

- Edit Profile Page
![Edit page](https://user-images.githubusercontent.com/69070044/200598421-25afcb4f-a894-4eef-a35d-bce2e8f896c9.png)

- Blog Page
![Nurse blog page](https://user-images.githubusercontent.com/69070044/200598497-a1afe92a-b991-4cde-a537-c3a4ce109b1d.png)

- Blog Detail Page
![blog detail page](https://user-images.githubusercontent.com/69070044/200598622-fc429b95-6efd-46f1-a59d-3a06197ef66d.png)

- Signup/Register Page
![signup page](https://user-images.githubusercontent.com/69070044/200598614-e641d0b0-4fcd-4696-8aa3-32d94e79c105.png)

- Logout Page
![Logout page](https://user-images.githubusercontent.com/69070044/200598656-0f8f6fed-26bd-4e8e-8382-f933071ffce6.png)

### Functional Structure
### Database Structure
Three models were created to produce the required database structure.
- Nurse profile model: Contains all the information about a particular nurse in the database. This model has the name of the nurse and the creator of the profile, date  profile was created, image or picture on the profile, his or her specialty in nursing, his job description or career experience and status of the profile (published or not published).
- Blog model: Contains all the information about the blog post such as title of blog post, authur, image, excerpt, likes, date updated and status of blog post (draft or published).
- Comment model: Create the ability for loggin users to submit their thoughts or contributions to posts as well as the ability of site administrator to approve or disapprove any comments.
- The blog and comment model was an inspiration from code institute django walkthrough project "I think therefore I blog".
<img width="554" alt="Screenshot 2022-11-08 at 00 34 08" src="https://user-images.githubusercontent.com/69070044/200445609-b18d1ea8-1798-4e76-9db8-d2d9c9867700.png">


### Features
- Home page
- Nurse profile page
- Nurse detail page
- Nurse blog page
- Blogpost detail page
- Sign up, Log in and log out pages

### CRUD Fuctionality

### Features for Future Implementation
- Vancancies/Job opportunity app
- Research section
- Article archive
- Password reset

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

