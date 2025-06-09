# JsonConverter

## 目的
各モジュールはLua prototypeの各ファイルをJSON形式に変換するためのコンバータを提供します。
このコンバータは、Luaのデータ構造をJSONに変換し、Factorio Factoryの他の部分で利用できるようにします。

## 入出力の形式
### 入力
* 1つの Lua ファイル
* data/raw/ 以下に配置されている
### 出力
* 1つまたは複数の JSON ファイル
* data/intermediate/ 以下に配置される
