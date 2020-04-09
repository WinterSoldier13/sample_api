# sample_api
<h1>How to test?</h1>
<br>Run python manage.py
<br>Send api calls to the displayed url followed by the details as explained below:
<br>
<br>
to login a user call: http://localhost:8000/login/ayushsingh1315@outlook.com,password/ , if successful it wil return "login_successful"
<br>
<br>
<br>To sign up a user call: http://localhost:8000/signup/Ayush%20Singh,aysdfdfsfsafsdfdsasdfushsingh1315@gmail.com,password,phone/
<br> if successful it will return a unique key: "key: {'name': '-M4UMbVhNDgq2uzLw_LW'}"
<br>else it will return "user already exits"
