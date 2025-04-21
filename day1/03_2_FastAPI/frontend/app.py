from flask import Flask, request, jsonify, render_template, send_from_directory
import requests
import os

app = Flask(__name__)

# Get backend URL from environment variable or use default
BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:8000')

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        if prompt:
            try:
                # Call FastAPI backend
                backend_url = f"{BACKEND_URL}/generate"
                print(f"Calling backend at: {backend_url}")
                response = requests.post(
                    backend_url,
                    json={"prompt": prompt, "max_new_tokens": 512}
                )
                if response.status_code == 200:
                    data = response.json()
                    response_text = data.get('generated_text', 'No response from API')
                else:
                    response_text = f"Error: {response.status_code}"
            except Exception as e:
                response_text = f"Error: {str(e)}"
    
    return render_template('index.html', response_text=response_text)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)