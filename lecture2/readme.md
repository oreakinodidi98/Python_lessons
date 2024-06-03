# Iteration and GitHub

process of repeateadly executing a set of instructions or a code block
2 types of Loops

## While Loops

- As long as specific condition is true

```py
count = 0
while count < 5:
    print("count is:"" , count)
    count += 1
#this will print numbers from 0 to 4 
```

## For Loops

- control flow structures 
- iterate over sequence 
- used when you know the number of times you want to execute a block of code

```py
pokemon_list= ["pikachous","chazard","something","something2"]
for pokemon in pokemon_list:
    print (pokemon)
```

## Ranges

- built in python function
- generate a sequence of numbers
- range(start, stop, step)
- specify a sequence of numbers that you want to iterate over
- if start is not provided it defaults to 0
- step defaults to 1
- stop value is exclusinve so will stop before reaching it

```py
for i in range(start, stop, step):
    print(i)
```

## Trace Tables

- step by step record of your programms journey through each line of code 
- helps you keep track of how the values of variables change as the progeramm run
- visualise what is going on in your ccode
- also known as **trace diagrams** or **execution tables**
- can be a simple excell sheet

```py
x=5
y=2
z = x + y
print (x , y, z)
```

## Git

- version control, system that records changes to files over time
- git = version control system
- distributed

## GitHub

- online hub for code
- centralised platform for hosting
- git init
- git add .
- git branch -M main
- git commit -m "commit message"
- git remote add origin <your_Remote_repo_url>...
- git push -u origin master
- git fetch origin
- git merge origin/master
- git branch <branch_name>
- git checkout <branch_name>
- git checkout -b <branch_name>
- git stash -> takes all changes in your working copy and saves them to a clipboard
- git stash pop -> get the newest stash and clear it from the clipboard
- git stash apply <stashname> -> get specifieed stash 
- repository: location or directry where project files resides
- commit: snapshot of project at specific point in time. representss a sset of changes made to the files in your repository
- branch: seperate line of developent withing a repository
- merge: combines changes from one branch into another
- pll request: request to merge changes from one branch into another. allows for code review and collaboration before changes are merged
- git authentication: process of aunthenticating users who interact with git repository
- door lock -> like a key
- GitHub DAG (Directed Acyclic Graph). Helps you track history of Code