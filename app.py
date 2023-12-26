from flask import Flask, render_template, request,jsonify
from pdfminer.high_level import extract_pages,extract_text
from transformers import pipeline

summarizer=pipeline('summarization')
# text=extract_text("sample.pdf")
# print(text)

app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    user_text = None
    ai_text=None
    if request.method == 'POST':
        user_text = request.form['user_text']
        print(user_text)
        ai_text = as_summary(user_text)
        return jsonify({'user_text': user_text, 'ai_text': ai_text})
    return render_template('base.html')


def as_summary(txt):
    summary=summarizer(txt,max_length=150, min_length=30,do_sample=False)
    out_text=summary[0]['summary_text']
    return out_text



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
