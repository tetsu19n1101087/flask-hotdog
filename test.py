from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def test():
  return render_template("index.html", title = "Flask")

if __name__ == '__main__':
  app.run()
  print("ok")

