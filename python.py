Q1--> Create a Flask application with the following static routes: i) / ii) /about iii) /contact Display an appropriate message on each webpage. 
flask_app/
│── app.py
│── templates/
    │── home.html
    │── about.html
    │── contact.html
app.py
from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

home.html

<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Home Page</h1>
    <p>This is the main page.</p>
</body>
</html>

about.html

<!DOCTYPE html>
<html>
<head>
    <title>About</title>
</head>
<body>
    <h1>About Us</h1>
    <p>This is the about page of the website.</p>
</body>
</html>

contact.html

<!DOCTYPE html>
<html>
<head>
    <title>Contact</title>
</head>
<body>
    <h1>Contact Us</h1>
    <p>Email: example@gmail.com</p>
</body>
</html>

for run
python app.py


Q2--> 2. Create a dynamic URL route using an integer parameter: /student/<int:roll_no>/<name> The route should accept the student’s roll number and name through the URL and display the student details in a structured format. 

app.py

from flask import Flask, render_template

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return "Welcome to Home Page"

# Dynamic Student Route
@app.route('/student/<int:roll_no>/<name>')
def student(roll_no, name):
    return render_template('student.html', roll_no=roll_no, name=name)

if __name__ == '__main__':
    app.run(debug=True)

students.html

<!DOCTYPE html>
<html>
<head>
    <title>Student Details</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            background-color: #f2f2f2;
        }
        .card {
            margin: 100px auto;
            padding: 20px;
            width: 300px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }
    </style>
</head>
<body>

    <div class="card">
        <h2>Student Details</h2>
        <p><strong>Roll No:</strong> {{ roll_no }}</p>
        <p><strong>Name:</strong> {{ name }}</p>
    </div>

</body>
</html>

RUN
python app.py

Q3-->Create a Flask application that stores an employee’s details (Employee ID, Name, Department, Basic Salary) in predefined variables, calculates HRA (20%), DA (12%), TA (8%), PF (10%), Gross Salary and Net Salary, and displays a salary slip on the home page. gross_salary = basic_salary + hra + da + ta net_salary = gross_salary - pf

flask_app/
│── app.py
│── templates/
    │── salary.html 

app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def salary_slip():
    # Predefined Employee Details
    emp_id = 101
    name = "Yash"
    department = "IT"
    basic_salary = 30000

    # Calculations
    hra = basic_salary * 0.20
    da = basic_salary * 0.12
    ta = basic_salary * 0.08
    pf = basic_salary * 0.10

    gross_salary = basic_salary + hra + da + ta
    net_salary = gross_salary - pf

    return render_template('salary.html',
                           emp_id=emp_id,
                           name=name,
                           department=department,
                           basic_salary=basic_salary,
                           hra=hra,
                           da=da,
                           ta=ta,
                           pf=pf,
                           gross_salary=gross_salary,
                           net_salary=net_salary)

if __name__ == '__main__':
    app.run(debug=True)


