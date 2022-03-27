This a a basic Python Pytest Automation Framework.

Technologies used are:

  Python programming language.
  Pytest: Test framework
  pytest-html: for HTML reporting
  Python Logging: For the logger utiliy

The project structure from root folder is as follows:
  /images: for storing saved images from the API random image tests
  /logs: for saving all the test logs
  /page_objects: contains the page object files for the web automation
  /tests: contains the test cases for API and Web
  /utilities: contains a base_class for commonly used modules
  
  The /test/conftest.py file is a Python file which is placed in the test folder. 
  It contains the web driver setup/teardown, reporting and test data functions.
   
  To install the framework:
    After cloning from VCS:
      Ensure that Python 3.10.xxx is installed and added to Windows System Path.
      Open the project preferbly with Pycharm IDE
      In Pycarm settings, select File > Settings and add a new Python virtual envoronment.
      In Pycharm, select Tools > Run setup.py
      The tests are then ready to execute from within Pycharm run or from a Command Prompt window: pytest
      
   Test logs can be viewed in the /logs folder
   HTML Report (with screenshot apon failure) can be viewed in the report.html file
