# The Atlas AirBnB Console


![alt text](https://github.com/moshjerrick/atlas-AirBnB_clone/blob/main/Airbnb_Logo_Be%CC%81lo.svg.png)


## Description
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…



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
$```
