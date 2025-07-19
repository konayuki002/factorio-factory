# factorio-factory

**WIP**

## Directory Structure

```
factorio_factory/
├── core/                           # 純粋なロジック (依存なし)
│   ├── models/                     # Pydanticモデル
│   │   ├── models/                 # モデルの構造定義
│   │   ├── allowed/                # 包含関係の所属の定義
│   │   └── data/                   # モデルのデータ辞書の定義
│   ├── enum/                       # 識別子定義
│   ├── 02_logic/                   # 計算ロジック [未実装]
│   │   ├── 01_recipe_graph.py
│   │   ├── 02_throughput.py
│   │   └── 03_machine_count.py
│   ├── 03_layout/                  #  配置とトポロジー [未実装]
│   │   ├── 01_topology.py
│   │   └── 02_placer.py
│   ├── loader/
│   │   ├── converters/             # 個別の変換ロジック
│   │   │   ├── base.py             # 変換のベースクラス
│   │   │   ├── json/               # LuaからJSONへの変換
│   │   │   ├── enum/               # JSONからEnumのPythonコードへの変換
│   │   │   └── model/              # JSONからPydanticモデル用のPythonコードへの変換
│   │   │       ├── allowed/
│   │   │       └── data/
│   │   ├── __init__.py             # パッケージ初期化
│   │   ├── __main__.py             # コマンドライン実行用
│   │   ├── config.py
│   │   └── registry.py             # 個別の変換ロジックの登録と順序管理
│   └── utils.py                    # ユーティリティ関数
├── data/                           # factorio-dataからのデータ抽出と変換
│   ├── fetcher.sh                  # wube/factorio-dataをcloneするスクリプト
│   ├── raw/                        # Luaデータのキャッシュ
│   └── intermediate/               # 中間変換データ
├── llm/                            # LLMとの連携機能 [未実装]
│   ├── prompts/                    # プロンプトテンプレート
│   └── tasks.py                    # LLMタスク定義と型バリデーション
├── plugins/                        # ユーザーが拡張できる場所
│   └── my_custom_layout.py
├── tools/                          # CLIやWeb UI用のツール [未実装]
│   ├── cli.py
│   └── web_ui.py
├── examples/                       # 使用例・ノートブック
│   └── basic_use.ipynb
├── tests/                          # pytestテスト群
│   ├── fixtures/                   # テスト用のサンプルファイル
│   │   ├── enum/
│   │   └── json/
│   ├── test_enum_converter.py
│   ├── test_json_converter.py
│   ├── test_model.py
│   ├── test_logic.py
│   └── test_layout.py
├── .gitignore                      # Git無視設定
├── .python-version                 # Pythonバージョン指定
├── mypy.ini                        # 静的型チェック設定
├── pyproject.toml                  # フォーマッタ・リンタ設定
├── requirements.txt                # 依存パッケージ
├── README.md
└── mkdocs.yml                      # ドキュメント構成
```

## 前提
以下がインストール済みであることを前提とします.
1. **pyenv**
  - Python 3.13.3 (あるいはそれ以降の3.13系) がインストールされていること.
  ```sh
  pyenv install 3.13.3 # もしまだインストールしていない場合
  pyenv local 3.13.3 # このプロジェクトのルートディレクトリで実行
  ```
  - `pyenv which python` で表示されるパスが `~/.pyenv/versions/3.13.3/bin/python` であることを確認してください.

## セットアップ手順
1. 仮想環境を作成し, 有効化する
  - プロジェクトのルートディレクトリで以下を実行:
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

2. 依存パッケージをrequirements.txtからインストール
  ```sh
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
  
## 仮想環境を抜けるとき
仮想環境を抜けるには以下を実行:
```bash
deactivate
```

## CLIの使い方
CLIツールを使ってwube/factorio-dataのプロトタイプ定義をEnum識別子に変換することができます
```bash
python -m core.loader build-all
```

## 編集上の注意
`core/enums/`以下のファイルで, manual_*.py以外のファイルは自動生成されるため, 手動で編集しないでください.
* 編集NG: `item_group.py`           # アイテムグループの列挙型
* 編集NG: `item_subgroup.py`
* 編集OK: `manual_item_group.py`    # 追加用ハードコード識別子の定義

## 静的型チェック
静的型チェックはmypyを使って行います. 仮想環境を有効化した状態で以下を実行:
```bash
mypy .
```

## テストの実行方法
テストはpytestを使って実行できます. 仮想環境を有効化した状態で以下を実行:
```bash
pytest
```
