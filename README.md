# hiro_robot_private

## 使用環境
<img src="https://img.shields.io/badge/-Flask-00000.svg?logo=flask&style=plastic">
<img src="https://img.shields.io/badge/-Python-3776AB.svg?logo=python&style=plastic">
<img src="https://img.shields.io/badge/-Javascript-F7DF1E.svg?logo=javascript&style=plastic">

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [セットアップ](#セットアップ)
3. [環境](#環境)
4. [使い方](#使い方)
5. [ファイルの内容](#ファイルの内容)



## プロジェクト名

癒しの赤ちゃんロボットシステム

<!-- プロジェクトについて -->

## プロジェクトについて


## セットアップ
以下のPythonライブラリが必須．必要なPythonバージョンなどは調べること

openai
flask
flask_socketio


## 環境

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

Python、Flask、chatGPT

<p align="right">(<a href="#top">トップへ</a>)</p>




## 使い方
1.system_1.pyを実行
2.http://127.0.0.1:5000/にアクセス
3.ページ上の「設定」に赤ちゃんロボットの設定（例：赤ちゃん、機嫌の良い赤ちゃん）を記入して、「反映」をクリック。
4.音声認識開始時に「Start」ボタンをクリック。
5.音声認識が終了するとChatGPTに認識結果を入力し，システム側が喃語の返答を返す
6.システム側の喃語の返答、自然言語の意味がページ上に追加され，喃語返答が合成音声で読み上げられる
7.合成音声の再生が終了すると，音声認識が再開され5.に戻る



<p align="right">(<a href="#top">トップへ</a>)</p>

## ファイルの内容

### system_1.py

提案システム。自然言語を出し、出した自然言語から喃語に変換。
変換時に音素数を揃えてバブバブと出力するようにプロンプトに指示。




