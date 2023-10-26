# Capacity Exchange Development: Django Bug Tracker

The main objective of this project is to get familiar with the basic structure of Django through a series of tasks.

## Task 1: Setting Up the Django Project

**Objective**: Create a Django project with an app called `bug` and commit it on GitHub.

### Steps:

1. Create an account on GitHub.
2. Read the first part of the [Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/) tutorial.
3. Create a Django project with an app called `bug`.
4. Commit your Django project to GitHub.
   
## Task 2: Structuring Database and Model Creation

**Objective**: Structure a SQLite database and create a Django model for the Bug app.

### Steps:

1. Read the second part of the [Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial02/) tutorial.
2. Create a `Bug` model with fields: "description", "bug_type", "report_date", "status".
3. Structure the database as described in the tutorial and create at least one bug through Django Admin.

## Task 3: Creating Views and Templates

**Objective**: Create views and templates to 
1) register and view a bug.
2) list all bugs registered.

### Steps:

1. Read the third and fourth parts of the [Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial03/) tutorial.
2. Create a view to register a bug into the database.
3. Design a simple HTML template with a form to add a bug to the database.
4. Develop another view to display the fields of the bug.
5. Design a template to list the bug fields.
6. Implement a view to list all the bugs.
7. Design a template with a list containing links to the detail page of each bug.

## Task 4: Automated Unit Testing

**Objective**: Create automated unit tests for the `bug` app.

### Steps:

1. Read the fifth part of the [Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial05/) tutorial.
2. Create at least four automated tests for the `bug` model.
3. Develop at least three automated tests for the `bug` views.
