from flask import Flask
from flask_cors import CORS
from controllers.file_ops import move_file, copy_file, delete_file
from controllers.read_file import read_file

app = Flask(__name__)
app = Flask(__name__)
CORS(app)  # 👈 Allow all external requests


# 📂 List files in a directory
@app.route('/list_files', methods=['GET'])
def list_files():
    from flask import request, jsonify
    import os

    path = request.args.get('path', '.')
    if not os.path.exists(path):
        return jsonify({"error": "Path not found"}), 400
    return jsonify({"files": os.listdir(path)})

# ✏️ Move or Rename a File
@app.route('/move_file', methods=['POST'])
def api_move_file():
    return move_file()

# 📂 Copy a File
@app.route('/copy_file', methods=['POST'])
def api_copy_file():
    return copy_file()

# 📖 Read a file
@app.route('/read_file', methods=['GET'])
def api_read_file():
    return read_file()

# 🗑️ Delete a file
@app.route('/delete_file', methods=['POST'])
def api_delete_file():
    return delete_file()

# 🚀 Run the API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
