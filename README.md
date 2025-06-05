# factorio-factory

## Directory Structure

```
factorio_factory/
├── core/                           # 純粋なロジック (依存なし)
│   ├── 01_models/                  # Pydanticモデル
│   │   ├── 01_item_groups.py
│   │   ├── 02_item.py
│   │   ├── 03_recipe.py
│   │   └── 04_entities.py
│   ├── 02_logic/                   # 計算ロジック
│   │   ├── 01_recipe_graph.py
│   │   ├── 02_throughput.py
│   │   └── 03_machine_count.py
│   ├── 03_layout/                  # 配置とトポロジー
│   |   ├── 01_topology.py
│   |   └── 02_placer.py
|   ├── enum/                       # 識別子定義
│   |   ├── item_group.py           # アイテムグループの列挙型
|   |   ├── item_subgroup.py
|   |   └── manual_item_group.py    # 追加用ハードコード識別子の定義
│   ├── loader/                     # 識別子生成
│   |   ├── converters/             # 個別の変換ロジック
│   |   │   ├── base.py             # 変換のベースクラス
│   |   │   ├── enum/               # JSONからEnumへの変換
│   |   │   │   └── item_groups.py  
│   |   │   └── json/               # LuaからJSONへの変換
│   |   │       └── item_groups.py
│   |   ├── __init__.py             # パッケージ初期化
│   |   ├── __main__.py             # コマンドライン実行用
│   |   ├── config.py
│   |   └── registry.py             # 個別の変換ロジックの登録と順序管理
|   └── utils.py                    # ユーティリティ関数
├── data/                           # factorio-dataからのデータ抽出と変換
│   ├── fetcher.sh                  # wube/factorio-dataをcloneするスクリプト
│   ├── raw/                        # Luaデータのキャッシュ
│   |   ├── _factorio-data_cache/   # wube/factorio-data全体のキャッシュ
│   |   ├── items.lua               # 変換対象となる定義
│   |   ├── recipes.lua
│   |   ├── entities.lua
│   |   └── ...
|   └── intermediate/               # 中間変換データ
│       ├── item_groups.json        # アイテムグループのJson
│       └── item_subgroups.json
├── llm/                            # LLMとの連携機能
│   ├── prompts/                    # プロンプトテンプレート
│   └── tasks.py                    # LLMタスク定義と型バリデーション
├── plugins/                        # ユーザーが拡張できる場所
│   └── my_custom_layout.py
├── tools/                          # CLIやWeb UI用のツール
│   ├── cli.py
│   └── web_ui.py
├── examples/                       # 使用例・ノートブック
│   └── basic_use.ipynb
├── tests/                          # pytestテスト群
│   ├── test_model.py
│   ├── test_logic.py
│   └── test_layout.py
├── .gitignore                      # Git無視設定
├── requirements.txt                # 依存パッケージ
├── python-version.txt              # Pythonバージョン指定
├── README.md
└── mkdocs.yml                      # ドキュメント構成
```

## 前提
以下がインストール済みであることを前提とします.
1. **pyenv**
  - Pytnon 3.13.3 (あるいはそれ以降の3.13系) がインストールされていること.
  ```sh
  pyenv install 3.13.3 # もしまだインストールしていない場合
  pyenv local 3.13.3 # このプロジェクトのルートディレクトリで実行
  ```
  - `pyenv which python` で表示されるパスが `home/<username>/.pyenv/versions/3.13.3/bin/python` であることを確認してください.

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
CLIツールを使ってwube/factorio-dateのプロトタイプ定義をEnum識別子に変換することができます
```bash
python -m core.loader build-all
```

## 編集上の注意
`core/enums/`以下のファイルで, manual_*.py以外のファイルは自動生成されるため, 手動で編集しないでください.
* 編集NG: `item_group.py`           # アイテムグループの列挙型
* 編集NG: `item_subgroup.py`
* 編集OK: `manual_item_group.py`    # 追加用ハードコード識別子の定義

## テストの実行方法
テストはpytestを使って実行できます. 仮想環境を有効化した状態で以下を実行:
```bash
python -m pytest
```
