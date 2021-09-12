import infraestructure.S3 as Storage
from datetime import datetime
from infraestructure.db_mongo import mongo
from bson.objectid import ObjectId

class ServiceGallery:
    def ___init___(self) -> None:
        self.uri = ''

    def get_images(self, param):
        if param == 'true':
            images = list(mongo.apptenis.gallery.find({"status": "not_approved"}))
        else:
            images = list(mongo.apptenis.gallery.find({"status": "approved"}))
        return Storage.InfraestructureStorage().get_image(images)

    def upload_image(self, image):
        try:
            Storage.InfraestructureStorage().upload_image(image)
            data = {
                "filename": image.filename,
                "date": datetime.now(),
                "status": 'not_approved'
            }
            mongo.apptenis.gallery.insert_one(data)
            return data
        except Exception as err:
            print(err)

    def approve_image(self, id):
        query_filter = {"_id": ObjectId(id)}
        new_values = {"$set":{ "status": "approved" }}
        mongo.apptenis.gallery.update_one(query_filter, new_values)