salary.html
<!DOCTYPE html>
<html>
<head>
    <title>Salary Slip</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f4f4f4;
        }
        .container {
            width: 400px;
            margin: 50px auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }
        h2 {
            text-align: center;
        }
        table {
            width: 100%;
        }
        td {
            padding: 8px;
        }
        .total {
            font-weight: bold;
            color: green;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Salary Slip</h2>
    
    <table>
        <tr><td>Employee ID:</td><td>{{ emp_id }}</td></tr>
        <tr><td>Name:</td><td>{{ name }}</td></tr>
        <tr><td>Department:</td><td>{{ department }}</td></tr>
        <tr><td>Basic Salary:</td><td>{{ basic_salary }}</td></tr>

        <tr><td>HRA (20%):</td><td>{{ hra }}</td></tr>
        <tr><td>DA (12%):</td><td>{{ da }}</td></tr>
        <tr><td>TA (8%):</td><td>{{ ta }}</td></tr>
        <tr><td>PF (10%):</td><td>{{ pf }}</td></tr>

        <tr class="total"><td>Gross Salary:</td><td>{{ gross_salary }}</td></tr>
        <tr class="total"><td>Net Salary:</td><td>{{ net_salary }}</td></tr>
    </table>
</div>

</body>
</html>

RUN
python app.py


Q4-->Create a Flask application to develop a dynamic product information page using URL routing. Create a dynamic URL route /product/<product_name>/<int:price>/<category> that accepts product details through the URL and displays the product name, price, category, discount amount(10%), GST (18%), and final price after calculation on the webpage. Test the application by accessing the URL with different product values through the browser and verify the output.

flask_app/
│── app.py
│── templates/
    │── product.html

app.py 

from flask import Flask, render_template

app = Flask(__name__)

# Dynamic Product Route
@app.route('/product/<product_name>/<int:price>/<category>')
def product(product_name, price, category):

    # Calculations
    discount = price * 0.10
    discounted_price = price - discount
    gst = discounted_price * 0.18
    final_price = discounted_price + gst

    return render_template('product.html',
                           product_name=product_name,
                           price=price,
                           category=category,
                           discount=discount,
                           gst=gst,
                           final_price=final_price)

if __name__ == '__main__':
    app.run(debug=True)

templates/product.html

<!DOCTYPE html>
<html>
<head>
    <title>Product Details</title>
    <style>
        body {
            font-family: Arial;
            background-color: #f2f2f2;
        }
        .container {
            width: 400px;
            margin: 80px auto;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0px 0px 10px gray;
        }
        h2 {
            text-align: center;
        }
        table {
            width: 100%;
        }
        td {
            padding: 8px;
        }
        .highlight {
            font-weight: bold;
            color: green;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Product Information</h2>

    <table>
        <tr><td>Product Name:</td><td>{{ product_name }}</td></tr>
        <tr><td>Category:</td><td>{{ category }}</td></tr>
        <tr><td>Original Price:</td><td>{{ price }}</td></tr>

        <tr><td>Discount (10%):</td><td>{{ discount }}</td></tr>
        <tr><td>GST (18%):</td><td>{{ gst }}</td></tr>

        <tr class="highlight">
            <td>Final Price:</td>
            <td>{{ final_price }}</td>
        </tr>
    </table>
</div>

</body>
</html>

RUN 
python app.py


Q5--> Create a Flask application with the following files: 
● base.html 
● home.html 
● employees.html 
● department.html 
Create employee data and use Jinja2 loops to display the records. Use conditional statements to categorize employees as Fresher, Experienced, or Senior based on experience. Use template inheritance and create a CSS file in static/css. Verify the application in the browser. 

flask_app/
│── app.py
│── static/
│    └── css/
│         └── style.css
│── templates/
│    │── base.html
│    │── home.html
│    │── employees.html
│    │── department.html

app.py
from flask import Flask, render_template

app = Flask(__name__)

# Employee Data
employees = [
    {"id": 1, "name": "Yash", "dept": "IT", "salary": 30000, "exp": 1},
    {"id": 2, "name": "Rahul", "dept": "HR", "salary": 40000, "exp": 3},
    {"id": 3, "name": "Amit", "dept": "Finance", "salary": 60000, "exp": 6},
    {"id": 4, "name": "Sneha", "dept": "IT", "salary": 80000, "exp": 10}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/employees')
def emp():
    return render_template('employees.html', employees=employees)

@app.route('/department')
def dept():
    return render_template('department.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)

static/css/style.css
body {
    font-family: Arial;
    background-color: #f2f2f2;
}

.navbar {
    background: #333;
    padding: 10px;
}

.navbar a {
    color: white;
    margin: 10px;
    text-decoration: none;
}

.container {
    width: 80%;
    margin: 20px auto;
    background: white;
    padding: 20px;
    border-radius: 10px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

td, th {
    padding: 10px;
    border: 1px solid #ddd;
}

th {
    background: #444;
    color: white;
}

templates/base.html

<!DOCTYPE html>
<html>
<head>
    <title>Employee App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

<div class="navbar">
    <a href="/">Home</a>
    <a href="/employees">Employees</a>
    <a href="/department">Department</a>
</div>

<div class="container">
    {% block content %}{% endblock %}
</div>

</body>
</html>

templates/home.html

{% extends 'base.html' %}

{% block content %}
<h2>Welcome to Employee Management System</h2>
<p>This is Home Page</p>
{% endblock %}

templates/employees.html
{% extends 'base.html' %}

{% block content %}
<h2>Employee List</h2>

<table>
<tr>
    <th>ID</th>
    <th>Name</th>
    <th>Department</th>
    <th>Salary</th>
    <th>Experience</th>
    <th>Category</th>
</tr>

{% for emp in employees %}
<tr>
    <td>{{ emp.id }}</td>
    <td>{{ emp.name }}</td>
    <td>{{ emp.dept }}</td>
    <td>{{ emp.salary }}</td>
    <td>{{ emp.exp }} years</td>

    <td>
        {% if emp.exp <= 2 %}
            Fresher
        {% elif emp.exp <= 5 %}
            Experienced
        {% else %}
            Senior
        {% endif %}
    </td>
</tr>
{% endfor %}

</table>
{% endblock %}


templates/department.html

{% extends 'base.html' %}

{% block content %}
<h2>Department Wise Employees</h2>

<ul>
{% for emp in employees %}
    <li>{{ emp.name }} - {{ emp.dept }}</li>
{% endfor %}
</ul>

{% endblock %}

RUNpython app.py

Q6-->Display Student Information using Jinja2 ,Create a Flask application with the following templates: base.html, home.html, student html .Create student data containing name, roll number, and course in app.py. Pass the data to student.html using Jinja2 variables and display the student information. Use template inheritance and create a CSS file in the static/CSS folder. Verify the output in the browser. 

flask_app/
│── app.py
│── static/
│    └── css/
│         └── style.css
│── templates/
│    │── base.html
│    │── home.html
│    │── student.html

app.py

from flask import Flask, render_template

app = Flask(__name__)

# Student Data
student = {
    "name": "Yash",
    "roll_no": 101,
    "course": "BCA"
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student')
def student_page():
    return render_template('student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
	
static/css/style.css

body {
    font-family: Arial;
    background-color: #f2f2f2;
}

.navbar {
    background: #333;
    padding: 10px;
}

.navbar a {
    color: white;
    margin: 10px;
    text-decoration: none;
}

.container {
    width: 60%;
    margin: 30px auto;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px gray;
}

h2 {
    text-align: center;
}

templates/base.html

<!DOCTYPE html>
<html>
<head>
    <title>Student App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

<div class="navbar">
    <a href="/">Home</a>
    <a href="/student">Student</a>
</div>

<div class="container">
    {% block content %}{% endblock %}
</div>

</body>
</html>

templates/home.html

{% extends 'base.html' %}

{% block content %}
<h2>Welcome to Student Information System</h2>
<p>This is Home Page</p>
{% endblock %}

templates/student.html

{% extends 'base.html' %}

{% block content %}
<h2>Student Details</h2>

<p><strong>Name:</strong> {{ student.name }}</p>
<p><strong>Roll Number:</strong> {{ student.roll_no }}</p>
<p><strong>Course:</strong> {{ student.course }}</p>

{% endblock %}


RUN

Q7-->Display HTML Template using Flask ,Create a Flask application with the following structure: templates/home.html Create a home.html template and display a ‘ welcome’ message using the render_template() function. Verify the output in the browser. 

flask_app/
│── app.py
│── templates/
    └── home.html

app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

templates/home.html

<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome</h1>
</body>
</html>

and run


Q8-->Display Course List using Jinja2 Loop, Create a Flask application with the following templates: base.html, home.html, courses.html, Create a list of five courses in app.py. Use a Jinja2 for loop to display the courses in courses.html. Use template 

flask_app/
│── app.py
│── static/
│    └── css/
│         └── style.css
│── templates/
│    │── base.html
│    │── home.html
│    │── courses.html


app.py

	from flask import Flask, render_template

app = Flask(__name__)

# Course List
courses = ["Python", "Java", "Web Development", "Data Science", "Machine Learning"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/courses')
def course_page():
    return render_template('courses.html', courses=courses)

if __name__ == '__main__':
    app.run(debug=True)

static/css/style.css

body {
    font-family: Arial;
    background-color: #f2f2f2;
}

.navbar {
    background: #333;
    padding: 10px;
}

.navbar a {
    color: white;
    margin: 10px;
    text-decoration: none;
}

.container {
    width: 60%;
    margin: 30px auto;
    background: white;
    padding: 20px;
    border-radius: 10px;
}

ul {
    list-style-type: none;
}

li {
    padding: 10px;
    background: #ddd;
    margin: 5px 0;
}

templates/base.html

<!DOCTYPE html>
<html>
<head>
    <title>Course App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

<div class="navbar">
    <a href="/">Home</a>
    <a href="/courses">Courses</a>
</div>

<div class="container">
    {% block content %}{% endblock %}
</div>

</body>
</html>

templates/home.html

{% extends 'base.html' %}

{% block content %}
<h2>Welcome to Course Portal</h2>
<p>This is Home Page</p>
{% endblock %}



templates/courses.html

{% extends 'base.html' %}

{% block content %}
<h2>Welcome to Course Portal</h2>
<p>This is Home Page</p>
{% endblock %}

templates/courses.html
{% extends 'base.html' %}

{% block content %}
<h2>Course List</h2>

<ul>
    {% for course in courses %}
        <li>{{ course }}</li>
    {% endfor %}
</ul>

{% endblock %}

run
python app.py

Q9-->
Student Result using Jinja2 Conditional Statements ,Create a Flask application with the following templates:base.html,home.html,result.html .Create student name and percentage in app.py. Use Jinja2 conditional statements to display the result as Distinction, First Class, Second Class, Pass, or Fail according to the percentage. Use template inheritance and create a CSS file in the static/CSS folder. Verify the output in the browser. 

flask_app/
│── app.py
│── static/
│    └── css/
│         └── style.css
│── templates/
│    │── base.html
│    │── home.html
│    │── result.html


app.py

from flask import Flask, render_template

app = Flask(__name__)

# Student Data
student = {
    "name": "Yash",
    "percentage": 78
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result')
def result():
    return render_template('result.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)

static/css/style.css

body {
    font-family: Arial;
    background-color: #f2f2f2;
}

.navbar {
    background: #333;
    padding: 10px;
}

.navbar a {
    color: white;
    margin: 10px;
    text-decoration: none;
}

.container {
    width: 60%;
    margin: 30px auto;
    background: white;
    padding: 20px;
    border-radius: 10px;
}

.result {
    font-weight: bold;
    color: green;
    font-size: 20px;
}


templates/base.html

<!DOCTYPE html>
<html>
<head>
    <title>Student Result</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

<div class="navbar">
    <a href="/">Home</a>
    <a href="/result">Result</a>
</div>

<div class="container">
    {% block content %}{% endblock %}
</div>

</body>
</html>


templates/home.html

{% extends 'base.html' %}

{% block content %}
<h2>Welcome to Result System</h2>
<p>Click on Result to view student performance</p>
{% endblock %}


templates/result.html

{% extends 'base.html' %}

{% block content %}
<h2>Student Result</h2>

<p><strong>Name:</strong> {{ student.name }}</p>
<p><strong>Percentage:</strong> {{ student.percentage }}%</p>

<p class="result">
    Result:
    {% if student.percentage >= 75 %}
        Distinction
    {% elif student.percentage >= 60 %}
        First Class
    {% elif student.percentage >= 50 %}
        Second Class
    {% elif student.percentage >= 40 %}
        Pass
    {% else %}
        Fail
    {% endif %}
</p>

{% endblock %}

and then run 



Q10-->10. Apply CSS Styling using Static Folder . Create a Flask application with the following structure: templates/home.html and static/CSS/style.css .Create a home.html template and apply CSS styling using the style.css file in the static/CSS folder. Apply simple styling to the heading, paragraph, background, and text alignment. Verify the output in the browser.


flask_app/
│── app.py
│── static/
│    └── css/
│         └── style.css
│── templates/
│    └── home.html

app/py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)


🎨 static/css/style.css

body {
    background-color: #f2f2f2;
    text-align: center;
    font-family: Arial;
}

h1 {
    color: blue;
    margin-top: 50px;
}

p {
    color: #333;
    font-size: 18px;
}

🌐 templates/home.html

<!DOCTYPE html>
<html>
<head>
    <title>Home</title>

    <!-- Linking CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>

    <h1>Welcome</h1>
    <p>This is a styled Flask webpage using CSS.</p>

</body>
</html>


run
python app.py