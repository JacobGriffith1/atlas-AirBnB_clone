# The Atlas AirBnB Console


![alt text](https://github.com/moshjerrick/atlas-AirBnB_clone/blob/main/Airbnb_Logo_Be%CC%81lo.svg.png)


## Description
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…


# Requirements
## Python Scripts

* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
* e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
* e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')




## How to start and use our console

* Clone this repository: git clone "https://github.com/moshjerrick/AirBnB_clone.git"
* Access AirBnb directory: cd AirBnB_clone    
* Run hbnb(interactively): ./console and then press enter command
* Run hbnb(non-interactively): echo "<command>" | ./console.py

## List of commands


| Command  | Description |
| ------------- | ------------- |
| ```quit```  | Quits or exits the console |
| ```EOF```  |  ```ctrl+D ``` Will quit or exit the console |
| ```create <classname>```  | Creates Object, saves it to JSON file, prints out Objects ID |
| ```help``` or ```Help <command>``` |  Displays all available commands and explains specific commands |
| ```Show <class> <ID>```  | Shows string representation of object     |
| ```Destroy <class> <ID>``` | Deletes object based on classname and ID      |
| ```All ``` |  Prints all strings representing a object and all of a specific class    |

## Examples
```
$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create
Creates new instance of BaseModel and saves it to JSON file
(hbnb) help update

        Updates an instance based on the class name and id by
        adding or updating attribute
        (save the change into the JSON file).
        
(hbnb) quit
$
```
