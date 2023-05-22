# Assessment Instructions

There are two parts to this assessment as follows;

- **Part I:** Write a security issues analysis report (600 words)
- **Part II:** Implementation

## Scenario

GoNZ provides New Zealand tourism services for travelers from around the world. The company wants to create a professional and responsive web application with a rich UI. After a thorough discussion amongst the Design Team, Development Team and product owner, they decide to build the application using Django.

As a junior developer, you received the below tasks from a senior member John:

### Part I: Write a security issues analysis report (600 words)

In this report, you need to analyse potential web application issues that this application may face, and then propose solutions to these issues based on the web application security standards. In addition, you also need to explain how to enhance privacy perfection against data collecting.

### Part II: Implementation

Some initial work (https://classroom.github.com/a/WXMHb7B6 Links to an external site.) has been done to create this application for the GoNZ company. Department and staff information in this company are given as below:

#####Departments deputies:

- **Administrators** look after this web application. They should have full permissions, including modifying any users and tour data.
- **Agents** can provide and modify their personal information. They should also have permission to add a tour and modify the information of an existing tour (NOTE: Agents should only be able to alter the information of a tour running by themselves).
- **Managers** should be able to modify the information of all agents and tours.

| Name               | Position             | Department    |
| ------------------ | -------------------- | ------------- |
| Haywood Luby       | System Administrator | Administrator |
| Mariah Schumaker   | Technical Director   | Administrator |
| Marty Schaeffer    | Senior Agent         | Agent         |
| Beryl Gauer        | Senior Agent         | Agent         |
| Cathrine Heckstall | Agent                | Agent         |
| Dane Ratliff       | Agent                | Agent         |
| Halina Dabbs       | Managing Director    | Management    |
| Andres Peltier     | Area Manager         | Management    |

#### Task 2a: Authentication.

Create an admin superuser (you should give a robust and secure password)
Create users and user groups based on the above staff and department information
Set up “signup” and “login” views for this application

#### Task 2b: Create the URLs listed below.

/ - home page
tours/ - tours page (list all tours in the application)
tours/<tour_id>/ - page for a single tour with the specified ID (primary key)
agents - agents page (list all agents in the application)
agents/<agent_id> - page for a single agent with the specified ID (primary key)

#### Task 2c: Authorisation.

Set up users and group permissions as per the department deputy list provided above.

#### Task 3: User experience.

Users can access all the pages they should have access to through the application, and the navigation through the pages is logical.
