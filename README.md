# kivyTest

## Description of Components <br>
backend/: This directory contains all the backend logic of your application. It can include data processing, database interactions, network requests, etc. <br>

__init__.py: Makes Python treat the directories as containing packages; this is just an empty file. <br>
logic.py: Here, you define classes and functions related to the business logic of your application. For example, Backend class in our previous example. <br>
frontend/: This directory will contain all frontend-related files, primarily your .kv files for Kivy. <br>

__init__.py: Similarly, makes Python treat the directory as containing packages. <br>
main.kv: Contains the Kivy markup language definitions for your application's UI. It's linked to your main application logic in main.py. <br>
main.py: This is the entry point of your application. It initializes the app, loads the Kivy UI definitions, and creates instances of your backend logic. It's where you tie together the frontend and backend parts of your application. <br>

requirements.txt: Lists all the Python package dependencies for your project, ensuring that anyone who works on the project can install the correct versions of the required packages. For a basic Kivy application, this might just list Kivy and any other libraries you're using for your backend logic. <br>

## File Hierachy <br>
my_kivy_project/ <br>
│ <br>
├── backend/ <br>
│   ├── __init__.py <br>
│   └── logic.py        # Contains your application's backend logic <br>
│<br>
├── frontend/<br>
│   ├── __init__.py<br>
│   └── main.kv         # Your Kivy language file for UI definitions<br>
│<br>
├── __init__.py<br>
├── main.py             # Entry point of the application, initializes the app and binds frontend and backend<br>
└── requirements.txt    # Python dependencies for your project<br>
