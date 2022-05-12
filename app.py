from flask import Flask,request,jsonify
import time
from myMediapipe import *
app = Flask(__name__)

# media pipe test
@app.route("/api2/mediapipe/mov")
def mediapipe_mov():
    face_detection_mov_mediapipe()
    return "Hello mov!"

@app.route("/api2/mediapipe/img")
def mediapipe_img():
    face_detection_img_mediapipe()
    return "Hello face"

# 실제 사용
@app.route("/api2/blur/step-1",methods=['POST'])
def hello_flask():
    #resA,resB = solution(img_src) byte
    content_type = request.headers.get('Content-Type')
    print(content_type)
    if (content_type == 'application/json'):
        data = request.get_json()
        #
        # {사진: , blur 제외할 사람 위치값 :, blur할 사람 위치값: }
        #
        #  {원본사진 : byte[],
        #   faceInfo:  [
        #     {사진1 : 
        #      위치 : {
        #         상: 
        #          하:
        #         좌: 
        #         우:
        #        },
        #    블러 여부: fale/true
        # }]
        # 
        #}
        # 
       
        return jsonify(photo=data['exPhotos'][0])
    
    return "abc"

@app.route("/api2/blur/step-1",methods=['GET'])
def hello_flask2():
    start_time = time.time()
    #resA,resB = solution(img_src)

    end_time = time.time()
    return "abc"

if __name__ == "__main__":
    app.run(debug=True)