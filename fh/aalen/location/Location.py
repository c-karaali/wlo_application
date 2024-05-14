import sqlalchemy as sa
from fh.aalen.data.modelbase import ModelBase
from fh.aalen.relations.observed import Observed
class Location(ModelBase):
    __tablename__ = 'Location'

    lnr = sa.Column('lnr', sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column('title', sa.String, nullable=False)
    description = sa.Column('description', sa.String, nullable=False)
    persons = sa.orm.relationship("Favours", back_populates="video")

    #Helpermethod to create a dictionary representation from video attributes
    def to_dict(self):
        return dict(lnr=self.lnr,
        title=self.title,
        description=self.description,
        )