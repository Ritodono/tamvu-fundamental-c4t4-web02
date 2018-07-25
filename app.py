#1 Create Flask App
from flask import Flask, render_template

app = Flask(__name__)

class movie:
    def __init__(self, t, c, tu):
        self.title = t
        self.casts = c
        self.thumbnail_url= tu

m1 = movie('Batman: The dark night rises',
          'christian bale, cillian murphy',
          'https://www.google.com.vn/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjGhevvp7DcAhWHlJQKHW71AG0QjRx6BAgBEAU&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DDKbkKJWYT6E&psig=AOvVaw28qH96_kaxYC06KPCaf72a&ust=1532265536574816')
m2 = movie("ant man",
           "michael douglas. dr. hank pym. evangeline lilly",
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8omKF5M-hmVXwczBS5L2Qir_3JuoHhmXLEeVu73cGjMfDyCPzEQ")

movie_list = [m1,m2]
@app.route("/")
def index():
  return render_template("index.html",
    name="tam",
    img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRiAmjlgQoYG-_DqR0u4M-mqjoUJLooOtnE_AOsmmLuBBDYuMckUg")


@app.route("/casts")
def casts():
  return render_template("casts.html", casts)
@app.route("/movie")
def movie():
    return render_template("movie.html", movie = m)

@app.route("/about-me")
def about_me():
  return "Huy - 29, single, teacher, developer..."

@app.route("/hello/<name>")
def hello(name):
  return "Hello " + name

# 2 Run app
if __name__ == "__main__":
  app.run(debug=True)