from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import keras
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

model = keras.models.load_model('models/model3.h5')


@app.route("/")
def test():
  return render_template("index.html")

@app.route("/post", methods=["POST"])
def post():
  file = request.files['image']
  dtype = file.filename.rsplit('.', 1)[1]
  if file and (dtype == 'jpg' or dtype == 'jpeg'):
    filename = 'images/' + file.filename
    file.save(filename)
    image = Image.open(filename).resize((100, 100))
    array = np.array([np.array(image)]) / 255
    result = str(np.round(model.predict(array)[0][0] * 100, decimals=4))
    os.remove(filename)
    return render_template("result.html", result=result, port="5000")
  else:
    return render_template("error.html")

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(app.root_path, 'favicon.ico')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5001)
