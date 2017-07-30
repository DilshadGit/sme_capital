Create Loan

control_app:
Create project with two applications first apps to control the system of the project where display the layout of all website such as main page.

installed django_registration_redux for user login and logout where user has no access to the admin site and cms or dashboard site (CMS not required in this test I have just added I will make some update later on for fun)

Intelled bootstrap3 for layout process

Second application loan_app, here user can check own profile and edit. Also user can create, view, eidt or update and delete the loan if needed.

Notice: I can create 3 types of users, user has access to only own profile page with all loan creation when loggedin. Second user can have access to the same above plus cms page the second user is company staff. The third user is developer which is calles superuser has access to general login/out, cms and admin page.

The last part of this test is display the data as JSON object using rest_framework user can create, view, eidt and delete data from api page. 

Notice:

I have used slug to display the title in the url I could used just id or pk but slug more active. 


There registered User:
Username: admin, Password: _Admin_123
Username: admin, Password: _Admin_123
Username: admin, Password: _Admin_123