from flask import Flask, request, jsonify
from services.verification import verify_user, verify_video
from services.alerts import send_alert

app = Flask(__name__)

@app.route('/api/verify_user', methods=['POST'])
def verify_user_route():
    data = request.json
    result = verify_user(data['user_id'])
    return jsonify(result)

@app.route('/api/verify_video', methods=['POST'])
def verify_video_route():
    data = request.json
    result = verify_video(data['video_id'])
    return jsonify(result)

@app.route('/api/send_alert', methods=['POST'])
def send_alert_route():
    data = request.json
    send_alert(data['message'])
    return jsonify({"status": "Alert sent"})

if __name__ == '__main__':
    app.run(debug=True)

