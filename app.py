from flask import Flask, jsonify

app = Flask(__name__)  # Flask 애플리케이션 인스턴스를 생성

@app.route('/api', methods=['GET'])  # GET 요청을 받을 '/api' 엔드포인트 설정
def api():
    return jsonify(message="Hello, world!")  # 'message'라는 키를 가진 JSON 응답 반환

if __name__ == '__main__':
    app.run(debug=True)  # 애플리케이션 실행