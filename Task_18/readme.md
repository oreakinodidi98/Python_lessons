# create a Virtual enviroment

- python -m venv venv
- activate the virtual enviroment: . .\venv\Scripts\Activate
- install dependencies
  - pip install django
  - pip install flake8
    - check code: flake8 crud_example.py

```py
crud_example.py:8:1: W293 blank line contains whitespace
crud_example.py:9:17: W291 trailing whitespace
crud_example.py:10:1: E302 expected 2 blank lines, found 1
crud_example.py:12:11: F541 f-string is missing placeholders
crud_example.py:14:80: E501 line too long (97 > 79 characters)
crud_example.py:15:1: W293 blank line contains whitespace
crud_example.py:16:1: E302 expected 2 blank lines, found 1
crud_example.py:25:1: E302 expected 2 blank lines, found 1
crud_example.py:29:80: E501 line too long (101 > 79 characters)
crud_example.py:34:1: E302 expected 2 blank lines, found 1
crud_example.py:45:1: E302 expected 2 blank lines, found 1
crud_example.py:57:1: E305 expected 2 blank lines after class or function definition, found 1
crud_example.py:58:13: E128 continuation line under-indented for visual indent
crud_example.py:59:13: E128 continuation line under-indented for visual indent
crud_example.py:60:13: E128 continuation line under-indented for visual indent
crud_example.py:71:15: W292 no newline at end of file
```

- Deactivate the virtual environment: venv\Scripts\deactivate.bat
- or : deactivate

## generating a requirements file

- document outlining the specific Python packages and their corresponding versions required for the project to run successfully.
- you can use the pip freeze command
- This command lists all installed packages and their versions.
- Here's how you can create a requirements.txt
- activate virtual nviroment: . .\venv\Scripts\Activate
- run command: pip freeze > requirements.txt
  - This command creates a requirements.txt file containing the names and versions of all installed packages
  - to include only the packages needed for your project (excluding development dependencies), you can use the:
  - pip freeze --exclude-editable > requirements.txt
  - j
