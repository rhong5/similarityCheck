from flask import Flask, request, render_template
from Similar_Texts import compareText
app = Flask(__name__)

@app.route("/")
def text_input_form():
    return render_template('/result.html')

@app.route("/", methods=['POST'])
def my_form_post():
    text1=request.form['text1']
    text2=request.form['text2']
    result = compareText(text1, text2)
    return "Similarity: "+str(result)


if __name__ == '__main__':
    app.run(debug=True)