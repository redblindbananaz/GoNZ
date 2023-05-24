# Project Documentation

## Installation:

Please make sure that you looked at the READ ME file in this project repository for the installation process.

## Set up:

- Create a Django Project: Once Django is installed, create a new Django project with the following command:

```
django-admin startproject GoNZ
```

- Go to directory:

```
cd GoNZ
```

- Start the Development Server: To test Django project locally, starting the development server with the following command:

```
python manage.py runserver
```

## Application:

Creation of two separate apps: one for handling the tours-related functionality and another for the agents-related functionality.

By separating the functionality into two apps, I can keep the codebase organized, maintain a clear separation of concerns, and easily manage and scale each feature independently. It also provides modularity and makes it easier to understand and maintain the codebase in the long run.

### Steps:

- **1. Basic Models and urls:**

* Creating the app ( home app will be hosting sign up and landing page and can be extended later for further functionalities)
* Register the App
* Create Models
* Migrate the database with makes migration and migrate
* Register the model in each app admin.py to access it in the admin panel.
* Create Views
* Create URLS
* Include app URLS
* Configure templates
* Design and functionalities

- **2. Groups, user and authentification:**
