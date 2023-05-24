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

* Creation of the super user:
* Creation of groups and users with passwords
* Need to extend the existing agent model to abstract user in order to assign permissions.

| Name               | Position             | Department    | Password          | Username               |
| ------------------ | -------------------- | ------------- | ----------------- | ---------------------- |
| Haywood Luby       | System Administrator | Administrator | R1@7jL!p          | haywood.luby_admin     |
| Mariah Schumaker   | Technical Director   | Administrator | P@ssw0rd123!      | mariah.schumaker_admin |
| Marty Schaeffer    | Senior Agent         | Agent         | Ag#nt2023         | marty.schaeffer_agent  |
| Beryl Gauer        | Senior Agent         | Agent         | G#uer!2023        | beryl.gauer_agent      |
| Cathrine Heckstall | Agent                | Agent         | C@thrine2023!     | cathrine.heckstall     |
| Dane Ratliff       | Agent                | Agent         | D@neR@tliff2023!  | dane.ratliff           |
| Halina Dabbs       | Managing Director    | Management    | DabbsM@n@ger2023! | halina.dabbs           |
| Andres Peltier     | Area Manager         | Management    | PeltierA#r3@2023! | andres.peltier         |
| ITAdmin            | IT                   | IT admin      | 123456            | ITAdmin                |

- Creating custom display for the damin panel for agent:

```
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Agent

# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'position')

admin.site.register(Agent, AgentAdmin)
```
