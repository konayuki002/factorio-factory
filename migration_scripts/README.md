# Migration Scripts

このディレクトリには、Factorioデータ変換基盤のLua実行ベース移行プロジェクトで使用された検証・分析スクリプトが含まれています。

## スクリプト一覧

### 分析・検証スクリプト
- `analyze_migration.py` - 移行前後のデータ差分分析
- `check_integration.py` - 統合動作確認
- `check_normalization.py` - データ正規化確認
- `check_fluid_structure.py` - fluidデータ構造確認
- `check_prototypes_fluid.py` - プロトタイプfluid確認
- `debug_data_types.py` - データ型デバッグ

### 基盤コード
- `lua_runtime.py` - Lua実行環境のプロトタイプ（現在は`core/loader/converters/lua_prototypes.py`に統合済み）

## 使用方法

これらのスクリプトは移行プロジェクト完了後の参考用です。必要に応じて、プロジェクトルートから実行してください：

```bash
# プロジェクトルートから実行
python migration_scripts/analyze_migration.py
```

## 注意

これらのスクリプトは移行時の一時的な検証用であり、通常のビルドプロセスには含まれません。
