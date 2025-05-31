# factorio-factory

## Directory Structure

```
factorio_factory/
├── core/                           # 純粋なロジック (依存なし)
│   ├── 01_models/                  # Pydanticモデル
│   │   ├── 01_item.py
│   │   ├── 02_recipe.py
│   │   └── 03_entity.py
│   ├── 02_logic/                   # 計算ロジック
│   │   ├── 01_recipe_graph.py
│   │   ├── 02_throughput.py
│   │   └── 03_machine_count.py
│   └── 03_layout/                  # 配置とトポロジー
│       ├── 01_topology.py
│       └── 02_placer.py
├── data/                           # factorio-dataからのデータ抽出と変換
│   ├── loader.py                   # Luaデータ -> Pythonモデル変換
│   ├── fetcher.sh                  # wube/factorio-dataをcloneするスクリプト
│   └── raw/                        # Luaデータのキャッシュ
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
