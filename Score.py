from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def read_score():
    with open("Score.txt", "r") as data_file:
        score = data_file.readline()
    return render_template("index.html", SCORE=score), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)