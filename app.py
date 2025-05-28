from flask import Flask, render_template, request, redirect, url_for
from Utils.Prepare_table_json_structures import all_metadata
from services.AI_service import ask_question_to_ai
import json
import os


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Initial page load, no answer yet
    return render_template('index.html', ai_answer=None, thinking=False)

@app.route('/save_comments', methods=['POST'])
def save_comments():
    allMetadata_formatted = "{"
    for view in all_metadata:
        table_name = view[0]
        allMetadata_formatted += '"' + table_name + '":{'
        comment = request.form.get(f"comment_{table_name}", "")
        allMetadata_formatted += f'"comment":"{comment}", "columns":['
        
        columns = view[1]
        for idx, data in enumerate(columns):
            if idx > 0:
                allMetadata_formatted += ','
            allMetadata_formatted += '{"name":"' + data['name'] + '", "type":"' + str(data['type']) + '"}'
        allMetadata_formatted += ']},'
    allMetadata_formatted = allMetadata_formatted[:-1] + "}"

    # Optionally save the JSON string to a file:
    with open('Json/metadata_with_comments.json', 'w') as f:
        f.write(allMetadata_formatted)
    return redirect(url_for('index'))

@app.route('/chat', methods=['POST'])
def chat():
    question = request.form.get('question')
    with open('Json/metadata_with_comments.json', 'r') as f:
        metadata_json = f.read()

    # Optionally: render the page first with thinking=True to show "AI is thinking..."
    # But since Flask rendering is server-side, you’ll see the whole response after AI finishes

    ai_answer = ask_question_to_ai(question, metadata_json)

    return render_template('index.html', ai_answer=ai_answer, thinking=False)
if __name__ == "__main__":
    app.run(debug=True)