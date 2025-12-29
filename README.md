# ml-inference-web-app
A simple inference web application built with Java and Python.

## Overview
This project is a personal learning project focused on building a simple web application where a Java client communicates with a Python-based inference service.
JavaとPythonを組み合わせたWebアプリケーション構成を学ぶための個人開発プロジェクトです。

## Current Status
- FastAPI-based inference endpoint implemented
- Endpoint: POST /infer
- Simple inference logic (x * 2) for initial validation
- Business logic separated into a dedicated module (logic.py)

## Tech Stack
- Java (Frontend / UI)
- Python (Backend / ML inference)
- REST API
- Git / GitHub

## Planned (Future Work)
- FastAPI
- scikit-learn
- SQLite

## System Architecture
- Java : ユーザー入力、画面表示、Python APIへのリクエスト送信を担当
- Python : データ処理、推論ロジックを担当(初期は簡易処理)
- DB : 推論結果の保存(予定)

## Processing Flow (Planned)
1. User inputs data via the Java UI
   →ユーザーがJava UIからデータを入力
2. Java sends a request to the Python REST API
   →JavaがPython REST APIにリクエストを送信
3. Python validates and preprocesses the input data
   →Python側で入力データを検証・前処理
4. Inference is performed(initially simple logic, later a trained ML model)
   →初期は簡易ロジックで推論し、将来的に学習済みMLモデルを使用
5. The inference result is stored in the database
    →推論結果をデータベースに保存
6. The result is returned to the Java UI and displayed to the user
    →結果をJava UIに返却し、ユーザーに表示


