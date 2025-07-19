# Lua実行ベースコンバータ統合設計

## 概要

従来の静的Lua解析ベース（`parse_lua_file`）から、lupaによるLua実行ベース（`LuaPrototypeExecutor`）への移行を行い、Space Age等の拡張や複雑な依存関係に対応できるシステムを構築する。

## アーキテクチャ設計

### 1. 新しいデータフロー

```
[Factorio Data] 
    ↓ (Lua実行)
[lua:prototypes] → data.raw → JSON抽出
    ↓ (依存関係)
[json:item, json:recipe, json:entities, ...]
    ↓ (既存フロー)
[models, enums, logic, layout]
```

### 2. コンバータ依存関係

```
lua:prototypes (最初に実行、dependencies=[])
    ↓
json:item (dependencies=["lua:prototypes"])
json:recipe (dependencies=["lua:prototypes"])  
json:entities (dependencies=["lua:prototypes"])
json:mining_drill (dependencies=["lua:prototypes"])
json:fluid (dependencies=["lua:prototypes"])
json:technology (dependencies=["lua:prototypes"])
    ↓
既存のenum/modelコンバータ（変更なし）
```

## 統合実装計画

### Phase 1: LuaPrototypeExecutorの完成 ✅

- [x] 基本的なLua実行環境構築
- [x] カスタムrequire関数（__core__, __base__対応）
- [x] グラフィック/シミュレーション系モック
- [x] data.raw抽出とJSON出力

### Phase 2: 各JSONコンバータの移行

各JSONコンバータを以下のパターンで更新：

```python
# 変更前（静的解析版）
from core.utils.lua_parser import parse_lua_file

@register("json:recipe")
class RecipeJsonConverter(BaseConverter):
    dependencies = []
    lua_filename = "recipe.lua"
    
    def load(self):
        lua_file = f"{self.raw_dir}/{self.lua_filename}"
        data = parse_lua_file(lua_file)
        # ...処理...

# 変更後（Lua実行版）
import json

@register("json:recipe")  
class RecipeJsonConverter(BaseConverter):
    dependencies = ["lua:prototypes"]
    
    def load(self):
        # lua:prototypesから生成されたprototypes.jsonを読み込み
        prototypes_file = f"{self.intermediate_dir}/prototypes.json"
        with open(prototypes_file, 'r') as f:
            all_prototypes = json.load(f)
        
        # recipeタイプのみ抽出・フィルタリング
        recipes = []
        for prototype in all_prototypes.get("recipe", {}).values():
            if prototype.get("subgroup") != "parameters":
                recipes.append(prototype)
        
        # 出力
        json_path = f"{self.intermediate_dir}/recipe.json"
        self.dump_json(recipes, json_path)
```

### Phase 3: 統合テストと検証

1. **データ整合性チェック**
   - 旧方式と新方式の出力JSON比較
   - 重要な属性（name, type, ingredients, results等）の一致確認

2. **パフォーマンステスト**
   - 実行時間測定
   - メモリ使用量確認

3. **拡張性テスト**
   - Space Age MOD追加時の動作確認
   - カスタムMODでの動作確認

### Phase 4: 最適化とクリーンアップ

1. **不要コードの削除**
   - `core/utils/lua_parser.py`の使用停止
   - 静的解析関連コードの削除
   - 不要な`raw/*.lua`ファイル参照の削除

2. **エラーハンドリング強化**
   - Lua実行エラーの適切な処理
   - 部分的失敗時の復旧機能

## 実装上の留意点

### 1. データ形式の統一

LuaPrototypeExecutorが出力する`prototypes.json`は以下の構造：

```json
{
  "item": {
    "iron-plate": { "name": "iron-plate", "type": "item", ... },
    "copper-plate": { "name": "copper-plate", "type": "item", ... }
  },
  "recipe": {
    "iron-plate": { "name": "iron-plate", "type": "recipe", ... }
  },
  "assembling-machine": { ... },
  "fluid": { ... }
}
```

各JSONコンバータは、必要なタイプのデータを抽出してリスト形式で出力。

### 2. エラーハンドリング戦略

```python
def load(self):
    try:
        # lua:prototypesの結果を読み込み
        prototypes_file = f"{self.intermediate_dir}/prototypes.json"
        if not Path(prototypes_file).exists():
            self.logger.error(f"Prototypes file not found: {prototypes_file}")
            return
            
        with open(prototypes_file, 'r') as f:
            all_prototypes = json.load(f)
            
    except Exception as e:
        self.logger.error(f"Failed to load prototypes: {e}")
        return
```

### 3. 移行の段階的実行

1. **一つずつ移行**: まず`json:recipe`から開始
2. **並行テスト**: 新旧両方を実行して結果比較
3. **段階的切り替え**: 検証完了したものから本格移行

## 期待される効果

### 1. 機能的改善
- Space Age等の複雑なMODサポート
- require依存関係の正確な解決
- 動的データ生成の対応

### 2. 保守性向上
- 静的解析の複雑なパースロジック削除
- 単一のLua実行環境による一貫性
- Factorioアップデート時の追従容易性

### 3. 拡張性向上
- 新しいプロトタイプタイプの自動対応
- カスタムMODの簡単な統合
- 将来のFactorio仕様変更への柔軟な対応

## 次のステップ

1. **json:recipe**コンバータの移行実装
2. 移行後の動作確認と整合性テスト  
3. 他のJSONコンバータの順次移行
4. 統合テストの実施とパフォーマンス評価
