from flask import Flask, render_template,request,jsonify
from pdfminer.high_level import extract_pages,extract_text
text=extract_text("chatbot-deployment/sample.pdf")
print(text)
# from chat import get_response
app=Flask(__name__)
@app.route("/")
def index():        
    return render_template("base.html") 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
