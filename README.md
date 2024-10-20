3-Tier Rule Engine Application

https://github.com/user-attachments/assets/a90558c3-4d56-4d94-994c-feb03f467645




![image](https://github.com/user-attachments/assets/1862955f-780a-41aa-a1b7-18ca281314d9)
![image](https://github.com/user-attachments/assets/c46a5d71-27c1-40b6-8a90-3480eaba9a0a)

🚀 Overview
This 3-tier rule engine application enables dynamic rule creation, evaluation, and modification using Abstract Syntax Trees (AST). The system is designed to determine user eligibility based on attributes such as age, department, income, and experience, by parsing conditional logic into a tree structure. It provides an intuitive UI to allow rule input and evaluation, with a Flask backend handling rule creation and evaluation.

🧠 Theory Behind the Rule Engine
A rule engine is a system that applies business logic and decision-making processes using conditional rules. In this application, rules are represented using AST (Abstract Syntax Trees), a data structure that breaks down expressions into hierarchical trees. AST is useful for representing logical conditions as it allows for dynamic creation, combination, and modification of rules.

How it Works:
Rule Creation: Rules like "age > 30 AND department = 'Sales'" are parsed and transformed into an AST.
AST Representation: The AST represents the logical structure of the rule, with operator nodes (AND, OR) and operand nodes (conditions like age > 30).
Rule Evaluation: User data is compared against the rules by traversing the AST, and the system evaluates whether the user meets the defined conditions.

Abstract Syntax Tree (AST) Breakdown:

Consider the rule:

(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')
This would generate an AST like this:

Shell
Code
        
        OR
       /  \

     AND  AND

    /   \ /   \


 age>30 dept='Sales' age<25 dept='Marketing'


The system evaluates these rules by recursively checking each condition from the AST and returns True if the user data matches the rule, False otherwise.

🖥️ Tech Stack
This project is built using the following technologies:

Frontend:
HTML: For structuring the UI elements.

CSS: For styling the UI, using modern design techniques with vibrant colors and smooth transitions.

JavaScript: For handling frontend interactions, such as user input and sending requests to the backend.

Backend:
Flask: A lightweight Python web framework that handles the API logic for creating, combining, and evaluating rules.

✨ Features

Dynamic Rule Creation: Define complex logical rules using simple text input and translate them into AST.

Rule Combination: Combine multiple rules into one while optimizing the overall structure.

Real-time Rule Evaluation: Evaluate user data against dynamically created rules through an interactive interface.

Error Handling: Provides clear feedback for invalid rule syntax or JSON data input.

User-Friendly UI: Responsive design with a modern color palette and smooth 3D transitions for a great user experience.

🌐 API Endpoints
1. Create Rule
Endpoint: /create_rule
Method: POST
Request Body:
json
Copy code
{
  "rule_string": "age > 30 AND department = 'Sales'"
}
Response:
json
Copy code
{
  "ast": { ... }
}
2. Evaluate Rule
Endpoint: /evaluate_rule
Method: POST
Request Body:
json
Copy code
{
  "user_data": { "age": 35, "department": "Sales", "salary": 60000, "experience": 3 },
  "ast": { ... }
}
Response:
json
Copy code
{
  "result": true
}
📦 Project Setup

🛠️ Prerequisites

Python 3.x installed on your machine.

Flask installed. Run the following command to install Flask:

pip install flask

📦 Installation

Clone the repository:

git clone https://github.com/Dilip-code584/Rule-Engine-with-AST.git

cd rule-engine-ast

Install dependencies:
Flask
Python3 


Run the application:
python3 app.py 
or just 
flask run
Access the UI: Navigate to http://localhost:5000 in your browser to access the Rule Engine UI.

🧪 Test Cases
Create Rule: Test rule creation using strings like "age > 30 AND department = 'Sales'" and verify their AST structure.
Evaluate Rule: Test rule evaluation with various sample JSON data, ensuring the rules return accurate results.
Invalid Input Handling: Test error handling for incorrect rule strings or JSON formats.
Combine Rules: Test combining multiple rules and verify the resulting AST.

🎉 Bonus Features
Modification of Rules: Allows editing existing rules by changing operators, operand values, or adding/removing conditions.
Validations: Ensures input attributes (e.g., age, department) are part of a predefined catalog.
Advanced Conditions: The system can be extended to support user-defined functions for more advanced logic, such as custom eligibility conditions.

Security Points:
Input Validation and Sanitization:

Ensure that user inputs for creating or evaluating rules are properly validated and sanitized to prevent malicious input.
Use libraries like Flask-WTF or Python’s built-in validation to check inputs.
Secure Communication:

Implement HTTPS for all communications between the frontend and backend, especially if the system is accessed over a network.
Consider using tools like Flask-Talisman to enforce secure HTTP headers.
Authentication and Authorization:

Secure access to sensitive API endpoints (e.g., /create_rule, /evaluate_rule) by implementing user authentication and role-based access control (RBAC).
Consider using Flask-JWT-Extended for managing secure user sessions with JWT tokens.
Rate Limiting:

Implement rate limiting to prevent abuse of your endpoints, especially /evaluate_rule, which could be a target for brute-force attacks.
Prevent Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF):

Ensure that the frontend is protected against XSS by escaping HTML content.
Use Flask-WTF or Flask-SeaSurf for CSRF protection to secure forms and API requests.
Sensitive Data Handling:

If any sensitive user data is involved, ensure that it’s securely stored using encryption and handled according to best practices for data privacy.
Error and Exception Handling:

Provide detailed error messages for the development environment, but hide detailed system information in production. Use Flask-RESTful or Flask-Error to handle errors gracefully.
Environment Variable Management:

Store sensitive keys (e.g., database credentials) in environment variables instead of hardcoding them in the source code. Use .env files with tools like python-dotenv.
Performance Points:
Efficient AST Parsing:

Optimize the AST generation and evaluation logic by using efficient parsing libraries (e.g., lark-parser) and avoid creating deep or unnecessarily complex trees that can slow down evaluation.
Concurrency:

Use asynchronous request handling to improve performance, especially if the system is expected to handle multiple rule evaluations concurrently. Tools like Flask-Async can be used for this.
Data Caching:

Cache frequently evaluated rules to avoid re-generating and re-evaluating the AST for every request. Use a caching library like Flask-Caching with in-memory cache systems like Redis for better performance.
Database Optimization:

If the application stores rule data, ensure that the database schema is well-indexed for fast retrieval and avoid redundant data operations. Use a relational database like PostgreSQL and optimize queries.
Load Balancing:

If the application scales and has multiple users, consider implementing load balancing to distribute traffic across different servers for better performance.
Batch Processing:

For multiple rule evaluations, batch process requests to avoid blocking or overwhelming the system with a large number of requests at once.
Frontend Optimization:

Minimize frontend requests and assets (CSS/JS) to reduce the load on the server. Compress images and enable HTTP/2 for faster asset delivery.
Use lazy loading and preloading strategies to optimize page load times.
Asynchronous Task Processing (Optional):

Offload heavy tasks (e.g., combining multiple complex rules) to background workers using Celery or Flask-Executor.



🤝 Contributions
All contributions are welcome! Fork the repository, make your changes, and submit a pull request.

📝 License
This project is licensed under the MIT License. See the LICENSE file for more details.

📬 Contact
For any questions or feedback, feel free to contact:

Email: dilipsagarm@gmail.com
GitHub: (https://github.com/Dilip-code584)



Please run it via virtual env(ubuntu)(if encountering problems)
Steps -
1)python3 -m venv venv
2)source venv/bin/activate
