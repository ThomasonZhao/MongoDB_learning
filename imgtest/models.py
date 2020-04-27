import mongoengine

# Create your models here.


class ImageModel(mongoengine.Document):
    filename = mongoengine.StringField()
    data = mongoengine.FileField()
    uploadDate = mongoengine.DateField()
