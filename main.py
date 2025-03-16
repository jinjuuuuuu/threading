import threading
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

def task1(data):
    print(f"Task 1 - {data} 시작")
    time.sleep(5)
    print(f"Task 1 - {data} 완료")

def task2(data):
    print(f"Task 2 - {data} 시작")
    time.sleep(3)
    print(f"Task 2 - {data} 완료")

@app.route('/start', methods=['POST'])
def start_task():
    data = request.json.get("input")

    thread1 = threading.Thread(target=task1, args=(data,))
    thread2 = threading.Thread(target=task2, args=(data,))

    thread1.start()
    thread2.start()

    return jsonify({"message": "작업이 시작되었습니다."}), 202

if __name__ == '__main__':
    app.run(debug=True)
