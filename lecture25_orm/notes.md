# ORM (Object-Relational Mapping)

## Database interactions

- Example
- SELECT * FROM users WHERE age > 30;
- Negatives: Verbose, error-prone, and tightly coupled to database specifics

## ORM

- Object-Relational Mapping
- technique to interact with databases using an object-oriented programming (OOP) language
- This Simplifies database operations by mapping database tables to class structures in code

```py
# define the model
class User(Base): # Grade is a class that inherits from BaseModel.
    __tablename__ = "Users" # name of the table in the database
    grade = Column("grade", Integer, nullable=False)
    student_id = Column("student_id", Integer, ForeignKey("Students.id"), nullable=False) # foreign key to students table
    subject = Column("subject", String, nullable=False)
    course_id = Column("course_id", Integer, ForeignKey("Courses.id"), nullable=False)
```

- ORM is the abstraction Layer
- Provides a layer between application code and the database
- Enables developers to work with high-level objects instead of raw SQL
- session.execute(select(User).where(User.age == 'John Doe')).all()
- Migrations are a way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your databaseschema.
- They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into

## process

- python -m venv venv
- . .\venv\Scripts\Activate
- pip install django
- pip install sqlalchemy
- pip install alembic
- pip list
- pip freeze > requirements.txt

### Import

``` py
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship, Session
from sqlalchemy import Integer, String, ForeignKey, select, delete, update, create_engine

engine = create_engine(f"sqlite:///linkedout.sqlite3", echo=True)
session = Session(engine)
Base= declarative_base()
```

- create an engine
- different relationshisps
- user = parent class
- profile and comment are children


### modles

- create modles.py
- now perform migration
  - alembic --version
  - initiallise a migration folder
    - alembic init <name of folder>
  - alembic.ini -> sqlalchemy.url -> change address to sqlite:///my_db.db
  - show models we want to have migrated and add our models metadata to env.py.
    - <name of folder> -> env.py -> target_metadata -> from models import BaseModel, Grade, Course, Student 
    - target_metadata = [BaseModel.metadata]
  - create migration
    - alembic revision --autogenerate -m "added student , grade and class tables"
  - apply migration
    - alembic upgrade head
  - connect with DBeaver
    - SQL lite -> path to current folder