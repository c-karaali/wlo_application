import sqlalchemy as sa
from fh.aalen.data.modelbase import ModelBase
from sqlalchemy.orm import relationship

class Observed(ModelBase):
    __tablename__ = 'Observed'
    animal_id = sa.Column(sa.ForeignKey('Animal.id'), primary_key=True)
    location_id = sa.Column(sa.ForeignKey('Location.lnr'), primary_key=True)
    animal = relationship("Animal", back_populates="locations")
    location = relationship("Location", back_populates="animals")