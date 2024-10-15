import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250))
    description = Column(String(250))
    diameter = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    gravity = Column(String(250))
    population = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    url = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250))
    description = Column(String(250))
    model = Column(String(250))
    vehicles_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_creadits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atomsphering_speed = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    films = Column(String(250))
    pilots = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))
    url = Column(String(250))

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    color_eyes = Column(String(250))
    birth_year = Column(String(250))
    films = Column(String(250))
    gender = Column(String(6))
    hair_color = Column(String(250))
    height = Column(Float)
    homeworld = Column(String(250), ForeignKey(Planets.id))
    mass = Column(String(250))
    skin_color = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    spices = Column(String(250))
    starships = Column(String(250))
    url = Column(String(250))
    vehicles = Column(String(250), ForeignKey(Vehicles.id))

