from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from chatgpt import make_babbling


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#TODO 直接喃語に直す

robot_setting = "baby"

interview_list_file_1 = "interview_list_system_1.csv"
interview_list_file_2 = "interview_list_system_2.csv"
random_question_1 = "random_question_system_1.csv"
random_question_2 = "random_question_system_2.csv"
interview_file_log = "interview_system_log.csv"
interview_question = "interview_question.csv"
select_question_file = "select_question_file.csv"
question_number = 1
topic_file = "interview_topic_file.csv"


@app.route('/')
def index():
    return render_template('system.html')


@socketio.on('connect')
def test_connect():
    print('Client connected')
    emit('interview_info',{'contents': "send finish"})
    # send() も Flask サーバーへイベントを送ることができるが，文字列またはjson型の標準メッセージをクライアントに送信


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('my_event')
def get_setteing(data):
    # 受け取った音声認識結果を入力
    # gpt_result = chat(data['data'])
    # print('robot: ', gpt_result)
    # GPTの返答を表示
    print("setting: " + str(data['data']))
    emit('robot_setting' , {'data' : str(data['data'])})
    # emit('get_gpt',
    #      {'data': "こんにちは．これからインタビューよろしくお願いします．" })

@socketio.on('get_robot_setting')
def get_robot_setting(data):
    global robot_setting
    robot_setting = data['data']

@socketio.on('get_audio')
def get_audio(data):
    # print("type:" , type(data))
    text = make_babbling(str(data), robot_setting)
    print("gpt_result:" , text)

    # ()とその中身を削除
    start_index = text.find("（")  # "("のインデックスを取得
    end_index = text.find("）")  # ")"のインデックスを取得
    if start_index != -1 and end_index != -1:  # ()が見つかった場合
        inner_text = text[start_index + 1:end_index]  # ()の中身を取得
        text = text[:start_index] + text[end_index + 1:]  # ()とその中身を削除

    print("text:", text)
    print("inner_text:", inner_text)

    emit('get_gpt',
         {'data': text , "context":inner_text})

@socketio.on('get_information')
def get_information(data):
    # 受け取った音声認識結果を入力
    # gpt_result = chat(data['data'])
    # print('robot: ', gpt_result)
    # GPTの返答を表示
    print("OK, " + str(data))
    # emit('get_gpt',
    #      {'data': "こんにちは．これからインタビューよろしくお願いします．" })


if __name__ == '__main__':
    socketio.run(app)
