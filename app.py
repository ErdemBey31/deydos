from flask import Flask
app = Flask(__name__)
@app.route('/')
def hp():
  return "fuxk you"
boc = "o"
if boc == "o":
  app.run();
