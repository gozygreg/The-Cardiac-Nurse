# TABLE OF CONTENTS
- [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Lighthouse](#lighthouse-testing)
    - [Python and Javascript Testing](#python-and-javascript-testing)
    - [Manuel Testing](#manuel-testing)
        - [User Story Testing](#user-story-testing)
            - [Site Admin](#as-an-site-admin-i-can)
            - [Registered User/Nurse](#as-a-registered-user--nurse-on-the-platform-i-can)
            - [Unregistered User/Site Visitor](#as-a-site-visitor-or-unregistered-user-i-can)
    - [Automatic Testing](#automatic-testing)







## Testing
- ### Validator Testing
    - All html files in the template directory were passed through the [W3C validator](https://validator.w3.org/) with no errors found 
    <img width="1280" alt="html val" src="https://user-images.githubusercontent.com/69070044/203661954-97bf1c00-c4b4-4c9c-9593-d50d069c6830.png">

    - CSS file has been passed through [Jigsaw validator](https://jigsaw.w3.org/css-validator) with no issues found
    <img width="1280" alt="css validator" src="https://user-images.githubusercontent.com/69070044/201546693-42ab2f73-a790-4475-946a-834a4a1500e6.png">

    - All python code was subjected to [PEP8 Online](https://www.pythonchecker.com/) with no significant issues other than some line of code being longer than 79 characters and the need to add two lines in front of a function definition.
    <img width="1280" alt="pep8" src="https://user-images.githubusercontent.com/69070044/201548367-2e0594f2-0554-43f1-bba2-dfb0ad264fd9.png">

- ### Lighthouse Testing
    - Home page <br>
        - <img width="1000" alt="lightgouse" src="https://user-images.githubusercontent.com/69070044/202856712-c93d08f3-0cb7-463f-a4bb-e8cd387cea8f.png">
    - Blog list page (Mobile view) <br>
        - <img width="500" alt="LH bloglistpage MV" src="https://user-images.githubusercontent.com/69070044/234424046-89d5a8ab-c791-4cd2-8e70-4944abae8284.png">
     - Blog list page (Desktop view) <br>
        - <img width="500" alt="LH bloglist DV" src="https://user-images.githubusercontent.com/69070044/234426332-496aa0d1-54e6-4cd0-b810-58593275104c.png">
    - Blog detail page (Mobile view) <br>
        - 
    - Blog detail page (Desktop view) <br>
        - 
    - Profile list page (Mobile view) <br>
        - 
    - Profile list page (Desktop view) <br>
        - <img width="500" alt="LH profilelistpage DV" src="https://user-images.githubusercontent.com/69070044/234425656-256e3bcf-6bc0-4923-bfff-383118a5a4f1.png">
    - Profile detail page (Mobile view) <br>
        - 
    - Profile detail page (Destop view) <br>
        - <img width="500" alt="LH profiledetail DV" src="https://user-images.githubusercontent.com/69070044/234425790-9e4348df-943a-4741-81e9-f28595cdf106.png">


- ### Python and JavaScript Testing
    - All Custom Python & JavaScript code was manually tested multiple times during and after development. This is reflected in the fact that all of the user stories below are working and have produced no errors in the terminal or the console.

    - All social links are working and open to external pages

    - Site checked and is working in various browsers such as Chrome and Safari

- ### Manuel Testing 
    Below is a summary of how I manually tested each user story. 
    - #### **User Story Testing**
        - ### *As an site admin I can...*
        | checked | create, read, update and delete post so that I can manage the contents and flow of the site |
        | ------- | ------------------------------------------------------------------------------------------- |
        | ✓ | add "/admin" to the site url |
        | ✓ | log on to admin panel        |
        | ✓ | create blog post             |
        | ✓ | read blog post               |
        | ✓ | update blog post             |
        | ✓ | delete blog post             |
        | checked | create draft posts so that I can finish writing the content later |
        | ✓ | create draft post to complete later |
        | checked | approve or disapprove comments so that prevent sharing inappropriate/offensive comments. |
        | ✓ | click on "approve" button to approve comments or leave it unapproved |
        | checked | verify and accept new nurses that what to join the platform so that they can be viewed by site visitors. |
        | ✓ | click "action" and then choose "verify nurse" option |
        | checked | add a new nurse profile, update or delete an existing nurse profile so that i can manage the content and flow of nurses in the site. |
        | ✓ | click on "add" button to add a new nurse profiles to the site |
        | ✓ | click on "delete" button to remove an existing nurse profile |

        - ### *As a Registered user / nurse on the platform I can ...*
        | checked | create a user profile and write about my career journey as a cardiac nurse so that I can be found and viewed on the site. |
        | --- | ------------------------------------------------------------------------------------------- |
        | ✓ | Link to register or signup is in navigation menu |
        | ✓ | "Join our platform" button is only visible to authenticated users/registered nurses that does not have a profile or have not joined the platform |
        | ✓ | "Join our platform" button is present in our "nurses page" |
        | ✓ | clicking on "Join our platform" button navigates registered user/nurse to form |
        | ✓ | registered user/nurse is able to fill form |
        | ✓ | form validation is present |
        | ✓ | submit button is present |
        | checked | upload my profile picture so that other site users can see what I look like. |
        | ✓ | registered user/nurse is able to choose/select and upload their picture |
        | ✓ | after form is submitted, message box appear to inform user that their details will be verified by admin. |
        | checked | view a list of post so that I can select one to read. |
        | ✓ | "Checkout our blog" button is present on the homepage |
        | ✓ | "Our Blog" link is present in page navigation menu |        
        | ✓ | When you click on the button or link, you are able to navigate to and view the various blogpost list. |
        | ✓ | The blogpost picture and title of each blog is visible on the blogpost list page  |
        | ✓ | You can access the detail or content of a particular blogpost by clicking on their title, which is located below their blogpost picture. |
        | ✓ | I can like a post by clicking the heart button present beneath the post |
        | ✓ | I can view the total number of like a post have received and this can be found beneath each post |      
        | ✓ | There is a comment box where I can leave my comment on a post |
        | ✓ | The comment box has a submit button |
        | ✓ | A message is displayed that my comment is awaiting approval by site admin after my form is validated and  I click the submit button |
        | ✓ | I am able to view all the comment other registered user have left about a post |

        Note: Authenticated user/Registered nurse that do not have a profile is able to join the platform. The "Join the platform" button is only visible to authenticated users who have not already joined the platform or set up their profile. This button is hidden for unauthenticated user and authenticated user who already have a profile or joined the platform 

        - ### *As a site visitor or unregistered user I can...*
        | checked | view any nurse profile so that see their career journey. |
        | ------- | ------------------------------------------------------------------------------------------- |
        | ✓ | "Meet our nurses" button is present on the homepage |
        | ✓ | "Our Nurses" link is present in page navigation menu |        
        | ✓ | When you click on the button or link, you are able to navigate to and view the profiles of nurses. |
        | ✓ | The profile picture and name of each nurse is visible on our nurses page  |
        | ✓ | You can access a nurse's profile details by clicking on their name, which is located below their profile picture. This allows you to navigate to their profile page.  |
        | checked | view a list of post so that I can select one to read. |
        | ✓ | "Checkout our blog" button is present on the homepage |
        | ✓ | "Our Blog" link is present in page navigation menu |        
        | ✓ | When you click on the button or link, you are able to navigate to and view the various blogpost list. |
        | ✓ | The blogpost picture and title of each blog is visible on the blogpost list page  |
        | ✓ | You can access the detail or content of a particular blogpost by clicking on their title, which is located below their blogpost picture. |
        | ✓ | Comment box is absent and I can not leave a comment since I am an unregistered user |
        | ✓ | I am able to view all the comment registered user have left about a post |
        | ✓ | I can view the total number of like a post have received and this can be found beneath each post |    
        | checked | signup for an account so that I can like and comment on posts as well as create a profile if I am a cardiac nurse. |
        | ✓ | "Join Us / Register" link is present in page navigation menu |        
        | ✓ | When you click on the link, you are able to navigate to the signup form. |
        | ✓ | Signup button is present below the form | 
        | ✓ | Message to await verification is seen once form is filled  and signup button is clicked|

- ### Automatic Testing
    - After testing all the user stories manually, I went further to attempt automatic testing. 
    <hr>
    class HomePageTest(TestCase): 

        def setUp(self): 
            self.client = Client()

        def test_home_page(self):
            response = self.client.get(reverse('home_page'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'index.html') 
    <hr>

    - This test sets up a test client, makes a GET request to the home_page view using the reverse function to get the URL, and then checks that the response status code is 200 and that the response uses the index.html template.

    - However, was an error when running the command "python manage.py test". The error message indicates that there is a permission issue with creating a test database. The error also mentions that Django is unable to connect to the 'postgres' database and will use the first PostgreSQL database instead.

    - Due to lack of time and the amount time it will take to do automatic testing for all the code I have already written, I am unable to resolve this issue at this time. For this reason, I focus on doing an extensive manual testing as seen above.

    - I however, intend to solve this problem and go ahead in doing the automatic test. Below are troubleshooting steps, I would try in rosolving the problem.
        1. check the permissions of the database
        2. verify that the PostgreSQL database server is properly configured
        3. ensure that the necessary dependencies are installed
        4. try running the command with elevated privileges, such as by using the sudo command.
        5. seek help from online community or support forum related to Django and database management.
    

[back to readme](./README.md)

       