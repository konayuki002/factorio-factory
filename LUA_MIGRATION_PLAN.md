# Lua実行ベースコンバータへの移行計画

## Phase 1: 基盤構築 ✅
- [x] LuaPrototypeExecutor作成
- [x] カスタムrequire関数実装
- [x] data.raw抽出機能

## Phase 2: 既存コンバータ更新 ✅
- [x] json:item → lua:prototypesに依存変更
- [x] json:recipe → lua:prototypesに依存変更
- [x] json:entities → lua:prototypesに依存変更
- [x] json:mining_drill → lua:prototypesに依存変更
- [x] json:fluid → lua:prototypesに依存変更
- [x] json:technology → lua:prototypesに依存変更
- [x] json:item_group → lua:prototypesに依存変更
- [x] json:resource → lua:prototypesに依存変更
- [x] json:recipe_category → lua:prototypesに依存変更
- [x] json:resource_category → lua:prototypesに依存変更

## Phase 3: 静的解析コードの削除 ✅
- [x] 各JSONコンバータのLua解析コード削除
- [x] lua_parser依存関係の削除
- [x] 不要なraw/*.luaファイル参照の削除

## Phase 4: 検証・最適化
- [ ] データ整合性チェック
- [ ] パフォーマンス測定
- [ ] エラーハンドリング改善
- [ ] Space-Age対応テスト

## 変更が必要なファイル

### 新規作成
- core/loader/converters/lua_prototypes.py ✅

### 更新対象 ✅
- core/loader/converters/json/item.py ✅
- core/loader/converters/json/recipe.py ✅
- core/loader/converters/json/entities.py ✅
- core/loader/converters/json/mining_drill.py ✅
- core/loader/converters/json/fluid.py ✅
- core/loader/converters/json/technology.py ✅
- core/loader/converters/json/item_groups.py ✅
- core/loader/converters/json/resource.py ✅
- core/loader/converters/json/recipe_category.py ✅
- core/loader/converters/json/resource_category.py ✅

### 削除完了（Phase 3）
- core/utils/lua_parser.py ✅ 削除済み
- data/raw/*.lua (静的解析版) ✅ 削除済み

## リスク・注意点

1. **データ形式の差異**: Lua実行結果と静的解析結果でデータ構造が異なる可能性
2. **パフォーマンス**: Lua実行は静的解析より重い
3. **エラーハンドリング**: Lua実行時のエラーを適切に処理
4. **依存関係**: lupaライブラリの追加が必要

## 検証項目

- [ ] 生成されるJSON構造が既存と同じか
- [ ] プロトタイプ数が期待値と一致するか
- [ ] Space-Age追加コンテンツが含まれるか
- [ ] ビルド・テストが通るか
