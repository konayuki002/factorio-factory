# core/enums/ Enum識別子定義ファイル

## 目的
* 各種アイテムやレシピの識別子を定義し、Factorio Factoryの他の部分で利用できるようにします。
  - core/01_models/で定義される Pydantic モデルで構造を定義するために利用される識別子を提供します。

## 編集NG
* このファイルは自動生成されるため、手動での編集は行わないでください。
* 編集が必要な場合は、core/loader/converters/以下の変換モジュールや、core/utils/lua_parser.pyを修正し、再度変換`python3 -m core.loader build-all`を実行してください。