from flask import Flask, request, jsonify
from src.llm_client import screen_candidate

app = Flask(__name__)

@app.route('/screen', methods=['POST'])
def screen():
    data = request.json
    result = screen_candidate(data['profile'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)
