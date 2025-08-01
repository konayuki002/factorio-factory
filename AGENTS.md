# AGENTS.md

## コード管理
### ブランチ名
* ブランチ名は英語のスネークケースで書いてください。

### コミットメッセージ
* コミットメッセージは英語で書いてください。

## コード品質
### フォーマット
* このプロジェクトでは、コードのフォーマットにruffを使用しています。
* コードを変更した場合は、必ず`script/format.sh`を実行してコードのフォーマットを整えてください。
* フォーマッタの設定は`pyproject.toml`に記載されています。

### 静的型チェック
* このプロジェクトでは、静的型チェックを行うためにmypyを使用しています。
* コードを変更した場合は、必ず`mypy .`を実行して型チェックを行ってください。
* 型チェックの設定は`mypy.ini`に記載されています。

### テスト
* このプロジェクトでは、pytestを使用してテストを実行します。
* ロジックやテストを変更した場合は、必ず`pytest`を実行して`tests/`以下の全てのテストが通ることを確認してください。

### CI
* このプロジェクトでは、GitHub Actionsを使用してCIを実行します。
* プルリクエストを作成したり追加コミットをすると、CIが自動的に実行されます。
* 上記フォーマットチェック+静的型チェックと、ビルド+テストが並列で実行されます。
* CIの設定は`.github/workflows/ci.yml`に記載されています。

## 構成
* core/はプロジェクトのコアロジックを含むディレクトリです。
* data/はデータファイルを含むディレクトリです。
  - .gitignoreで除外されているため、Gitには含まれません。
* examples/はjupyter notebooksによって実行可能なコード例を含むディレクトリです。(作成前につき未実装)
* tests/はpytestを使用したテストコードを含むディレクトリです。
* llm/はLLM関連のコードを含むディレクトリです。(作成前につき未実装)
* plugins/はユーザーが独自のレイアウトを追加できる場所です。(作成前につき未実装)
* tools/はCLIやWeb UIなどのツールを含むディレクトリです。(作成前につき未実装)