# THE CARDIAC NURSE
The Cardiac Nurse website is go-to platform for every nurse that specialise in anything that has to do with the cardiovascular health. It is an educational medium that all nurses can learn from, particularly those with keen interest in cardiology. See [link](http://cardiacnurseblog.herokuapp.com/) to deployed site 


<img width="1041" alt="Responsive" src="https://user-images.githubusercontent.com/69070044/201549312-97292c00-b1b1-4715-986c-0881a7aff5e0.png">

# Table of Contents
- [UX](#ux)
    - [Site Aim](#site-aim)
    - [Site Goals](#user-goals)
    - [User Goals](#user-goals)
    - [Site Visitors' Goal](#site-visitors-goals)
- [Agile Methodology](#agile-methodology)
    - [Epics](#epics)
    - [Acceptance Criteria](#nurse-stories-and-corresponding-acceptance-criteria)
- [Design](#design)
    - [Wireframe](#wireframe)
    - [Database Structure](#database-structure)
    - [Features](#features)
    - [CRUD](#crud-fuctionality)
- [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Lighthouse](#lighthouse-testing)
    - [Python and Javascript Testing](#python-and-javascript-testing)
- [Technologies](#technologies)
- [Deployment](#deployment)
- [Credits](#credits)
- [Dedication](#dedication)

## Ux
- ### Site Aim
The purpose of the cardiac nurse website is to bring together nurses with intrest in all areas of cardiology care. Its aim is to provide educational support through extensive and research oriented blog post.
- ### Site Goals
    - create a medium where nurses can be inspired, enlightened and informed about new developments in heart health.
    - create a platfrom where cardiac nurses can be found and can also find collegues.
- ### User Goals
    - User/nurse is able to join platform, create a profile and update their professional experience/journey as a cardiac nurse
    - User/nurse is able to access blogpost and stay up-to-date with treatment guildelines in various aspect of cardiology
- ### Site visitors' Goals
    - Site visitors are able to see the profile and professional experience/journey of nurses who registered
    - Site visitors are able to read the various blog posts on the site.

## Agile Methodology
The plan for this project was carried out using the Agile Methodology in Github. Epics and User Stories were created using [issues](https://github.com/gozygreg/The-Cardiac-Nurse/issues) on git hub. Each user story explicitly explains the purpose of the issues. Each story was assigned a classification of must-have, should-have, could-have or future-have. It was prioritised using GitHub labels with different colors. See link to kanban board [here](https://github.com/users/gozygreg/projects/14/views/1). Various tasks performed were also itemized using the agile methodology in Github.

- ### Epics
    1. Nurse Profile
    2. Nurse Blog
    3. Sign in/out
    4. Messaging

For simplicity in the readme documentation, I have categorized all user stories in to three below; Admin stories, Nurse stories and site visitors stories. However, visit my [epics](https://github.com/gozygreg/The-Cardiac-Nurse/issues) on git hub to see more of the agile methodology arrangement. I have created 4 Epics and 16 user stories and various tasks under each user stories.

### Admin stories and Corresponding Acceptance Criteria
As the site administrator (For Nurse Blog app):
1. I can create, read, update and delete post so that I can manage the contents and flow of the site.
    - Acceptance Criteria
        - Scenario: Create Read and Update post
        - Given: The admin navigates to django admin panel
        - When: The admin add "/admin" to the site url
        - Then: The django admin page loads and the admin can create read and delete post

2. I can create draft posts so that I can finish writing the content later.
    - Acceptance Criteria
        - Scenario: Create draft
        - Given: The admin navigates to django admin panel
        - When: The admin add "/admin" to the site url
        - Then: The admin can create a draft post to complete and publish later

3. I can approve or disapprove comments so that prevent sharing inappropriate/offensive comments.
    - Acceptance Criteria
        - Scenario: Manage comments
        - Given: The admin navigates to the django admin panel
        - When: The admin add "/admin" to the site url
        - Then The admin can click on "approve" button to approve comments or leave it unapproved. If approved, the comment can then be seen on the blog post page

As the site administrator (For Nurse Profile app):
1. I can verify and accept new nurses that what to join the platform so that they can be viewed by site visitors.
    - Acceptance Criteria
        - Scenario: Verify new nurses joining platform
        - Given: A new nurse have join platform and admin navigates to admin panel
        - When: The admin add "/admin" to the site url
        - Then: The admin can click "action" and then choose "verify nurse" option. The new nurse can now be seen on the profile page of the website
2. I can add a new nurse profile, update or delete an existing nurse profile so that i can manage the content and flow of nurses in the site.
 - Acceptance Criteria
        - Scenario: Manage Nurse Profile
        - Given: The admin navigates to the django admin panel
        - When: The admin add "/admin" to the site url
        - Then The admin can click on "delete" or "add" button to manage new or existing profiles
### Nurse stories and Corresponding Acceptance Criteria
As a nurse registered on the platform:
1. I can create a user profile and write about my career journey as a cardiac nurse so that I can be found and viewed on the site.
    - Acceptance Criteria
        - Scenario: Creating user/nurse profile
        - Given: A user/nurse is registered
        - When: The registered user click "Join our platform" button
        - Then: The user/nurse can fill and submit the form to join platform. And then await verification by site administrator

2. I can upload my profile picture so that other site users can see what I look like.
    - Acceptance Criteria
        - Scenario: Upload user/nurse profile picture
        - Given: A user/nurse is registered and filled the registration form
        - When: The user/nurse click "Join our platform" button
        - Then: The user/nurse can upload his/her picture by clicking "Choose File" on the form. And then await verification by the site administrator


### Site visitors' stories and Corresponding Acceptance Criteria
As a visitor of the site:
1. I can view any nurse profile so that see their career journey. 
    - Acceptance Criteria
        - Scenario: View various nurse profiles on the website
        - Given: The site visitor navigate to the "our nurses" page
        - When: The site visitor click "Our Nurses" button
        - Then: The site visitor is now able to see the profile picture and name of nurses that are registered on the site

2. I can signup for an account so that I can like and comment on posts as well as create a profile if I am a cardiac nurse.
    - Acceptance Criteria
        - Scenario: Signing Up
        - Given: The site visitor navigate to the signin page
        - When: The site visitor click "Sign In" button
        - Then: The site visitor is now able to register and have access to like and comment on post

3. I can view a list of post so that I can select one to read. 
    - Acceptance Criteria
        - Scenario: See Post List
        - Given: The site visitor navigate to the "Our Blog" page
        - When: The site visitor click "Our Blog" button
        - Then: The site visitor is able to various blog post to choose from.

4. I can click to open a post so that read the content of the post. 
    - Acceptance Criteria
        - Scenario: Read Blog Post
        - Given: The site visitor navigate to the "Our Blog" page
        - When: The site visitor click one of the post in the post list
        - Then: The site visitor is able read the content of the particular post

5. 1 can view a paginated list of post so that I can select a post to view. 
    - Acceptance Criteria
        - Scenario: See more post list
        - Given: The site visitor is post list page and there are more than 6 posts
        - When: The site visitor click on "next" button
        - Then: The site visitor is able to see all the post on the next page

6. I can be able to like or unlike post so that I can interact with the content. 
    - Acceptance Criteria
        - Scenario: Liking Posts
        - Given: The site visitor registered and navigate to the our blog page
        - When: The site visitor click "Our Blog" button
        - Then: The site visitor is now able to like or unlike post

7. I can view the number of likes on individual post so that know the most popular post.
    - Acceptance Criteria
        - Scenario: View Number of Likes
        - Given: The site visitor is registered or is sign in and have navigated to the blog post list
        - When: The site visitor click on "Our blog" button
        - Then: The site visitor is able to see the number of likes that a post have

8. I can be able to comment on post so that I can be able to leave feedback and engage further.
    - Acceptance Criteria
        - Scenario: Comment on Post
        - Given: The site visitor is registered or is sign in and have navigated to a particular blog post
        - When: The site visitor click on the hyperlink text on the blog post
        - Then: The site visitor is has access to write comments on the post

9. I can view comments on each post so that know the most engaging post.
    - Acceptance Criteria
        - Scenario: View Comments
        - Given: The site visitor is registered or is sign in and have navigated to a particular blog post
        - When: The site visitor click on "Our blog" button
        - Then: The site visitor is able to see and read the comment writen about the post.

## Design
- ### Wireframe
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


- ### Database Structure
    - Three models were created to produce the required database structure.
        - Nurse profile model: Contains all the information about a particular nurse in the database. This model has the name of the nurse and the creator of the profile, date  profile was created, image or picture on the profile, his or her specialty in nursing, his job description or career experience and status of the profile (published or not published).
        - Blog model: Contains all the information about the blog post such as title of blog post, authur, image, excerpt, likes, date updated and status of blog post (draft or published).
        - Comment model: Create the ability for loggin users to submit their thoughts or contributions to posts as well as the ability of site administrator to approve or disapprove any comments. The blog and comment model was an inspiration from code institute django walkthrough project "I think therefore I blog".

        - <img width="554" alt="Screenshot 2022-11-08 at 00 34 08" src="https://user-images.githubusercontent.com/69070044/200445609-b18d1ea8-1798-4e76-9db8-d2d9c9867700.png">
    - The flow chart of the website below:
        - ![The Cardiac Nurse Flow chart](https://user-images.githubusercontent.com/69070044/204094866-1f058c6e-462f-461e-8c58-129e677d343a.png)


- ### Features
    - Home page

    <img width="993" alt="home" src="https://user-images.githubusercontent.com/69070044/201520809-f00fb672-35b7-482a-a7a5-0e9bf2ec2096.png">

    - Nurse profile page

    <img width="820" alt="profilepage" src="https://user-images.githubusercontent.com/69070044/201520815-6ffe1f25-b948-46ea-a180-d3ee37cde434.png">

    - Nurse profile detail page

    <img width="492" alt="profile detail" src="https://user-images.githubusercontent.com/69070044/201520816-a7f518bc-536c-463f-a029-8fd01dcd57f2.png">

    - Site advert section: This section is beneath the profile of each nurse and it has an external link to the british cardiovascular society. Details of this advert is hidden on small devices

    <img width="1280" alt="bcs advert section" src="https://user-images.githubusercontent.com/69070044/202856828-bea3ee56-9294-4890-9a96-49e9250dd12d.png">

    - Nurse blog page

    <img width="762" alt="blogpage" src="https://user-images.githubusercontent.com/69070044/201520823-e09a9a39-5645-4efb-a343-de3cee281ef2.png">

    - Blogpost detail page

    <img width="445" alt="blogdetail" src="https://user-images.githubusercontent.com/69070044/201520827-5f80cb8f-4afe-43f4-9359-b2cc872d32d9.png">

    - Sign up, Log in and log out pages

    <img width="936" alt="signup" src="https://user-images.githubusercontent.com/69070044/201520832-6ced2e5d-544b-459d-9dae-ec09fbb41c1c.png">

    <img width="945" alt="signin" src="https://user-images.githubusercontent.com/69070044/201520836-59fa3c39-f9c5-4ec6-b55e-1845ed19b711.png">

- ### CRUD Fuctionality
    - CREATE:
    - By clicking the button 'Join our platform' in the website, authenticated users/nurses are able to create a profile
    <img width="1280" alt="Create" src="https://user-images.githubusercontent.com/69070044/201519597-2a76d79d-20fd-466a-bddf-8201fa02a6c6.png">

    - This button is only visible to users that have signed in or registered.
    <img width="1280" alt="CreateofCrud" src="https://user-images.githubusercontent.com/69070044/201519594-ec8918bc-5bb1-4908-a7ec-2513a44884a5.png">

    - READ:
    - Users (registered or not registered) are able to see various nurse profiles and blog posts available on the website
    - UPDATE & DELETE:
    - Users who are signed in/registered and have gone further to create a profile are able to edit/update as well as delete their profile should they wish to. This can be done using the edit and delete button respectively in the profile detail page on the website.
    <img width="1280" alt="crUD" src="https://user-images.githubusercontent.com/69070044/201519611-faa2f733-1a44-4a69-ae16-f0f0bf1998c1.png">

    - On the backend side of thing in django admin panel, the site administrator is able to perform all the CRUD functionality on both the profile app and blog app.

- ### Features for Future Implementation
    - Vancancies/Job opportunity app
    - Research section
    - Article archive
    - Password reset

## Testing
- ### Validator Testing
    - All html files in the template directory were passed through the [W3C validator](https://validator.w3.org/) with no errors found 
    <img width="1280" alt="html val" src="https://user-images.githubusercontent.com/69070044/203661954-97bf1c00-c4b4-4c9c-9593-d50d069c6830.png">

    - CSS file has been passed through [Jigsaw validator](https://jigsaw.w3.org/css-validator) with no issues found
    <img width="1280" alt="css validator" src="https://user-images.githubusercontent.com/69070044/201546693-42ab2f73-a790-4475-946a-834a4a1500e6.png">

    - All python code was subjected to [PEP8 Online](https://www.pythonchecker.com/) with no significant issues other than some line of code being longer than 79 characters and the need to add two lines in front of a function definition.
    <img width="1280" alt="pep8" src="https://user-images.githubusercontent.com/69070044/201548367-2e0594f2-0554-43f1-bba2-dfb0ad264fd9.png">

- ### Lighthouse Testing
    - <img width="1128" alt="lightgouse" src="https://user-images.githubusercontent.com/69070044/202856712-c93d08f3-0cb7-463f-a4bb-e8cd387cea8f.png">

- ### Python and JavaScript Testing
    - All Custom Python & JavaScript code was manually tested multiple times during and after development. This is reflected in the fact that all of the user stories below are working and have produced no errors in the terminal or the console.

    - All social links are working and open to external pages

    - Site checked and is working in various browsers such as Chrome and Safari

## Technologies
- ### Programming Languages
    - HTML
    - CSS
    - JavaScript
    - Python
    - SQL
    - Postgres
    - [ElephantSQL](https://www.elephantsql.com/)
- ### Frameworks and Libraries
    - [Django](https://www.djangoproject.com/)
    - [Bootstrap](https://getbootstrap.com/)
    - [Gitpod](https://www.gitpod.io/)
    - [Github](https://github.com/)
    - [Google Fonts](https://fonts.google.com/about)
    - [Font Awesome](https://fontawesome.com/)
    - [Balsamqid](https://balsamiq.com/)
    - [Am I Resposive](https://ui.dev/amiresponsive)
    - [Adobe stock images](https://stock.adobe.com/uk)
    - [Image resizer](https://imageresizer.com/)

- ### Installed Packages
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
- See [link](http://cardiacnurseblog.herokuapp.com/) to deployed site 

## Credits
- My code institute mentor Martina Terlevic for her constant guide and support
- Student care support from Oisin tahak.
- [Stackoverflow platform](https://stackoverflow.com/)
- The buttons in the site is styled by inspiration from [webdeasy.de](https://webdeasy.de/)

## Dedication
- This project is dedicated to my wife and son who was born 2 weeks before the submission deadline. 

[top of page](#table-of-contents)
