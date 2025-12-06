
from IPython.display import HTML, display

# Define the HTML content as a multiline Python string
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Portal - Fixed</title>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px; /* Line 11 is where the error appears when incorrectly parsed */
            background-color: #f5f5f5;
        }

        header {
            background-color: #3498db;
            color: white;
            padding: 15px;
            text-align: center;
        }

        nav ul {
            list-style: none;
            padding: 0;
            display: flex;
            justify-content: center;
            background-color: #2980b9;
        }

        nav ul li a {
            display: block;
            padding: 10px 20px;
            color: white;
            text-decoration: none;
        }

        main {
            padding: 20px;
        }

        footer {
            text-align: center;
            padding: 10px;
            background-color: #333;
            color: white;
        }
    </style>
</head>
<body>

    <header>
        <h1>Student Info Portal</h1>
    </header>

    <nav>
        <ul>
            <li><a href="#" onclick="showPage('Home')">Home</a></li>
            <li><a href="#" onclick="showPage('Grades')">Grades</a></li>
            <li><a href="#" onclick="showPage('Schedule')">Schedule</a></li>
        </ul>
    </nav>

    <main>
        <h2>Welcome to Your Portal</h2>
        <p>This is the central area for all your student information.</p>
        <button onclick="showPage('Test')">Click for Test</button>
    </main>

    <footer>
        <p>&copy; 2025 Student Portal</p>
    </footer>

    <script>
        function showPage(pageName) {
            alert('Loading ' + pageName + ' page.');
        }
    </script>
</body>
</html>
"""

# Use IPython.display.HTML to tell the cell to render the string as an HTML document
display(HTML(html_code))
Student Portal - Fixed
Student Info Portal
Home
Grades
Schedule
Welcome to Your Portal
This is the central area for all your student information.

© 2025 Student Portal
