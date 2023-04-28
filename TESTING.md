# TABLE OF CONTENTS
- [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Lighthouse](#lighthouse-testing)
    - [Python and Javascript Testing](#python-and-javascript-testing)
    - [Manual Testing](#manuel-testing)
        - [User Story Testing](#user-story-testing)
            - [Site Admin](#as-an-site-admin-i-can)
            - [Registered User/Nurse](#as-a-registered-user--nurse-on-the-platform-i-can)
            - [Unregistered User/Site Visitor](#as-a-site-visitor-or-unregistered-user-i-can)
    - [Authorizaton and Authentication Testting](#authorizaton-and-authentication-testting)
    - [Automatic Testing](#automatic-testing)


# Testing
- ## Validator Testing
    - All html files in the template directory were passed through the [W3C validator](https://validator.w3.org/) with no errors found 
    <img width="1280" alt="html val" src="https://user-images.githubusercontent.com/69070044/203661954-97bf1c00-c4b4-4c9c-9593-d50d069c6830.png">

    - CSS file has been passed through [Jigsaw validator](https://jigsaw.w3.org/css-validator) with no issues found
    <img width="1280" alt="css validator" src="https://user-images.githubusercontent.com/69070044/201546693-42ab2f73-a790-4475-946a-834a4a1500e6.png">

    - All python code was subjected to [PEP8 Online](https://www.pythonchecker.com/) with no significant issues other than some line of code being longer than 79 characters and the need to add two lines in front of a function definition.
    <img width="1280" alt="pep8" src="https://user-images.githubusercontent.com/69070044/201548367-2e0594f2-0554-43f1-bba2-dfb0ad264fd9.png">

- ## Lighthouse Testing
    - Home page <br>
        - <img width="1000" alt="lightgouse" src="https://user-images.githubusercontent.com/69070044/202856712-c93d08f3-0cb7-463f-a4bb-e8cd387cea8f.png">
    - Blog list page (Mobile view) <br>
        - <img width="571" alt="LH bloglist MV" src="https://user-images.githubusercontent.com/69070044/235110079-4f40c879-1cce-426d-82ce-168b2b1a11ee.png">
     - Blog list page (Desktop view) <br>
        - <img width="500" alt="LH bloglist DV" src="https://user-images.githubusercontent.com/69070044/234426332-496aa0d1-54e6-4cd0-b810-58593275104c.png">
    - Blog detail page (Mobile view) <br>
        - <img width="500" alt="LH bloglist detail" src="https://user-images.githubusercontent.com/69070044/235110089-39838217-c6f2-4fd7-a8a2-fe9efae18513.png">
    - Blog detail page (Desktop view) <br>
        - <img width="500" alt="LH blogdetail DV" src="https://user-images.githubusercontent.com/69070044/235075006-45d6aeca-ae19-40b6-a831-31c66af046bb.png">
    - Profile list page (Mobile view) <br>
        - <img width="577" alt="LH Profile list MV" src="https://user-images.githubusercontent.com/69070044/235111377-9f86e222-cac7-4209-bc1c-4e995ee704b6.png">
    - Profile list page (Desktop view) <br>
        - <img width="500" alt="LH profilelistpage DV" src="https://user-images.githubusercontent.com/69070044/234425656-256e3bcf-6bc0-4923-bfff-383118a5a4f1.png">
    - Profile detail page (Mobile view) <br>
        - <img width="599" alt="LH Profile detail MV" src="https://user-images.githubusercontent.com/69070044/235111388-f15f54f7-b536-448b-8c33-c17d76b749e8.png">
    - Profile detail page (Destop view) <br>
        - <img width="500" alt="LH profiledetail DV" src="https://user-images.githubusercontent.com/69070044/234425790-9e4348df-943a-4741-81e9-f28595cdf106.png">


    - ## Lighthouse analysis and improvements:
        - All pages were run through lighthouse check site performance, accessibility, best practices and SEO. 
        - All the pages came back with a score of 90 and above for desktop screens.
        - Initially mobile screens for profile detail page, profile list page and blog detail pages came back with a score of less than 90 in performace. I improved the score by;
            - optimizing the images
            - the use of CDN to reduce the load on the server and improve the delivery speed of site contents.
            - using responsive design technique


- ## Python and JavaScript Testing
    - All Custom Python & JavaScript code was manually tested multiple times during and after development. This is reflected in the fact that all of the user stories below are working and have produced no errors in the terminal or the console.

    - All social links are working and open to external pages

    - Site checked and is working in various browsers such as Chrome and Safari

- ## Manual Testing 
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

        - ## *As a Registered user / nurse on the platform I can ...*
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

        - ## *As a site visitor or unregistered user I can...*
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

- ## Authorizaton and Authentication Testting
    - If an authenticated user attempts to directly access a profile that does not belong to them by typing its address on the URL, they will be unable to delete or edit it.
    - A message box appears to show this.
    - User are then redirected to nurse profile list page
        - <img width="1000" alt="message-edit" src="https://user-images.githubusercontent.com/69070044/235131152-f605e17e-b3c8-420c-bbff-7ed7e86b4bb9.png">
        - <img width="1000" alt="message-delete" src="https://user-images.githubusercontent.com/69070044/235131161-1d21ce94-c510-4e5a-822b-760a76b18547.png">

    - Also, Non-logged in users cannot delete or edit profiles on the site via URLs. They are will be redirected to signup page.
        - <img width="500" alt="signup page" src="https://user-images.githubusercontent.com/69070044/235146462-a9465d49-bf03-4cf9-8b32-d1e5b556542b.png">

    - Take note: Authenticated users who are registered nurses but do not have a profile can join the platform. The "Join the platform" button will only be visible to authenticated users who have not yet joined the platform or set up their profile. Unauthenticated users and authenticated users who already have a profile or have joined the platform will not see this button as it is hidden.
        - <img width="1000" alt="Join our platform button" src="https://user-images.githubusercontent.com/69070044/235149178-d9212b4a-ab7a-4986-ba90-5e10eeaa43a3.png">


- ## Automatic Testing
    - After testing all the user stories manually, I went further to run just two automatic test due to time contrains. 
        - <img width="500" alt="Screenshot 2023-04-28 at 07 39 22" src="https://user-images.githubusercontent.com/69070044/235073405-d70a930c-2d7f-4b07-be47-f4b51926c200.png">
    
    1. 
        <hr>

            class TestSubmitNurseProfile(TestCase):
                """
                Tests for Submit Nurse Profile Form
                """
                def test_nurse_name_required(self):
                    """
                    Verify nurse name is required
                    """
                    form = SubmitNurseProfile({'nurse_name': ''})
                    self.assertFalse(form.is_valid())
                    self.assertIn('nurse_name', form.errors.keys())
                    self.assertEqual(
                        form.errors['nurse_name'][0], 'This field is required.')
        <hr>

        - This is a test class named "TestSubmitNurseProfile" that inherits from Django's "TestCase" class. It contains a test method named "test_nurse_name_required" that checks if the "nurse_name" field in the "SubmitNurseProfile" form is required.
        - In the "test_nurse_name_required" method, a new form object is created with an empty "nurse_name" field. The test then checks if the form is not valid and if the "nurse_name" field is in the form's errors. It then checks if the error message for the "nurse_name" field is "This field is required."
        - This test ensures that the "nurse_name" field is properly validated and that the form requires a value for this field. If the test fails, it means that the form is not properly validating the "nurse_name" field.

    2. 
        <hr>

            class TestViews(TestCase):
            """
            Test views
            """
                def test_nurse_profile_page(self):
                    """
                    verify nurse profile page loads
                    """
                    url = reverse('nurse_profile')
                    response = self.client.get(url)
                    self.assertEqual(response.status_code, 200)
                    self.assertTemplateUsed(response, 'nurseprofile.html')

        <hr>

        - This is a test case for testing the behavior of a Django view called nurse_profile. The test verifies that when the user visits the URL associated with this view, the page loads successfully and the correct template (nurseprofile.html) is used to render the page.
        - The test uses the Django TestCase class and the Client class to simulate a GET request to the URL associated with the nurse_profile view. The reverse function is used to generate the URL for the view based on its name. The response object returned by the view is then checked to ensure that the status code is 200 (OK) and that the correct template is used to render the response.

[back to readme](./README.md)

       