# StudentFacultyResearchPortal (Term Project)
### Project Title: WSU Research Portal
### Team Name: Team Sioux 
### Team Members 
* Will Rae
* Cole Logan
* Ehiane Oigiagbe

`To run this application:` 
* open the terminal 
* run the following command(s):
```
flask run
```
or 
```
python project.py
```


#  User Interface
### Student main page & faculty main page:
<div style="display: flex;">
  <img width="960" alt="Screenshot 2024-01-02 173807" src="https://github.com/Ehiane/StudentFacultyResearchPortal/assets/79903725/2fad09de-15c9-4868-a988-f05829763ffb" style="width: 48%;">
  <img width="958" alt="Screenshot 2024-01-02 173746" src="https://github.com/Ehiane/StudentFacultyResearchPortal/assets/79903725/afde1836-9c2d-4d7b-896d-23e69bfd707f" style="width: 48%;">
</div>

### Login page & Registration page:
<div style="display; flex;">
  <img width="959" alt="Screenshot 2024-01-02 174336" src="https://github.com/Ehiane/StudentFacultyResearchPortal/assets/79903725/b22ece37-0033-4e2e-ba7f-f1c60ec6b851" style="width: 48%;">
  <img width="960" alt="Screenshot 2024-01-02 174306" src="https://github.com/Ehiane/StudentFacultyResearchPortal/assets/79903725/0e9a8bda-2b45-4e74-b97e-31a92cf8fdaf" style="width: 48%;">
</div>

## Features

- **Effortless Application Process**: Faculty members can effortlessly post research opportunities, including details on required experiences and additional research fields.

- **Intuitive Student Interface**: Students can explore a variety of research opportunities, select the projects that resonate with them, and submit applications seamlessly through an intuitive user interface.

- **Dynamic Application Status Updates**: Faculty members have the ability to update the status of applicants based on their qualities displayed in the application. This feature ensures transparency and keeps both parties informed throughout the selection process.

- **Adaptable Research Fields**: Faculty members can dynamically add new research fields to ensure the portal stays up-to-date with the evolving landscape of research.

## Technological Stack

| Section          | Technology             | Description                                               |
|------------------|------------------------|-----------------------------------------------------------|
| Backend          | Python, Flask           | Developed using Python and Flask for a robust and scalable server-side architecture. |
| Database         | SQL Alchemy            | Employed for efficient database management, ensuring data integrity and reliability. |
| Frontend Design  | HTML, CSS               | Utilized to create a clean and user-friendly frontend interface, enhancing the overall user experience. |
| Testing          | Unittest by Python      | Thoroughly tested using Python's unittest framework to ensure code quality and reliability. |


# Software Requirements Specification

