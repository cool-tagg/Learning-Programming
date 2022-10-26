from extractors.extract_themes import get_themes_allPage, get_themes_onePage
from extractors.file import save_to_file
from flask import Flask, render_template

print("----------------------------------------------------------------")
print("----------------------------------------------------------------\n\n ")
print("Now Start")



app = Flask("ThemeStripper")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/hello")
def hello():
    return render_template("hello.html", game = "tagg")

app.run()


print("ok")
print("\n\n ----------------------------------------------------------------")
print("----------------------------------------------------------------")
