from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from chatgpt import make_boin
from chatgpt import make_babbling_from_boin
from chatgpt import robot_reaction



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

#TODO 子音・母音に直してから直す

interview_list_file_1 = "interview_list_system_1.csv"
interview_list_file_2 = "interview_list_system_2.csv"
random_question_1 = "random_question_system_1.csv"
random_question_2 = "random_question_system_2.csv"
interview_file_log = "interview_system_log.csv"
interview_question = "interview_question.csv"
select_question_file = "select_question_file.csv"
question_number = 1
topic_file = "interview_topic_file.csv"

robot_setting = "baby"

@app.route('/')
def index():
    return render_template('system_2.html')


@socketio.on('connect')
def test_connect():
    print('Client connected')
    emit('interview_info',{'contents': "send finish"})
    # send() も Flask サーバーへイベントを送ることができるが，文字列またはjson型の標準メッセージをクライアントに送信


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')



@socketio.on('get_audio')
def get_audio(data):
    # print("type:" , type(data))
    # print("robot_setting : " , type(robot_setting))
    # print("data : " , type(data))
    robot_data = robot_reaction(str(data), robot_setting)
    setting_text = make_boin(robot_data , robot_setting)
    text = make_babbling_from_boin(setting_text , robot_setting)
    inner_text = setting_text
    # text = make_babbling(str(data))
    print("gpt_result:" , text)
    emit('get_gpt',
         {'data': text , "robot" : robot_data , "context":inner_text})

@socketio.on('get_information')
def get_information(data):
    # 受け取った音声認識結果を入力
    # gpt_result = chat(data['data'])
    # print('robot: ', gpt_result)
    # GPTの返答を表示
    print("OK, " + str(data))
    # emit('get_gpt',
    #      {'data': "こんにちは．これからインタビューよろしくお願いします．" })

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


if __name__ == '__main__':
    socketio.run(app)
