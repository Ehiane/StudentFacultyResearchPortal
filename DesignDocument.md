# Design Document

## Your Project Title
--------
Prepared by:

* `Will Rae`,`Team Sioux`
* `Ehiane Oigiagbe`,`Team Sioux`
* `Cole Logan`,`Team Sioux`
---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay

---

## Table of Contents
- [Design Document](#design-document)
  - [Your Project Title](#your-project-title)
  - [Table of Contents](#table-of-contents)
    - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
- [2.	Architectural and Component-level Design](#2architectural-and-component-level-design)
  - [2.1 System Structure](#21-system-structure)
  - [2.2 Subsystem Design](#22-subsystem-design)
    - [2.2.1 Model](#221-model)
    - [2.2.2 Controller](#222-controller)
    - [2.2.3 View and User Interface Design](#223-view-and-user-interface-design)
- [3. Progress Report](#3-progress-report)
- [4. Testing Plan](#4-testing-plan)
- [5. References](#5-references)
- [Appendix: Grading Rubric](#appendix-grading-rubric)

<a name="revision-history"> </a>

### Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2021-10-05 |Initial draft | 1.0 |
|Revision 2 |2023-11-07 |First Revision| 2.0 |
|      |      |         |         |


# 1. Introduction

The purpose of this design document is to serve as a comprehensive guide for the development of the "Online Faculty Research Connection Platform," ensuring alignment with project requirements, providing documentation of design decisions, and facilitating effective communication among stakeholders. If this document is a revision of an earlier version, a brief summary of the changes made during the revision will be included to track the project's evolution and maintain transparency.


### Project Description:

The "Online Faculty Research Connection Platform" is a web-based solution designed to bridge the gap between faculty members and undergraduate students within an academic institution. This platform will provide a centralized online space where faculty members can post research positions and seamlessly connect with qualified undergraduate students seeking research opportunities. Students, in turn, will have the ability to submit their contact information, academic backgrounds, research interests, and prior research experience. The platform's primary objective is to facilitate efficient communication, collaboration, and research team formation within the academic community. It aims to simplify the process of matching students with research opportunities, enhancing transparency, and ultimately contributing to the advancement of academic research.

### Project Goal:

The primary goal of the "Online Faculty Research Connection Platform" is to create a user-friendly and efficient online interface that streamlines the connection between faculty members and undergraduate students for research collaborations. The key objectives and goals of the project include:

1. **Enhancing Accessibility:** To make research opportunities easily accessible to undergraduate students, ensuring they can readily find and apply for positions that align with their academic interests and skills.

2. **Efficient Matching:** To provide faculty members with tools that simplify the process of finding and selecting qualified student researchers, thus enhancing the efficiency of forming research teams.

3. **Transparency:** To improve the transparency of the research matching process, allowing both students and faculty to monitor the progress of their applications and postings, thereby fostering trust and accountability.

By achieving these goals, the project aims to foster a more collaborative and dynamic research environment within the academic institution.


# 2.	Architectural and Component-level Design
## 2.1 System Structure

This section should describe the high-level architecture of your software:  i.e., the major subsystems and how they fit together. 
If you adopted the application structure we used in the Smile App, your application would have the Model-View-Controller (MVC) pattern. If you adopted a different architectural pattern, mention the pattern you adopted in your software and briefly discuss the rationale for using the proposed architecture (i.e., why that pattern fits well for your system).

In this section:
 * Provide a UML component diagram that illustrates the architecture of your software.
 * Briefly mention the role of each subsystem in your architectural design. 
 * Discuss the rationale for the proposed decomposition in terms of  coupling and re-use.

## 2.2 Subsystem Design 

(**Note1**: This is just a suggested template. If you adopted a pattern other than MVC, you should revise this template and the list the major subsystems in your architectural design.)

(**Note2**: You should describe the design for the end product (completed application) - not only your iteration1 version. You will revise this document in iteration-2 and make changes  and/or add more details in iteration-2.)

### 2.2.1 Model

Briefly explain the role of the model. 

(***iteration-1***) 
| Model: | Position |
| -- |--|
| Role: | Holds all relevant information pertaining to each individual position, such as title, description, timecommitment, etc. |
| Attributes: | id, title, startDate, endDate, timeCommitment, *fields*, *experiences*, qualifications, facultyName, facultyContact, *applications* |
| Relationships: | fields: Many-to-Many relationship, each position can have many fields, likewise, the fields can have have many positions they are connected to. experiences: Many-to-Many relationship, each position can have many experiences, likewise, the experiences can have have many positions they are connected to. applications: One-to-Many: Each position can have many applications, but each application can only go to one position. |
| Notes: | This model additionally has 3 functions for each of the relationships, get_experiences, get_fields, and get_applications, all return a list of all that are connected to the position. |

| Model: | Application |
| -- |--|
| Role: | Holds information relevant to each application connected to a posted research position. |
| Attributes: | id, *position_id*, statement, referenceName, referenceEmail |
| Relationships: | position_id: serves as Table connecting each application to a position in a Many-to-One relationship, each position can have multiple applications. |
| Notes: | text |

| Model: | Experience |
| -- |--|
| Role: | All experiences in the application are part of this model to allow faculty users to add more as they see fit if an experience isn't already available to include in their position post. |
| Attributes: | id, name, *positions* |
| Relationships: | positions: serves as connection in Many-to-Many relationship with each position, allowing every experience to be part of many different position posts. |
| Notes: | additionally includes __repr__ function for printing on form. |

| Model: | Field |
| -- |--|
| Role: | All research fields in the application are part of this model to allow faculty users to add more as they see fit if an research field isn't already available to include in their position post. |
| Attributes: | id, name, *positions* |
| Relationships: | positions: serves as connection in Many-to-Many relationship with each position, allowing every field to be part of many different position posts. |
| Notes: | additionally includes __repr__ function for printing on form. |

| Model: | User |
| -- |--|
| Role: | Serves as base for both Faculty and Student models in the program. |
| Attributes: | id, username, password_hash, firstName, lastName, wsuID, email, phone, **student**, **faculty** |
| Relationships: | student: Serves as relationship for One-to-One connection between a User and Student. facuty: Serves as relationship for One-to-One connection between a User and Faculty. (**Note: not yet implemented, subject to change**) |
| Notes: | Model also includes functions for getting/setting the password, as well as checking the password and printing user info. |

| Model: | Faculty |
| -- |--|
| Role: | Serves as model for additional faculty information built upon the user model. |
| Attributes: | id, department, **user** |
| Relationships: | user: relateds faculty to user base model. (**Note: not yet implemented, subject to change**) |
| Notes: | N/A |

| Model: | Student |
| -- |--|
| Role: | Serves as model for additional student information built upon the user model. |
| Attributes: | id, GPA, grad_date, **user**, *experiences*, *fields* |
| Relationships: | user: relateds faculty to user base model. (**Note: not yet implemented, subject to change**). experiences: allows user to select from the existing list of experiences to add to their profile, helpful for faculty viewing when they apply for a position. fields: allows the user to select from the existing list of research fields to add to their profile, used for viewing related positions on "View Positions" page. |
| Notes: | N/A |

(***in iteration -2***) Revise the database model. Provide a UML diagram of your database model showing the associations and relationships among tables. Your UML diagram should also show the methods of your models.

### 2.2.2 Controller

Briefly explain the role of the controller. If your controller is decomposed into smaller subsystems (similar to the Smile App design we discussed in class), list each of those subsystems as subsections. 

For each subsystem:
 * Explain the role of the subsystem (component) and its responsibilities.
 * 	Provide a detailed description of the subsystem interface, i.e., 
    * which other subsystems does it interact with?  
    * what are the interdependencies between them? 


(***iteration-1***)
|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
| 1. | Register as Faculty | auth.facultyRegistration | Allows the user to access the faculty registration page and create a new faculty account, upon creation they are redirected to the faculty login page. |
| 2. | Sign in as Faculty | auth.facultyLogin | Allows previously registered faculty users to sign in using previously created log in credentials, system assigns current_user attributes to the created user/faculty accounts (objects). Upon sign in, they are redirected to the faculty home page. |
| 3. | Register as Student | auth.studentRegistration | Allows the user to access the student registration page and create a new student account, upon creation they are redirected to the student login page. |
| 4. | Sign in as Student | auth.studentLogin | Allows previously registered student users to sign in using previously created log in credentials, system assigns current_user attributes to the created user/student accounts (objects). Upon sign in, they are redirected to the student home page. |
| 5. | Faculty Post Position | routes.postposition | Allows logged in faculty users to create a new position using the post position form. Created forms are then posted to the "View Positions" page, allowing students to apply to them. |
| 6. | Student Apply for Position | routes.application | Allows student user to apply to post using the application form, upon submission the application is viewable to them in a "View Application" page, as well as to the faculty user who posted the position. |
| 7. | Faculty add Experience | routes.addexperience | Allows faculty users to add an experience to the database that can be used in the creation of their positions. Helpful for positions that are unique with experiences that aren't currently part of the database. |
| 8. | Faculty add Research Field | routes.addfield | Allows faculty users to add a research field to the database that can be used in the creation of their positions. Helpful for positions that are unique with research fields that aren't currently part of the database. |
| 9. | Faculty delete Position | routes.deleteposition | Allows logged in faculty members with previously created positions to delete them at their own discretion. A fauclty member can only delete their own posts. |
| 10. | Student can view open Positions | routes.index | Allows student users to view all open research positions and apply for them. The user can additionally filter the positions by their previously selected research interests. |
| 11. | Student can Withdraw Applications | routes.studentwithdraw/<position_id> | A student user with previously created applications can indicate they want to withdraw an application, allowing them to delete it from the positions application pool.  |
| 12. | Faculty can view applications to a created position. | routes.positionapplications/<application_id> | A faculty user with a previously created position with applications already submitted by student users can view information about the applications submitted.|
| 13. | Faculty can view information on Student Users that have applied to their positions | routes.viewstudent/<student_id> | A faculty user with a previously created position with applications already submitted by student users can view information about the applicants based on their student profile. |
| 14. | Faculty member can change the status of a student application. | routes.changestatus/<application_id> | A faculty user with a previously created position with applications already submitted by student users can change the status of multiple applications to "Approved for Interview". |
| 15. | Faculty member can indicate whether an approved student has been "Hired" or "Not Hired" | routes.hirestudent/<application_id> | A faculty user with a previously created position with applications already submitted and approved by student users can change the status of the students application to either "Hired" or "Not Hired". |

(***in iteration-2***) Revision

|   | Methods           | URL Path   | Description  |
|:--|:------------------|:-----------|:-------------|
| 1. | Register as Faculty | auth.facultyRegistration | Allows the user to access the faculty registration page and create a new faculty account, upon creation they are redirected to the faculty login page. |
| 2. | Sign in as Faculty | auth.facultyLogin | Allows previously registered faculty users to sign in using previously created log in credentials, system assigns current_user attributes to the created user/faculty accounts (objects). Upon sign in, they are redirected to the faculty home page. |
| 3. | Register as Student | auth.studentRegistration | Allows the user to access the student registration page and create a new student account, upon creation they are redirected to the student login page. |
| 4. | Sign in as Student | auth.studentLogin | Allows previously registered student users to sign in using previously created log in credentials, system assigns current_user attributes to the created user/student accounts (objects). Upon sign in, they are redirected to the student home page. |
| 5. | Faculty Post Position | routes.postposition | Allows logged in faculty users to create a new position using the post position form. Created forms are then posted to the "View Positions" page, allowing students to apply to them. |
| 6. | Student Apply for Position | routes.application | Allows student user to apply to post using the application form, upon submission the application is viewable to them in a "View Application" page, as well as to the faculty user who posted the position. |
| 7. | Faculty add Experience | routes.addexperience | Allows faculty users to add an experience to the database that can be used in the creation of their positions. Helpful for positions that are unique with experiences that aren't currently part of the database. |
| 8. | Faculty add Research Field | routes.addfield | Allows faculty users to add a research field to the database that can be used in the creation of their positions. Helpful for positions that are unique with research fields that aren't currently part of the database. |
| 9. | Faculty delete Position | routes.deleteposition | Allows logged in faculty members with previously created positions to delete them at their own discretion. A fauclty member can only delete their own posts. |
| 10. | Student can view open Positions | routes.index | Allows student users to view all open research positions and apply for them. The user can additionally filter the positions by their previously selected research interests. |
| 11. | Student can Withdraw Applications | routes.studentwithdraw/<position_id> | A student user with previously created applications can indicate they want to withdraw an application, allowing them to delete it from the positions application pool.  |
| 12. | Faculty can view applications to a created position. | routes.positionapplications/<application_id> | A faculty user with a previously created position with applications already submitted by student users can view information about the applications submitted.|
| 13. | Faculty can view information on Student Users that have applied to their positions | routes.viewstudent/<student_id> | A faculty user with a previously created position with applications already submitted by student users can view information about the applicants based on their student profile. |
| 14. | Faculty member can change the status of a student application. | routes.changestatus/<application_id> | A faculty user with a previously created position with applications already submitted by student users can change the status of multiple applications to "Approved for Interview". |
| 15. | Faculty member can indicate whether an approved student has been "Hired" or "Not Hired" | routes.hirestudent/<application_id> | A faculty user with a previously created position with applications already submitted and approved by student users can change the status of the students application to either "Hired" or "Not Hired". |


## 2.2.3 View and User Interface Design

The view in our "Online Faculty Research Connection Platform" plays a critical role in presenting the information and functionality of the system to both faculty members and undergraduate students. It serves as the user's gateway to interact with the platform and facilitates efficient communication and collaboration between these user groups.

### Technology Stack:

- **Web Framework**: We will utilize Flask as our web framework to handle routing, request handling, and interactions between the front-end and back-end components.

- **Back-End Technologies**: Python will be the primary programming language for the back-end, and we will use SQLAlchemy as an Object-Relational Mapping (ORM) tool for interacting with our database.

- **Front-End Technologies**: For the view, we will use HTML for page structure and content, and CSS for styling the user interfaces. Additionally, JavaScript will be employed for enhancing interactivity and user experience.

- **Responsive Design**: To ensure a seamless user experience across devices, we will implement responsive and mobile-friendly design using the Bootstrap framework.

Certainly, here's a more refined and structured presentation of the page templates you plan to use in your project:

### Page Templates:

Within our project, we have a set of HTML templates that play essential roles in shaping the user experience and facilitating various interactions:

1. **`position.html`**: This template is designed to display detailed information about available research positions, providing users with comprehensive insights into the opportunities.

2. **Error Files (`404error.html` and `500error.html`)**: These templates are dedicated to handling error messages, ensuring users are informed and guided in case of unexpected issues or page not found errors.

3. **`addexperience.html`**: This form template empowers users to enrich their profiles by adding relevant research experience, enhancing their suitability for the positions they are applying to.

4. **`base.html`**: Serving as the navigational hub, this template provides consistent navigation elements and links that are accessible across all pages, ensuring a unified and user-friendly experience.

5. **`login.html`**: This page template is dedicated to existing users, offering them a sign-in gateway to access their accounts and engage with the platform.

6. **`register.html`**: For new users, this template provides a user-friendly registration page, allowing them to create accounts and gain access to the platform's features.

7. **`create.html`**: This form template is responsible for collecting and organizing information about research positions, facilitating the creation and management of opportunities.

8. **`addfield.html`**: Designed to offer flexibility in research fields, this template empowers users to add additional research categories, enriching the diversity of opportunities.

9. **`application.html`**: This page template is designed for prospective applicants interested in research positions.

10. **`facultyInfo.html`**: This page template displays the contact information of faculty incharge of a position. 

11. **`facultyRegister.html`**: This page template is dedicated to faculty members who wish to register with the organization. It provides a user-friendly form for faculty to enter their registration details, including personal information, contact details, and login credentials, facilitating their registration process within the institution.

12. **`index.html`**: This page template serves as the welcoming interface for users of the website. It prominently displays a welcoming message and a list of available positions within the project.

13. **`studentRegister.html`**: This page template is designed for students who want to register inorder to apply for positions. 

These templates collectively shape the user interface and interaction within the "Online Faculty Research Connection Platform," ensuring a seamless and intuitive experience for both students and faculty members.


### Use-Cases Utilizing these Interfaces:

[Include the use-cases from your "Requirements Specification" document that will utilize these interfaces for user interaction as previously mentioned.]

By providing this additional information, you have a clear technology stack and can convey a more detailed picture of how the view and user interfaces will be built in your project. This helps project stakeholders understand the tools and frameworks you plan to use and how they will contribute to the development of the platform.


# 3. Progress Report

Write a short paragraph summarizing your progress in iteration1 / iteration2.

# 4. Testing Plan
(***in iteration 2***)
In this section , provide a brief description of how you plan to test the system. Thought should be given to mostly how automatic testing can be carried out, so as to maximize the limited number of human hours you will have for testing your system. Consider the following kinds of testing:
  * *Unit Testing*: Explain for what modules you plan to write unit tests, and what framework you plan to use.  (Each team should write automated tests (at least) for testing the routes)
  * *Functional Testing*: How will you test your system to verify that the use cases are implemented correctly? 
  * *UI Testing*: How do you plan to test the user interface?  (Manual tests are OK)

In our development plan, we aim to conduct unit testing for all the routes implemented in 'routes.py' and 'auth_routes.py.' This testing approach will be similar to the one employed in the 'smile app' project. For each route, we will simulate requests, navigate through the route, and then validate the response's status code to ensure it returns the expected 200 status code, indicating success. By thoroughly testing our routes, we can ensure that the core functionality of our web application is functioning as intended.

Additionally, we will extend our unit testing to cover the models defined in 'models.py.' Our tests will involve creating both student and faculty accounts and verifying their successful insertion into our database. We will also test the login process, ensuring that valid credentials grant access while incorrect ones are rejected. Further tests will include posting new positions using a faculty account, tracking changes in the database, and confirming the accuracy of the post's information. We will also test the application process, confirming that the number of applications in the database increases as expected, that application details are correct, and that both students and faculty members can access and view relevant application information. Finally, we will validate the functionality related to adding experiences and research topics by creating new entries and confirming their accurate addition to the database.


We will use both pytest and unittest to carry out these tests:
* Student applying to position
* Faculty member creating a position
* Log in
* Log out
* Adding new experience
* Adding new research fields

# 5. References

Cite your references here.

For the papers you cite give the authors, the title of the article, the journal name, journal volume number, date of publication and inclusive page numbers. Giving only the URL for the journal is not appropriate.

For the websites, give the title, author (if applicable) and the website URL.


----
# Appendix: Grading Rubric
(Please remove this part in your final submission)

These is the grading rubric that we will use to evaluate your document. 


|**MaxPoints**| **Design** |
|:---------:|:-------------------------------------------------------------------------|
|           | Are all parts of the document in agreement with the product requirements? |
| 10        | Is the architecture of the system described well, with the major components and their interfaces?  Is the rationale for the proposed decomposition in terms of cohesion and coupling explained well? |
| 15        | Is the document making good use of semi-formal notation (i.e., UML diagrams)? Does the document provide a clear and complete UML component diagram illustrating the architecture of the system? |
| 15        | Is the model (i.e., “database model”) explained well with sufficient detail? | 
| 10        | Is the controller explained in sufficient detail?  |
| 22        | Are all major interfaces (i.e., the routes) listed? Are the routes explained in sufficient detail? |
| 10        | Is the view and the user interfaces explained well? Did the team provide the screenshots of the interfaces they built so far.   |
| 5         | Is there sufficient detail in the design to start Iteration 2?   |
| 5         | Progress report  |
|           |   |
|           | **Clarity** |
|           | Is the solution at a fairly consistent and appropriate level of detail? Is the solution clear enough to be turned over to an independent group for implementation and still be understood? |
| 5         | Is the document carefully written, without typos and grammatical errors?  |
| 3         | Is the document well formatted? (Make sure to check your document on GitHub. You will loose points if there are formatting issues in your document.  )  |
|           |  |
|           | **Total** |
|           |  |
