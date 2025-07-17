from flask import Flask, request, jsonify
from emotion_analyzer import analyze_text_with_gemini, run_lighting_script
import argparse

app = Flask(__name__)

@app.route('/trigger-emotion', methods=['POST'])
def trigger_emotion():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Invalid request. 'text' field is required."}), 400

    text = data['text']
    duration = data.get('duration', 15)

    emotion, effect = analyze_text_with_gemini(text)

    if emotion and effect:
        run_lighting_script(emotion, effect, app.config['COM_PORT'], duration)
        return jsonify({"emotion": emotion, "effect": effect})
    else:
        return jsonify({"error": "Failed to determine valid emotion/effect."}), 500

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API for DMX lighting control.")
    parser.add_argument("-c", "--COM", type=str, required=True, help="COM port for Enttec DMX.")
    args = parser.parse_args()

    app.config['COM_PORT'] = args.COM
    app.run(host='0.0.0.0', port=5000)
