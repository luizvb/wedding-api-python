import service.Gallery as Gallery
class ControllerGallery:
    def get_images(self, request):
        try:
            return Gallery.ServiceGallery().get_images(request.args.get('infos'))
        except Exception as err:
            print(err)

    def upload_image(self, request):
        try:
            return Gallery.ServiceGallery.upload_image(request.files['image'])
        except Exception as err:
            print(err)

    def approve_image(self, id):
        try:
            return Gallery.ServiceGallery().approve_image(id)
        except Exception as err:
            print(err)