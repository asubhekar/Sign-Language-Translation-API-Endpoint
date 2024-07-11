from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        translated_text = f'Successful translation of simulated text: {text}'

        return jsonify({'message': 'Successful Translation', 'translated_text': translated_text}), 200

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
