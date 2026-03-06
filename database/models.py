from sqlalchemy import Column, String, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trend(Base):
    __tablename__ = "trend"
    id = Column(String, primary_key=True)
    keyword = Column(String)
    source = Column(String)
    growth_rate = Column(Float)
    volume = Column(Float)
    timestamp = Column(DateTime)

class Opportunity(Base):
    __tablename__ = "opportunity"
    id = Column(String, primary_key=True)
    project_name = Column(String)
    opportunity_score = Column(Float)
    trend_score = Column(Float)
    demand_score = Column(Float)
    competition_score = Column(Float)
    difficulty_score = Column(Float)
    is_blue_ocean = Column(Boolean)
    timestamp = Column(DateTime)
