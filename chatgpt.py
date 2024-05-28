import openai
import sys


api_key = os.getenv("OPENAI_API_KEY")
default_messages = [{"role": "system",
                     "content": "exam"},  # プロンプトを入力
                    ]

next_messages = default_messages

# def make_babbling(input_text):
#     if input_text == "さようなら":
#         sys.exit()
#     client = openai.ChatCompletion.create(
#     model="gpt-4",
#     messages=[
#     {
#         "role": "system",
#         "content": "あなたは赤ちゃんです．\nUserに対する返答を「バ」と「ブ」のみを使用した赤ちゃん言葉で答えてください．ただし，「〜」は使用しないでください．また，（）の中に内容を答えてください．\n\n\n"
#     },
#     {
#         "role": "user",
#         "content": input_text
#     }
#     ],
#     temperature=0,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#     )
#     # 生成されたテキストを取得
#     generated_text = client['choices'][0]['message']['content']
#     return generated_text

def make_babbling(input_text , setting):
    if input_text == "さようなら":
        sys.exit()
    client = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "あなたは" + setting + "です．\nUserに対する返答を「バ」や「ブ」などを使用した赤ちゃん言葉で答えてください．ただし，最後に（）の中に内容を答えてください．\n\n\n"
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # 生成されたテキストを取得
    generated_text = client['choices'][0]['message']['content']
    return generated_text

def make_babbling_from_language(input_text , setting):
    if input_text == "さようなら":
        sys.exit()
    client = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                # 音素数を合わせる
                # "content": "あなたは" + setting + "です．\nUserの言葉を喃語に直してください．\n喃語にする際は，【例】に従って音素数を同じにしてください．\n\n【例】\nUser：お腹すいた\nAssistant：おあああああ\n\nUser：だっこして\nAssistant：だっだいえ\n\nUser：だいすき\nAssistant：だだだだ\n\n"
                # 最初の文字を伸ばす
                # "content": "あなたは" + setting + "です．\nUserの言葉を喃語に直してください．\n喃語にする際は，【例】に従ってください．\n\n【例】\nUser：お腹すいた\nAssistant：おーあー\n\nUser：だっこして\nAssistant：あーあえー\n\nUser：だいすき\nAssistant：あーいー"
                # 今までの喃語変換
                # "content": "あなたは" + setting + "です．\nUserの言葉を「バ」や「ブ」などを使用した赤ちゃん言葉に直してください．"
                # 音素数を合わせてバブバブ
                "content": "あなたは" + setting + "です．\nUserの言葉を喃語に直してください．\n喃語にする際は，【例】に従って音素数を同じにしてください．\n\n【例】\nUser：お腹すいた\nAssistant：バブバブバブ\n\nUser：だっこして\nAssistant：バッバブバ\n\nUser：だいすき\nAssistant：バブバブ"
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # 生成されたテキストを取得
    generated_text = client['choices'][0]['message']['content']
    return generated_text

def make_babbling_from_boin(input_text , setting):
    if input_text == "さようなら":
        sys.exit()
    client = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "あなたは" + setting + "です．\nUserの言葉を「バ」や「ブ」などを使用した赤ちゃん言葉で答えてください．\n\n"
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # 生成されたテキストを取得
    generated_text = client['choices'][0]['message']['content']
    return generated_text

def make_boin(input_text, setting):
    if input_text == "さようなら":
        sys.exit()
    client = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "あなたは" + setting + "です．\nUserの言葉を母音のみを使用した言葉に変えてください．\n"
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # 生成されたテキストを取得
    generated_text = client['choices'][0]['message']['content']
    return generated_text

def robot_reaction(input_text , setting):
    if input_text == "さようなら":
        sys.exit()
    client = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "あなたは" + setting + "です．\nUserの呼びかけに対する言葉を10字以内の日本語で答えてください．\n\n"
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # 生成されたテキストを取得
    generated_text = client['choices'][0]['message']['content']
    return generated_text

def make_language(input_text , setting):
    if input_text == "さようなら":
        sys.exit()
    client = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                # "content": "あなたは、" + setting + "です。Userの呼びかけに対する" + setting + "の心の言葉を10字以内で答えてください．\n\n"
                "content": "Userの呼びかけに対する" + setting + "の心の言葉を10字以内で答えてください．\n\n"
            },
            {
                "role": "user",
                "content": input_text
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # 生成されたテキストを取得
    generated_text = client['choices'][0]['message']['content']
    return generated_text


# chatGPTに音声認識結果を入力し，返答を得る
def chat(input_text):
    if input_text == "さようなら":
        sys.exit()

    next_messages.append({"role": "user",
                          "content": input_text})

    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=next_messages,
    )

    next_messages.append({"role": "assistant",
                          "content": res["choices"][0]["message"]["content"]})

    # GPTの返答
    return res["choices"][0]["message"]["content"]


if __name__ == '__main__':
    # キーボード入力での動作確認用
    input_text = input('user: ')
    res, a = make_babbling(input_text)
    print('robot: ' + res)
