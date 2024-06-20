from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship, Session
from sqlalchemy import Integer, String, ForeignKey, select, delete, update, create_engine

engine = create_engine(f"sqlite:///linkedout.sqlite3", echo=True)
session = Session(engine)
Base= declarative_base()

class User(Base):
    __tablename__ = "user_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]  = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer)
    comment: Mapped["Comment"] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

    #representation of the particular class
    def __repr__(self):
        return f"{self.name}"

class Profile(Base):
    __tablename__ = "profile_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped[str]  = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped['User'] = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"{self.profile}"
    

class Comment(Base):
    __tablename__ = "comment_tabble"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str]  = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped['User'] = relationship(back_populates="comment")

    def __repr__(self):
        return f"{self.comment}"