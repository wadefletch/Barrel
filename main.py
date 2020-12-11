from flask import Flask, send_file, abort, request, jsonify
import os

DATA_DIR = 'data/'

app = Flask(__name__)

@app.route('/<file>', methods=['GET', 'POST'])
def get_barrel(file: str):
    path = os.path.join(DATA_DIR, file)

    if (request.method == 'GET') and (file in os.listdir(DATA_DIR)):
        return send_file(path)
    if request.method == 'POST':
        with open(path, 'wb') as f:
            f.seek(0)
            f.write(request.get_data())
            f.truncate()
            return jsonify({'success': 200})
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=False)