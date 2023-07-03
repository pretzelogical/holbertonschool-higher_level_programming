#!/usr/bin/python3
"""Representation of a state using SQLalchemy"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Represents a state for a SQL database

    attrs:
    __tablename__ (str): The name of the sql table
    id (sqlalchemy.Integer): The state id
    name (sqlalchemy.String): The state name
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
