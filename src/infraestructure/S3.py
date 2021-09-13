import boto3
import os

class InfraestructureStorage:
    def __init__(self) -> None:
        self.access_key = os.environ['AWS_ACCESS_KEY']
        self.secret_key = os.environ['AWS_SECRET_KEY']
        self.s3 = boto3.client('s3',aws_access_key_id=self.access_key,aws_secret_access_key=self.secret_key)
        self.bucket = 'galleryimages'

    def get_image(self, images):
        response = {}
        data = []
        print(images)
        for image in images:
             image['url'] =self.s3.generate_presigned_url('get_object', ExpiresIn=3600, Params={'Bucket': self.bucket, 'Key': image['filename']})
        return images
    
    def upload_image(self, image):
        return self.s3.upload_fileobj(image, self.bucket,image.filename)
            