import os
from flask import request, Response, jsonify

# 📖 Read a file with pagination
def read_file():
    file_path = request.args.get('file_path')
    start_line = int(request.args.get('start', 0))  # Default: Start from line 0
    num_lines = int(request.args.get('lines', 100))  # Default: Read 100 lines

    if not file_path:
        return jsonify({"error": "No file path provided"}), 400
    if not os.path.isfile(file_path):
        return jsonify({"error": f"File not found: {file_path}"}), 400

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            total_lines = len(lines)
            end_line = min(start_line + num_lines, total_lines)
            selected_lines = lines[start_line:end_line]

        return jsonify({
            "total_lines": total_lines,
            "start_line": start_line,
            "end_line": end_line,
            "content": selected_lines
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
