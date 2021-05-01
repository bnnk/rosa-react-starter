from rosa import Rosa, Response, request
from rosa.middleware import Middleware
from middleware import SimpleCustomMiddleware

app = Rosa()

@app.route("/home/{kast}")
def home_kast(kast=None):
  home_kast.resp = Response(text = "Zootopia: " + kast)
@app.route("/home/")
def home():
  home.resp = Response(
    body = app.render("hello.jinja2",
        title = "Ramachandra",
        user = request.headers["User-Agent"]
      )
    )


app.add_middleware(SimpleCustomMiddleware)