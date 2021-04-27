from flask import Flask, jsonify, request
from video_predictor import run_prediction
app = Flask(__name__)


@app.route("/api", methods=['POST'])
def upload_video():

    if request.method == "POST":
        if request.files:
            video = request.files["video"]
            res = run_prediction(video)
            return jsonify({"result" : res})
        else:
            return jsonify({"result" : "file not found"})        
    return jsonify({"result" : "unknow error"}) 

if __name__ == '__main__': 
    app.run(threaded=True)  