### "WSU Research Portal"
--------
Prepared by:
* ![William Rae](https://github.com/WillRInternship) 
* ![Ehiane Oigiagbe](https://github.com/Ehiane)
* ![Cole Logan](https://github.com/clogan1227)

---

**Course** : CptS 322 - Software Engineering Principles I

**Instructor**: Sakire Arslan Ay
---

## Table of Contents
- [Software Requirements Specification](#software-requirements-specification)
  - [Table of Contents](#table-of-contents)
  - [Document Revision History](#document-revision-history)
- [1. Introduction](#1-introduction)
  - [1.1 Document Purpose](#11-document-purpose)
  - [1.2 Product Scope](#12-product-scope)
  - [1.3 Document Overview](#13-document-overview)
- [2. Requirements Specification](#2-requirements-specification)
  - [2.1 Customer, Users, and Stakeholders](#21-customer-users-and-stakeholders)
  - [2.2 Use Cases](#22-use-cases)
  - [2.3 Non-Functional Requirements](#23-non-functional-requirements)
- [3. Product Backlog](#4-product-backlog)

<a name="revision-history"> </a>

## Document Revision History

| Name | Date | Changes | Version |
| ------ | ------ | --------- | --------- |
|Revision 1 |2023-10-05 |Initial draft | 1.0    |
|Revision 2 |2023-11-25 |Addition of Use cases and User Stories | 2.0         |
|Revision 3 |2023-12-4  |Final review       | 3.0         |


----
# 1. Introduction

This section serves as the documentation to the Software Requirement Specification (SRS) document for the "Online Faculty Research Connection Platform"

## 1.1 Document Purpose
The purpose of this SRS document is to clearly define the requirements and specifications for the development of the "Online Faculty-Student Research Connection Platform." It outlines the non-functional requirements that the software solution must meet. This document serves as a critical reference for the project's stakeholders, including the development team, quality assurance, and all relevant parties involved in the platform's creation and operation.
## 1.2 Product Scope
### 1.2.1 Product Description
The "Online Faculty-Student Research Connection Platform" is designed to address the need for a centralized online platform where faculty members can post research positions and seamlessly connect with qualified undergraduate students. This platform will facilitate efficient communication between faculty and students, promoting collaborative research opportunities within the academic community.

### 1.2.2 Purpose and Goals
The main purpose of this software product is to offer an intuitive and user-friendly online interface that enables students to submit their contact information, academic coursework details, research interests, and prior research experience. Faculty members will have the ability to advertise research opportunities, receive student applications, and select candidates for interviews. 

The key objectives and goals of the platform include:
- Enhancing the accessibility of research opportunities for undergraduate students.
- Streamlining the faculty's ability to find and select qualified student researchers.
- Improving the overall efficiency and transparency of the research matching process.

### 1.2.3 Benefits
The "Online Faculty-Student Research Connection Platform" offers several benefits, including:
- Facilitating collaboration and networking between faculty and students.
- Simplifying the application and selection process for research positions.
- Enhancing the academic and research experience for all users.

## 1.3 Document Overview
The remainder of this document is organized into the following sections:


- Section 2: Requirments Specification - Outlines design, the audience, Use cases and Non-Functional Requirements.

- Section 3: User Interface (UI) Design - Details the design(with sketches included) and user interface guidelines.

- Section 4: Product Backlog - Guides the Development team through out the project by listing tasks and issues to handle as the development of the project carries on.

- Section 5: References - Contains all the external references or links that were used in the creation of the requirement document. 

This document will serve as a comprehensive reference for the development team, ensuring that the "Online Faculty-Student Research Connection Platform" is successfully designed, built, and meets the needs of all stakeholders.

# 2. Requirements Specification

This section specifies the software product's requirements. Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements, and to enable testers to test that the software system satisfies those requirements.

## 2.1 Customer, Users, and Stakeholders

Our customer will be WSU itself. We intend to make this software for WSU to use in order to advertise research positions to undergraduate students.

There will be two distinct users of our software: students and faculty.

Students will be any individual enrolled at WSU who is in undergrad. It is likely the student will be interested in research if they are to use our software. Students stand to benefit from our software because of the research opportunities that will be made available to them.

Faculty consists of any professors or graduate students who have a potential research opportunity for any interested undergrad students. Faculty must be employed by WSU and involved with research on campus. Faculty stands to benefit from our software because of the undergraduate students who will be able to assist with their research.

The stakeholders of this project will be WSU, students, faculty, and us, the programmers. Given this project is a success, WSU will have successfully funded a site that is able to connect undergraduate students with research positions that will prepare them for their future careers. Students will be able to boost their resume with their research experience and will have gained valuable skills from the experience. Faculty will recieve much needed help with their research, will connect with their undergrad students, and will be able to pass on their knowledge and skills to the students. We programmers will have created a successful site that many people will benefit from and use in the extended future, and will be able to add it to our resume.

----
## 2.2 Use Cases

This section will include the specification for your project in the form of use cases. The section should start with a short description of the actors involved (e.g., regular user, administrator, etc.) and then follow with a list of the use cases.

For each use case you should have the following:

* Name,
* Actors,
* Triggers (what initiates the use case),
* Preconditions (in what system state is this use case applicable),
* Actions (what actions will the code take to implement the use case),
* Alternative paths
* Postconditions (what is the system state after the use case is done),
* Acceptance tests (list one or more acceptance tests with concrete values for the parameters, and concrete assertions that you will make to verify the postconditions).

Each use case should also have a field called "Iteration" where you specify in which iteration you plan to implement this feature.

You may use the following table template for your use cases. Copy-paste this table for each use case you will include in your document.

Regular User:
8. On the student page, a student user can: Create a student account and enter their profile information
1. Set the account username and password (username should be the WSU email)
2. Enter contact information (name, last name, WSU ID, email, phone)
3. Enter additional information (major, cumulative GPA, expected graduation date, etc. )
4. Select the research topics they are interested in. You can assume a predetermined list of research fields and have the student choose among those.
5. Choose the programming languages with which they are familiar. You can assume a predetermined list of programming languages and have the instructor choose among those.
6. Describe their prior research experience if there is any.

| Name | Add Review |
|--------|--------|
| Users | Student |
| Rationale | When a student user wants to apply to a research position, they can create an account with information about themselves. |
| Triggers | The user intends to register as a student |
| Preconditions | The user is not already registered as a student. |
| Actions | 1. The user indicates to register themselves as a new student in the application. 2. The System will display the "Register Student Page" page 3. The user will then enter all the of the relevant information as requested by the form. The user then submits the form. 4. The system validates the entered entered information, checks that data is appropriate for each segment of form, (i.e., no GPA of 13.6) 5. The system will save the students login and information, acknowledging that the student is registered. 6. The system will navigate to the "View Positions" page. |
| Postconditions | The users login and information is saved to the system and can be used on the student "login" page. |
| Acceptance Tests | Check that the (1) users login is valid, and (2) the saved information is the same as what was submitted. |
| Milestone | Milestone 2 |

Regular User (Student):
9. On the student page, a student user can: Login with username and password
| Name | Add Review |
|--------|--------|
| Users | Student |
| Rationale | When a student user wants to apply to a research position, they can login with an existing username and password. |
| Triggers | The user intends to sign in as a previously registered student |
| Preconditions | The user has already registered as a student. |
| Actions | 1. The user indicates to log themselves in as a student in the application. 2. The System will display the "Student Login Page" page 3. The user will then enters their username and password as requested by the form. The user then submits the form. 4. The system validates the entered entered information (no space is left blank, or incorrect information entered). 5. The system will assign the information of the current user to the information of the account registered to that users sign in information. 6. The system will navigate to the "View Positions" page. |
| Postconditions | The users information will be taken from the system and applied to the current user. |
| Acceptance Tests | Check that the (1) users login is valid, (2) information is applied to current user |
| Milestone | Milestone 2 |

Regular User (Student):
10. On the student page, a student user can: View the open research positions (Milestone 1)
| Name | Add Review |
|--------|--------|
| Users | Student |
| Rationale | When a registered and logged in student wants to view open research positions. |
| Triggers | The user intends to view research positions, or logs in and is redirected to the home page. |
| Preconditions | The user has already registered and signed in as a student. |
| Actions | 1. The user indicates to view open research positions in the application. 2. The System will display the "View Positions Page" |
| Postconditions | The system will display all currently open research positions on the "View Positions" page. |
| Acceptance Tests | Check that the (1) user is logged in, (2) all open positions are displayed properly. |
| Milestone | Milestone 1 |

Regular User (Student):
11. On the student page, a student user can: View the open research positions (Milestone 3)
For Milestone 3:

| Name | Add Review |
|------ | ----------|
| Users | Student |
| Rationale | When a registered and logged in student wants to view open research positions that align with their own interests. |
| Triggers | The user intends to view research positions that align with their interests. |
| Preconditions | The user has already registered and signed in as a student, also has interests. |
| Actions | 1. The user indicates to view open research positions in the application that contain a tag that they are interested in. 2. The tags are checked by the system and posts are filtered by those tags. 3. The System will display the filtered "View Positions Page" |
| Postconditions | The system will display all currently open research positions on the "View Positions" page that contain the tags the user is interested in. |
| Acceptance Tests | Check that the (1) user is logged in, (2) all open positions are displayed properly, (3) they have been filtered properly. |
| Milestone | Milestone 3 |

Regular User (Student):
12. On the student page, a student user can view various displayed information:
1. Research project title
2. A brief description of the project goals and objectives
3. Start date and end date
4. Required time commitment (e.g., 10 hours per week)
5. Research field(s) (e.g., “Machine Learning, High Performance Computing, etc.)
6. Required programming language experience (e.g., “C++”, “Java”, “Python”, etc.)
7. A brief description of other required qualifications
8. Faculty’s name and contact information1. Research project title
2. A brief description of the project goals and objectives
3. Start date and end date
4. Required time commitment (e.g., 10 hours per week)
5. Research field(s) (e.g., “Machine Learning, High Performance Computing, etc.)
6. Required programming language experience (e.g., “C++”, “Java”, “Python”, etc.)
7. A brief description of other required qualifications
8. Faculty’s name and contact information

| Name | Add Review |
|--------|--------|
| Users | Student |
| Rationale | When a registered and logged in student wants to view information about a specific research position. |
| Triggers | The user intends to view research positions, or logs in and is redirected to the home page. |
| Preconditions | The user has already registered and signed in as a student. |
| Actions | 1. The user indicates to view open research positions in the application. 2. The System will display the "View Positions Page". 3. Each individual position will display the information listed above. |
| Postconditions | The system will display all the information listed above for a given research positions on the "View Positions" page. |
| Acceptance Tests | Check that the (1) user is logged in, (2) all open positions are displayed properly. |
| Milestone | Milestone 1 |

Regular User (Student):
13. On the student page, a student user can: Apply for research positions. A student can apply for more than one research position
For each position they apply to:
1. They should submit a brief statement describing why they are interested in this research topic and what they hope to gain by participating in that project.
2. They should provide the name and email of one faculty who can provide them a reference for the position. 

| Name | Add Review |
|--------|--------|
| Users | Student |
| Rationale | When a registered and logged in student wants to view open research positions and apply to any number of them. |
| Triggers | The user intends to apply to a research position. |
| Preconditions | The user has already registered and signed in as a student. |
| Actions | 1. The user indicates wanting to apply to an open research position in the application. 2. The System will use a many to many relationship to assign the user the the position they applied for. 3. The position will update for the user displaying they have applied. |
| Postconditions | The system will display that the user has applied for the position, allowing the faculty that posted it to view the students application. |
| Acceptance Tests | Check that the position has the user as an applicant through the relationship. |
| Milestone | Milestone 1 |

Regular User (Student):
14. On the student page, a student user can: View the research positions they already applied to and check the statuses of their applications
1. When the application is submitted, its status will appear as “Pending”.
2. After a faculty accept this application, the status should be updated as “Approved for Interview”. Student would do the interview in person.
3. After the interview, the faculty should update the status as either “Hired” or “Not hired”. Once updated, the changed status should be displayed on the student page.

| Name | Add Review |
|--------|--------|
| Users | Student |
| Rationale | When a registered and logged in student wants to view positions they have applied for and the status of their application. |
| Triggers | The user intends to view research positions they've applied for, and their application status. |
| Preconditions | The user has already registered, signed in as a student, and applied to positions. |
| Actions | 1. The user indicates to view research positions they've applied for in the application. 2. The System will display the "My Applications" page, and the status of each application. |
| Postconditions | The system will display all the users currently applied research positions on the "My Applications" page. |
| Acceptance Tests | Check that the (1) user is logged in, (2) all open applications are displayed properly. |
| Milestone | Milestone 3 |

Regular User (Student):
15. On the student page, a student user can: Withdraw their pending applications.
If the student is no longer interested in a research position, they can withdraw their application.

| Name | Add Review |
|--------|--------|
| Users | Student |
| Rationale | When a registered and logged in student wants to view positions they have applied for and rescind their application. |
| Triggers | The user intends to view research positions they've applied for and rescind their application. |
| Preconditions | The user has already registered, signed in as a student, and applied to positions. |
| Actions | 1. The user indicates to view research positions they've applied for in the application. 2. The System will display the "My Applications" page. 3. The user indicates they wish to rescind an application. 4. The relationship between the position and user will be deleted, rescinding their application. |
| Postconditions | The system will no longer display rescinded research position on the "My Applications" page. |
| Acceptance Tests | Check that the application the user wished to delete no longer exists. |
| Milestone | Milestone 3 |

Admin (Faculty):
16. On the faculty page, a faculty user can: Create a faculty account and enter profile information
1. Set the account username and password (user name should be the WSU email)
2. Enter contact information (name, last name, WSU ID, email, phone)

| Name | Add Review |
|--------|--------|
| Users | Faculty |
| Rationale | When a faculty user wants to create to a research position, they can create an account with relevant university information. |
| Triggers | The user intends to register as faculty |
| Preconditions | The user is not already registered as faculty. |
| Actions | 1. The user indicates to register themselves as a new faculty member in the application. 2. The System will display the "Register Faculty Page" page 3. The user will then enter all the of the relevant information as requested by the form. The user then submits the form. 4. The system validates the entered entered information, checks that data is appropriate for each segment of form, (i.e., actual WSU ID, not 3) 5. The system will save the faculty login and information, acknowledging that the faculty member is registered. 6. The system will navigate to the faculty home page. |
| Postconditions | The users login and information is saved to the system and can be used on the faculty "login" page. |
| Acceptance Tests | Check that the (1) users login is valid, and (2) the saved information is the same as what was submitted. |
| Milestone | Milestone 2 |

Admin (Faculty):
17. On the faculty page, a faculty user can: Login with username and password

| Name | Add Review |
|--------|--------|
| Users | Faculty |
| Rationale | When a faculty user wants to create a research position, they can login with an existing username and password. |
| Triggers | The user intends to sign in as a previously registered faculty member |
| Preconditions | The user has already registered as faculty. |
| Actions | 1. The user indicates to log themselves in as faculty in the application. 2. The System will display the "Faculty Login Page" page 3. The user will then enters their username and password as requested by the form. The user then submits the form. 4. The system validates the entered entered information (no space is left blank, or incorrect information entered). 5. The system will assign the information of the current user to the information of the account registered to that users sign in information. 6. The system will navigate to the "Faculty Home" page. |
| Postconditions | The users information will be taken from the system and applied to the current user. |
| Acceptance Tests | Check that the (1) users login is valid, (2) information is applied to current user |
| Milestone | Milestone 2 |

Admin (Faculty):
18. On the faculty page, a faculty user can: Create undergraduate research positions
Faculty should enter the details of the position and qualifications needed, i.e.,: 
1. Research project title
2. A brief description of the project goals and objectives
3. Start date and end date
4. Required time commitment (e.g., 10 hours per week)
5. Research field(s) (e.g., “Machine Learning”, “High Performance Computing”, etc.). You can assume a predetermined list of research fields and have the instructor choose among those.
6. Required experience with programming languages (e.g., “C++”, “Java”, “Python”, etc.) You can assume a predetermined list of programming languages and have the instructor choose among those.
7. A brief description of other required qualifications.
**Of course, a faculty can create more than one positions.**

| Name | Add Review |
|--------|--------|
| Users | Faculty |
| Rationale | When a faculty user wants to create to a research position. |
| Triggers | The user intends to create a new research position. |
| Preconditions | The user is currently registered and logged in as a faculty member. |
| Actions | 1. The user indicates to create a new research position in the application. 2. The System will display the "Create Research Position Page" page 3. The user will then enter all the of the relevant information as requested by the form. The user then submits the form. 4. The system validates the entered entered information, checks that data is appropriate for each segment of form, (i.e., no hour commitment of "egg") 5. The system will save created research position, acknowledging that the position was created. 6. The system will navigate to the "Faculty Home" page. |
| Postconditions | The users research position is saved and displayed for students to apply to. |
| Acceptance Tests | Check that the (1) the position has been saved, and (2) the position can be applied for my students. |
| Milestone | Milestone 1 |

Admin (Faculty):
19. On the faculty page, a faculty user can: See the list of the students who applied for their positions
A faculty should be informed about the other offers students get. If a student was “Approved for Interview” or was “Hired” for another position, those information should also be displayed. 

| Name | Add Review |
|--------|--------|
| Users | Faculty |
| Rationale | When a registered and logged in faculty member wants to view positions they've created and students that have applied to them. |
| Triggers | The user intends to view research positions they've created and the positions applicants. |
| Preconditions | The user has already registered, signed in as faculty, and created positions that have been applied to. |
| Actions | 1. The user indicates to view research positions they've created in the application. 2. The System will display the "My Positions" page, and the applicants of each position. |
| Postconditions | The system will display all the users currently created research positions on the "My Positions" page, as well as the applicants of each position. |
| Acceptance Tests | Check that (1) all created positions are displayed, (2) all applicants for each position is displayed. |
| Milestone | Milestone 2 |

Admin (Faculty):
20. On the faculty page, a faculty user can: View the qualifications of each student
1. their GPAs
2. the technical elective courses they have taken
3. the research topics they are interested in
4. the programming languages they have experience with
5. prior research experience.

| Name | Add Review |
|--------|--------|
| Users | Faculty |
| Rationale | When a registered and logged in faculty member wants to view positions they've created and the qualifications of the students that have applied to them. |
| Triggers | The user intends to view research positions they've created and the positions applicants qualifications. |
| Preconditions | The user has already registered, signed in as faculty, and created positions that have been applied to. |
| Actions | 1. The user indicates to view research positions they've created in the application. 2. The System will display the "My Positions" page, and the applicants of each position. 3. The user can view information about each applicant as listed above. |
| Postconditions | The system will display all the users currently created research positions on the "My Positions" page, as well as the applicants of each position and their qualifications.. |
| Acceptance Tests | Check that (1) all created positions are displayed, (2) all applicants qualifications for each position is displayed. |
| Milestone | Milestone 2 |

Admin (Faculty):
21. On the faculty page, a faculty user can: Approve the application of one or more students
The faculty can approve the application of one or more students and the status of those applications should be updated as “Approved for Interview”. 

| Name | Add Review |
|--------|--------|
| Users | Faculty |
| Rationale | When a registered and logged in faculty member wants to view positions they've created, the students that have applied to them, and approve the application of one or more of them. |
| Triggers | The user intends to accept the application of one or more applicants. |
| Preconditions | The user has already registered, signed in as faculty, and created positions that have been applied to. |
| Actions | 1. The user indicates to view research positions they've created in the application. 2. The System will display the "My Positions" page, and the applicants of each position. 3. The user indicates wether they would like to approve the application of a user. 4. The user is notified of acceptance. |
| Postconditions | The system will display that the users application has been accepted on both the faculty and student side. |
| Acceptance Tests | Check that (1) the position has been accepted on student side, (2) the position has been accepted on faculty side. |
| Milestone | Milestone 3 |

Admin (Faculty):
22. On the faculty page, a faculty user can: Update the status of applications
After interviewing with the student, the faculty can update the status of applications as either “Hired” or “Not hired”

| Name | Add Review |
|--------|--------|
| Users | Faculty |
| Rationale | When a registered and logged in faculty member wants to view positions they've created, the students that have been accepted, and indicate whether or not they've been hired. |
| Triggers | The user intends to hire or not hire one of the applicants. |
| Preconditions | The user has already registered, signed in as faculty, and created positions that have been applied to with accepted users. |
| Actions | 1. The user indicates to view research positions they've created in the application. 2. The System will display the "My Positions" page, and the applicants of each position. 3. The user indicates wether they would like to hired or not hire a student who was previously been accepted. 4. The user is notified of their status as either "hired" or "not hired". |
| Postconditions | The system will display that the users  has been either hired or not hired on both the faculty and student side. |
| Acceptance Tests | Check that (1) the status is correct on student side, (2) the status is correct on faculty side. |
| Milestone | Milestone 3 |

Admin (Faculty):
23. On the faculty page, a faculty user can: Delete the existing research positions
The faculty may delete the existing research positions. Once deleted, the status of all applications should be updated as “Position is not available”. 

| Name | Add Review |
|--------|--------|
| Users | Faculty |
| Rationale | When a registered and logged in faculty member wants to view positions they have created and delete one or more of them. |
| Triggers | The user intends to view research positions they've created and delete one or more. |
| Preconditions | The user has already registered, signed in as a student, and created positions. |
| Actions | 1. The user indicates to view research positions they've created in the application. 2. The System will display the "My Positions" page. 3. The user indicates they wish to delete a position. 4. The position will be deleted by the system. |
| Postconditions | The system will no longer display the research position on the "My Positions" page. |
| Acceptance Tests | Check that the positions the user wished to delete no longer exists. |
| Milestone | Milestone 3 |

----
## 2.3 Non-Functional Requirements

1. Students should only be able to access student functionality: Students should not be able to access faculty member exclusive functionality. This includes creating research opportunities, reviewing students qualifications, updating application statuses, etc.
2. Faculty should only be able to access faculty functionality: Faculty should not be able to access student exclusive functionality. This includes applying for research opportunities, updating student qualifications, etc.
3. Users must be logged in in order to access the site: Users should not be able to see research opportunities, apply for research positions, create research positions, etc without being logged in as a student/faculty member. Users must log in as a student to see the student view, and must log in as a faculty member to see the faculty view.
4. Our site should not take long to load different pages: When submitting a get or post request, our page should not take longer than a brief moment to load the next page. 
5. Our site should be easily readable and understood: We must keep all text in a clean, readable font that is easy to read and understand. The language included should be clear and to the point, leaving no room for confusion at any point. 
6. Our site should be well organized and easy to navigate: We must make sure all buttons are easy to see and that their purpose be easily understood. The layout should be clean and organized.
7. Students should only be able to create one account: Using their WSU email/ID, students should be able to create just a single account for themselves. If they are to try to create another account with the same ID, they should be stopped and directed to use a different ID.

----
# 3. Product Backlog
<div style="display; flex;">
  <img width="607" alt="Screenshot 2024-01-02 182044" src="https://github.com/Ehiane/StudentFacultyResearchPortal/assets/79903725/a74c3ca1-da37-4012-84aa-21860c2322c4" style="width: 48%;">
  <img width="607" alt="Screenshot 2024-01-02 182025" src="https://github.com/Ehiane/StudentFacultyResearchPortal/assets/79903725/e88cd2ff-0121-4ce8-ae10-160c36e6a09f" style="width: 48%;">
  <img width="604" alt="Screenshot 2024-01-02 182120" src="https://github.com/Ehiane/StudentFacultyResearchPortal/assets/79903725/dfe04654-b712-4f51-900e-0044c6cac08d" style="width: 48%;">
  <img width="601" alt="Screenshot 2024-01-02 182057" src="https://github.com/Ehiane/StudentFacultyResearchPortal/assets/79903725/8a81c8b7-9000-4c44-b7df-b2994af1b96b" style="width: 48%;">
  
</div>






