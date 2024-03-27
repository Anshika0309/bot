from flask import Flask, render_template, request
import openai


app = Flask(__name__, template_folder='templates')

openai.api_key = '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'


# default route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    
    response = openai.Completion.create(
        engine="davinci", 
        prompt=message,
        max_tokens=150
    )
    
    if response.choices:
        return response.choices[0].text.strip()
    else:
        return 'Failed to Generate response!'

if __name__=='__main__':
    app.run()
