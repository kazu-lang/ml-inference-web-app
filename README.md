# ml-inference-web-app
Machine learning inference web app built with Java and Python.

## Overview
This project is a machine learning inference web application built with Java and Python.

Javaでユーザー入力と結果表示を担当し、
Python(FastAPI)で前処理・機械学習推論・結果保存を行います。

## Tech Stack
- Java (Frontend / UI)
- Python (Backend / ML inference)
- FastAPI
- scikit-learn
- SQLLite
- REST API

## System Architecture
- Java : User interface and request handling
  →ユーザー入力・リクエスト制御を担当
- Python : Data preprocessing and ML inference
  →前処理および機械学習の推論処理
- DB : Persistence of inference results
  →推論結果の保存

## Processing Flow
1. User inputs data via the Java UI
   →ユーザーがJava UIからデータを入力
2. Java sends a request to the Python REST API
   →JavaがPython REST APIにリクエストを送信
3. Python validates and preprocesses the input data
   →Python側で入力データを検証・前処理
4. The trained ML model performs inference
   →学習済みMLモデルで推論を実行
5. The inference result is stored in the database
    →推論結果をデータベースに保存
6. The result is returned to the Java UI and displayed to the user
    →結果をJava UIに返却し、ユーザーに表示


