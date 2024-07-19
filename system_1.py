from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from chatgpt import make_babbling_from_language
from chatgpt import make_language
import ast


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# 初期設定
robot_setting = "baby"

@app.route('/')
def index():
    return render_template('system_1.html')


@socketio.on('connect')
def test_connect():
    print('Client connected')
    emit('interview_info',{'contents': "send finish"})


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('get_audio')
def get_audio(data):
    global robot_setting
    setting_text = make_language(str(data) , robot_setting)
    print(setting_text )
    print(type(setting_text))
    if ':' in setting_text or '：' in setting_text:
        try:
            setting_text = ast.literal_eval(setting_text)
            setting = setting_text['assistant']
            setting_text = setting
        except ValueError:
            print("文字列を辞書に変換できませんでした。")
    print(setting_text)
    text = make_babbling_from_language(setting_text , robot_setting)
    print("text : " , text)
    print("type: " , type(text) )
    print("text : " , text)
    inner_text = setting_text
    print("gpt_result:" , text)
    emit('get_gpt',
         {'data': text , "context":inner_text})

@socketio.on('get_information')
def get_information(data):
    print("OK, " + str(data))

@socketio.on('my_event')
def get_setteing(data):
    print("setting: " + str(data['data']))
    emit('robot_setting' , {'data' : str(data['data'])})

@socketio.on('get_robot_setting')
def get_robot_setting(data):
    global robot_setting
    robot_setting = data['data']


if __name__ == '__main__':
    socketio.run(app)
