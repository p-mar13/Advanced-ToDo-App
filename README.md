# Advanced To Do App

The project is focused on creating a well-known To-Do Web Application. But there will be some additional features available, that are going to make it stand out from your typical To Do App done by following a simple tutorial. 

Project could be used by managers or small companies to track the tasks done by their employees. 

Tech stack: Django (Python), DRF, PostgreSQL, HTML, Tailwind CSS, Vue.js

Planned features:
- calendar available to plan future tasks and see past tasks
- simple CRUD logic of to-do tasks (done)
- to-do tasks sorted into different categories (done)
- dockerized project
- trigger for weekly e-mail reports with statistics
- authentication system (manager and default account)
- availability to generate daily/weekly/monthly reports
- achievements system - synced with current date

Implemented features:
* CRUD for tasks on Django side (tested with Postman)
* Django integrated with PostegreSQL
* Vue.js initially set up, simple routing & calendar & GET requests added
* implemented categories and status classes nested inside to-do tasks

Current to-do:
1. link each task to list
2. add simple frontend: view all tasks, view info about chosen task, delete task, add new task
3. modify frontend view - all tasks visible in calendar (by date added)+can view all tasks in a certain day. New tasks added by clicking on a day with create_date automatically filled. By clicking on a existing task - display info and offer to update or delete

