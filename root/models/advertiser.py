from sqlalchemy import Column, Integer, String

from root import models


class Advertiser(models.Base):
    __tablename__ = 'advertiser'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)

    def __init__(self, name):
        self.name = name
