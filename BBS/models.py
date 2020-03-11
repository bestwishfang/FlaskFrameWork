from app import models


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

# 电影类型  一部电影可以对应多种类型
class Genre(BaseModel):
    __tablename__ = 'genre'
    name = models.Column(models.String(32))


class Movie(BaseModel):
    __tablename = 'movie'
    movie_id = models.Column(models.Integer, unique=True, primary_key=True)
    movie_name = models.Column(models.String(64))
    movie_location = models.Column(models.String(32))






































