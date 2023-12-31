# Running the Django REST API Endpoint

This document provides step-by-step instructions on how to run and use the Django REST API endpoint for managing persons.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed on your system:

- Python 3.x
- Django
- Django REST framework
- Postman (optional, for testing)

## Getting Started

1. Clone the repository containing your Django project to your local machine.

```bash
git clone [<repository_url>](https://github.com/Nazzcodek/person.git)

# Navigate to the project directory.
cd person

# Create and activate virtualenv
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make Migrations.
python manage.py makemigrations

# Apply database migrations.
python manage.py migrate

# Start the development server.
python manage.py runserver
```

# Using the API
1. Open your web browser or a tool like Postman.

2. Access the API overview to see available endpoints:

- Base URL: https://stage-two-naziff.onrender.com/person/
3. Perform CRUD operations:

- Create a new person:

    - Endpoint: https://stage-two-naziff.onrender.com/person/create/
    - Method: POST
    - Data: JSON object with a "name" field (e.g., {"name": "Mike Essien"})
- View all persons:

    - Endpoint: https://stage-two-naziff.onrender.com/person/all/
    - Method: GET
- Update a person:

    - Endpoint: https://stage-two-naziff.onrender.com/person/update/<int:pk>/
    - Method: POST
    - Data: JSON object with a "name" field (e.g., {"name": "Updated Name"})
- Delete a person:

    - Endpoint: https://stage-two-naziff.onrender.com/person/person/<int:pk>/delete/
    - Method: DELETE
- swagger documentation:

  - Endpoint:
    https://stage-two-naziff.onrender.com/swagger/
  
# Testing
You can use tools like Postman or use the API endpoints provided above.

# Conclusion
successfully set up and run Django REST API endpoint for managing persons. This API can now be use to create, view, update, and delete person records.
