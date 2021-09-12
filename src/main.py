from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import controllers.Gallery as Gallery
from common.mongoflask import MongoJSONEncoder, ObjectIdConverter

app = Flask(__name__)
CORS(app)

app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

@app.route("/images", methods=['GET', 'POST', 'OPTIONS'])
def images():
      return jsonify(Gallery.ControllerGallery().images(request))

@app.route("/images/<id>", methods=['PUT'])
def approve_image(id):
    return jsonify(Gallery.ControllerGallery().approve_image(id))



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=3001, debug=True)
