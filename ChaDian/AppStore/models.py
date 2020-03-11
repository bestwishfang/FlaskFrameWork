from . import models


class BaseModel(models.Model):
    __abstract__ = True
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)

    def save(self):
        db = models.session()
        db.add(self)
        db.commit()

    def delete(self):
        db = models.session()
        db.delete(self)
        db.commit()


# class Class_Info(BaseModel):
#     __tablename__ = 'class_info'
#     class_num = models.Column(models.String(32))
#     class_name = models.Column(models.String(32))
#     entrance_time = models.Column(models.Date)
#     college = models.Column(models.String(32))