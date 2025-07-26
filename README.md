# MiniProject1_GUVI
                                        Automation Testing of EdTech Platform Web Application(GUVI Website)

This project is to automate the testing of the web application https://www.guvi.in by simulating user actions and validating key UI functionalities. The system will interact with the web elements and execute test cases covering both positive and negative scenarios.
Test script is written using Selenium with Python and Pytest along with the Page Object Model framework(POM). It includes 10 detailed test cases  like verifying page behavior, accessibility of critical elements, navigation flows, and login and logout functionalities.

Project Architecture :

MiniProject1/   
├── Pages/        
│   ├── __init__.py
│   ├── base_page.py  
│   ├── login_page.py       
│   ├── home_page.py       
│
├── Tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_01_url.py        
│   ├── test_02_title.py    
│   ├── test_03_login_button.py     
│   ├── test_04_signup_button.py     
│   ├── test_05_signin.py     
│   ├── test_06_valid_login.py     
│   ├── test_07_invalid_login.py     
│   ├── test_08_menu_icons.py     
│   ├── test_09_dobby_assistant.py     
│   ├── test_10_logout.py        
│
├── Utils/
│   ├── config.py   
│   ├── __init__.py        
│
├── requirements.txt 
├── README.md  

Tools & Technologies:
Selenium WebDriver
Python 
Pytest
Page Object Model (POM)
Explicit Waits
Exception Handling
Pytest HTML Reports

Test Suite : 

Test Case 1: Check whether the URL https://www.guvi.in is valid or not.
	Positive case: Properly opens chrome and navigates to GUVI
	Negative case: Open Chrome but doesn’t navigate to GUVI


Test Case 2: Verify whether the title of the webpage is correct.
	Positive case: Exactly matches the title “GUVI | Learn to code in your native language”
	Negative case: Doesn’t match the given title and displays an error message.

Test Case 3:Login button visibility and clickability
	Assert login button is visible and interactable
	Clicking login button navigates to https://www.guvi.in/sign-in/

Test Case 4: SignUp button visibility and clickability
	Assert signup button is visible and interactable
	Clicking signup button navigates to https://www.guvi.in/register/

Test Case 5:  Navigation to the Sign-In page via the Sign-Up button.
	Clicking signup button navigates to https://www.guvi.in/register/
	Checks the redirected url matches the sign-in page.

Test Case 6: Login functionality with valid credentials.
	Enters valid email and password and clicks login button
	Enters the dashboard/profile page
	Check the dashboard url https://www.guvi.in/courses/?current_tab=myCourses

Test Case 7: Login functionality with invalid credentials.
	Enters invalid email and password and clicks login button
	Displays error message as “Incorrect username and password”

Test Case 8: Check menu items like “Courses”, “LIVE Classes”, and “Practice” are displayed.
	Checks  “Courses”, “LIVE Classes”, and “Practice” are visible and interactable.
	If menu items are not  found, exceptions are raised.

Test Case 9: Dobby Guvi Assistant is present on the page.
	Checks  Dobby Guvi Assistant is visible and interactable.

Test Case 10: Logout functionality
	Enters valid data and clicks login.
	Moves to dashboard page and clicks the profile menu
	Dropdown appears and clicks Sign out.
	After Sign out, it re-enters the login page again.

Instructions:

Ensure Selenium,Python and any Browser(Chrome,Firefox,Edge) installed in your system. 

To create a virtual environment,
>python -m venv venv

>Source venv/bin/activate(macOS)

>venv\scripts\activate(Windows)

To install the specific version,
	>pip install -r requirements.txt

To execute all the test files,
>pytest -v -s Tests/

>pytest pytest -v -s Tests/test_01_url.py(specific file)

>pytest pytest -v -s Tests/test_01_url.py::test_valid_url(specific method in a test file)


To Generate HTML Report:

To install pytest–html package
>pip install pytest–html

To execute all the test files and generate html report,
>pytest -v -s Tests/   --html = reports.html    --self-contained-html

To execute single file and generate html report,
>pytest -v -s Tests/test_01_url.py   --html = report1.html   --self-contained-html









