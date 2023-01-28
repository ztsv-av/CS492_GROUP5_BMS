# CS492_GROUP5_BMS

## Bookstore Management System

The project is running on Django (Python library). You will need to start it on your local machine in order to be able to edit files, view the changes and push the changes to this repository. Here are the steps that you will need to take to succefully start the virtual environment (**NOTE**: the following is for Windows users. If you have Linux, there might be some differences in command line commands).

1. Git clone this repository to your computer
2. Open CMD, go to the 'bookstore' folder (that you downloaded) and activate the virtual environment by following these 4 steps: 
  - type: python -m venv virt
  - type: virt\Scripts\activate
  - type: pip install django
  - type: pip install Pillow
3. Next, go to the next bookstore folder (bookstore/bookstore) and run the local server by typing: python manage.py runsever
5. The server should be up and running on your local machine (make sure that there are no errors in the CMD).
6. Open up your browser and type the following address: localhost:8000
7. This should show you the whole bookstore project and display any changes that you make to the files.
8. Once you are ready to push the changes to the repository, first - stage the change, second - write a small change description and commit the change, third - push the change to the repository.

**NOTE: before pushing any changes to the repository, make sure that your files are up to date. Sometimes people might push changes before you, so your code becomes outdated.**

If you are not sure how to set up the virtual enviroment or how to work with Django, you can follow this tutorial: https://www.youtube.com/watch?v=HHx3tTQWUx0&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=1

