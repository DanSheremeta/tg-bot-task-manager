from app.base import Base
from app.const import TaskPriority

from sqlalchemy import Column, String, Integer, Enum, ForeignKey, Float, func, DateTime
from sqlalchemy.orm import relationship


class TaskList(Base):
    __tablename__ = "task_list"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    username = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="list", cascade="all, delete")


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    priority = Column(Enum(TaskPriority), nullable=True)
    list_id = Column(
        Integer, ForeignKey("task_list.id", ondelete="CASCADE"), nullable=False
    )

    deadline = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    list = relationship("TaskList", back_populates="tasks")
