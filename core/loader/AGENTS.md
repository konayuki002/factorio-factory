# core/loader/AGENTS.md

# Loaderパッケージ全体ガイド (core/loader/)

## 目的
* Factorioデータ変換パイプラインの中核。Lua→JSON→Enum等の変換や、各種ロジック・設定・登録管理を担います。

## ディレクトリ構成
* converters/: 変換ロジックを提供するサブパッケージ。詳細はconverters/AGENTS.md参照。
* config.py: 変換やパイプライン全体の設定・パラメータ管理。
* registry.py: 変換器の登録・依存解決・順序管理。
* __init__.py: パッケージ初期化。
* __main__.py: コマンドラインエントリーポイント（python -m core.loader ... で実行）。
* AGENTS.md: このパッケージ全体の設計・役割ガイド（本ファイル）。

## 実装ガイド
- 新しい変換器やロジックを追加する場合は、converters/配下に実装し、registry.pyで登録してください。
- テスト・fixtureはtests/配下にまとめてください。
- CLIや設定の拡張はconfig.py, __main__.pyを参照。
