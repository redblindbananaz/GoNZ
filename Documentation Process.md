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

- Creating custom display for the admin panel for agent:

```
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Agent

# Register your models here.

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'position')

admin.site.register(Agent, AgentAdmin)
```

- Customize the admin panel:

```
# Adds site header, site title, index title to the admin side.
admin.site.site_header = 'GoNZ Admin'
admin.site.site_title = 'GONZ'
admin.site.index_title = 'Welcome GoNz Team'
```

- Create a login/sign up page:
  creation a login page then have a link to register:

  ```
    class HomeView(TemplateView):
        template_name = 'home/home.html'

    class LoginView(View):
        def get(self, request):
            return render(request, 'home/login.html')

        def post(self, request):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home')  # Replace 'tour-list' with the URL name of the tour list page
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('home:login')
  ```

* Need to create a sign up page and link it to the login page:

* Creation of agent details:
  modification of the View to filter the tour created by the agent:

```
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tours'] = Tour.objects.filter(agent=self.object)
        return context
```

`context = super().get_context_data(**kwargs)`: This line calls the parent class's get_context_data method to get the initial context data.
`context['tours'] = Tour.objects.filter(agent=self.object)`: This line adds an additional key-value pair to the context dictionary. The key is 'tours', and the value is the result of filtering the Tour objects based on the agent field, which is set to the current agent object (self.object).
`return context`: This line returns the updated context dictionary, which includes the tours related to the agent.

### Issues and bugs to fix:

- Pagination is not working as intented - **sorted** Django documentation
- Tour details when clicking on view details is not working- **solved** tempates was named tour_details.html and view, urls refers to tour_detail. with no s

* no active link indicator in tour details and also agent details.
* Would like to customise username to the name of the person
* If agent has no tour, display message, no tours available.
