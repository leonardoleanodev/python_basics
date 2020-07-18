precisa de tradução

# Install Python on Windows

## Python

### Download and Install
https://www.python.org/
- click on Downloads
- python 3.7

### Configurations Unders Installation
- add python 3.7 to path
- disable the path limitation 

![alt text](https://github.com/LeonardoLeano333/python_tutorials/blob/master/install_python.png)

![alt text](https://github.com/LeonardoLeano333/python_tutorials/blob/master/install_python_2.png)


### Test the python 
Open CMD (command prompt), recommend to open as administrator:
type: 
```C:\Users\Dell>python```

It should show up:
```
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
to exit the console type:
```
exit()
```

## Virtualenv
Virtual enviroments are important to isolate your develop enviroment from your computer or other projects, after you install `python` you have already installed `pip`. pip is a package mannager which provide you a easy way to install packages. 

### Install virtualenv
just type at CMD:
```
pip install virtualenv
```
It is going to download and install the virtualenv

#### Usefull commands in CMD:

open directory:

cd <directory name>

go up a directory level:

cd . 

create a direcory:

mkdir <directory name>


### Create a new environment

Go to the wanted directory which you want to start your new environment, and type:
```
virtualenv venv
```
It is going to make a new python3.7 environment (directory `venv`), but you have to activate it.

### Activate the enviroment

To activate just type at the same level directory:
```
venv\Scripts\activate
```
It is going to display a 
```
(venv) C:\Users\<dir path>
```

### installing packages in the enviroment

after activate the envonment install the packages just typing:

```
pip install <package name/library name>
```

examples:

```
pip install jupyter
pip install matplotlib
pip install pandas
pip install numpy
pip install seaborn
.
.
.
```

### pip freeze

to be sure that you are going to use the same libraries at the same version you can type pip freeze to make a requirement file which have the versions and libraries used in your environment, like this:
```
pip freeze > requirements.txt
``` 
this command makes a .txt file which have the libraries dependencies of your project

### pip install requirements

After you made a requirementl.txt file you can reinstall all the libraries again just typing:

```
pip install -r requirements.txt
```
It is going to install all the libraries and dependecies pre stabilished at `requiriments.txt`

Obs.: Remember to install this with pip after activate the enviroment.

## git 
Git is a version control system, and it is widely used in software development. you can install git downloading at this link:

https://git-scm.com/downloads

### Git-Bash

At windows git installation, it install Git-Bash too. Git-Bash is a terminal which has alot of same commands as the linux terminal, like:

list dir
```
ls
```
vim (text editor)
``` 
vim
```
and so on...

AND IT IS COLLORIZED to help development and look at files as a terminal interface.
