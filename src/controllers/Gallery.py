import service.Gallery as Gallery


class ControllerGallery:
    def images(self, request):
        file = request.files['image'] if len(request.files) > 0 else None
        param = request.args.get('infos')
        method = {
            "POST": ['upload_image', file ],
            "GET": ['get_images', param],
        }
        print(param)
        controller = getattr(Gallery.ServiceGallery(),method[request.method][0])
        return controller(method[request.method][1])

    def approve_image(self, id):
        return Gallery.ServiceGallery().approve_image(id)