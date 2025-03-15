import os
import shutil
from flask import request, jsonify

# ✏️ Move or Rename a File
def move_file():
    data = request.json
    src = data.get('src')
    dest = data.get('dest')

    if not src or not dest or not os.path.exists(src):
        return jsonify({"error": "Invalid source or destination path"}), 400

    try:
        os.rename(src, dest)
        return jsonify({"message": f"Moved {src} to {dest} successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 📂 Copy a File
def copy_file():
    data = request.json
    src = data.get('src')
    dest = data.get('dest')

    if not src or not dest or not os.path.exists(src):
        return jsonify({"error": "Invalid source or destination path"}), 400

    try:
        shutil.copy2(src, dest)
        return jsonify({"message": f"Copied {src} to {dest} successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 🗑️ Delete a file with confirmation
def delete_file():
    file_path = request.json.get('file_path')
    
    if not file_path or not os.path.isfile(file_path):
        return jsonify({"error": "Invalid file path"}), 400

    confirmation = request.json.get('confirm', False)
    if not confirmation:
        return jsonify({"warning": "Deletion requires confirmation"}), 400

    try:
        os.remove(file_path)
        return jsonify({"message": f"Deleted {file_path} successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
