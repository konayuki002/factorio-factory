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
├── pyproject.toml                  # Poetryなどの設定
├── README.md
└── mkdocs.yml                      # ドキュメント構成
```
