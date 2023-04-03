# Programming_For_Information_Systems_Assignment
After observing a manual excel sheet being filled out and passed around in a group for the daily shift managements for the many part-time work employers, we made an effort to design a roaster management system.

- Roaster Management System
  An organisation can keep track of the number of hours their staff members put in, allocate them to particular jobs or projects,  using a roster management system. A Roster Management system can assist an organisation in ensuring that employees are working the right number of hours and that projects are being completed on schedule by tracking employee hours and assigning employees to particular assignments. A Roster Management system can also assist a company in identifying areas where workers may want more assistance or training.

- Technologies Used:
  i. Python Django: High-level Python web framework Django promotes quick development and streamlined, practical design. It was created by seasoned programmers   and handles a lot of the hassle associated with web development, freeing you up to concentrate on building your app without having to invent the wheel. It is   open source and free.
  ii. HTML: The preferred markup language for documents intended to be viewed in a web browser is HTML, or HyperText Markup Language. Technologies like           Cascading Style Sheets and scripting languages like JavaScript can improve the overall user experience.
  iii. CSS: Cascading Style Sheets is a language for creating style sheets that describe how a document presented in a markup language, such HTML or XML. The     World Wide Web's foundational technologies, along with HTML and JavaScript, include CSS.
  iv. Sqlite3:  SQLite is a database engine. It is a library that software designers incorporate into their apps rather than a stand-alone application.           Therefore, it is a member of the family of embedded databases.
  
- Workflow of the Application:
    We have defined two user roles, Admin and employee.To login as admin the crededntials are as follows: UserId:"admin", Password:"test". Admin has the        rights to add the employee and allocate and update shifts to the employees and search the employees.
    The employee as a user can login with the registered phone number and an otp which a random number generated will be displayed on the screen, and the         employee can login with it, login example for employee is as follows, Phone Number:"8985454545" and OTP displayed on the screen.Once logged in the           employee can view and update own profile information and can view the list of co-workers. 

Command to run the application: python manage.py runserver

- Individual contributions:

  - Staicy Androose (10611860): Contributed to databse and python part of the applicaiton.Explore sqlite and worked on implementiing the same by creating         schema and tables for the database.And worked on page routing with python.

  - Sumi Tharayil Surendran (10625856): Contributed with the database, collecting refrences and HTML part of the application. Gathered sample sites for the       refrences and designed a simple wireframe with the same. Worked on page creation in HTML as well.

  - Rucha Ganesh Saraf (1063130): Worked on HTML and CSS. Also explored and implemented the crispy forms used in the applicaiton for various instances.           Worked on user validations.

- Contents of the Project:

  Tables:
    - auth_user
    - src_employee
    - src_employee_profile
    - src_employee_shift
    - src_role_admin
    
   Pages:
    - base.html
    - signin.html
    - signin-emp.html
    - add_employee.html
    - add_shift.html
    - otp.html
    - profile.html
    - profile-update.html
    - shift_management.html

GITHUB link:
https://github.com/srucha20/Programming_For_Information_Systems_Assignment.git
    

