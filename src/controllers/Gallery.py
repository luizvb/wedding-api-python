import service.Gallery as Gallery
class ControllerGallery:
    def images(self, request):
        try:
            file = request.files['image'] if len(request.files) > 0 else None
            param = request.args.get('infos')
            method = {
                "POST": ['upload_image', file ],
                "GET": ['get_images', param],
            }
            controller = getattr(Gallery.ServiceGallery(),method[request.method][0])
            return controller(method[request.method][1])
        except Exception as err:
            print(err)

    def approve_image(self, id):
        try:
            return Gallery.ServiceGallery().approve_image(id)
        except Exception as err:
            print(err)