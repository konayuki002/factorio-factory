"""
Lua実行によるFactorioプロトタイプ抽出コンバータ
"""

import json
import logging
from pathlib import Path
from typing import Any

import lupa

from core.loader.converters.base import BaseConverter
from core.loader.registry import register

logger = logging.getLogger(__name__)


@register("lua:prototypes")
class LuaPrototypeExecutor(BaseConverter):
    """
    Factorioのcore/data.luaとbase/data.luaを実行して、
    data.rawからプロトタイプデータを抽出し、JSONファイルとして出力する
    """

    dependencies = []  # 最初に実行

    def load(self) -> None:
        """Lua実行してdata.rawからプロトタイプを抽出"""
        cache_dir = Path(self.raw_dir) / "_factorio-data_cache"

        if not cache_dir.exists():
            logger.warning(f"Cache directory not found: {cache_dir}")
            return

        lua = self._setup_lua_environment(cache_dir)

        # core/data.lua読み込み
        core_lua = cache_dir / "core/data.lua"
        if core_lua.exists():
            lua.execute(f"dofile('{core_lua}')")
            logger.info("Loaded core/data.lua")

        # util関数のモック化（core/data.lua読み込み後）
        self._mock_util_functions(lua)

        # base/data.lua読み込み
        base_lua = cache_dir / "base/data.lua"
        if base_lua.exists():
            lua.execute(f"dofile('{base_lua}')")
            logger.info("Loaded base/data.lua")

        # data.rawからプロトタイプを抽出してJSONとして保存
        self._extract_and_save_prototypes(lua)

    def _setup_lua_environment(self, cache_dir: Path) -> lupa.LuaRuntime:
        """Lua実行環境を設定"""
        lua = lupa.LuaRuntime()

        # package.path設定
        lua.execute(
            f'package.path = "{cache_dir}/?.lua;{cache_dir}/?/init.lua;{cache_dir}/core/?.lua;{cache_dir}/core/lualib/?.lua;{cache_dir}/base/?.lua;{cache_dir}/base/prototypes/?.lua;" .. package.path'
        )

        # カスタムrequire関数
        lua.execute(f"""
local original_require = require

require = function(module_name)
    if string.match(module_name, "^__core__%.lualib%.") then
        local file_name = string.gsub(module_name, "^__core__%.lualib%.", "")
        local file_path = "{cache_dir}/core/lualib/" .. file_name .. ".lua"
        return dofile(file_path)
    end
    
    if string.match(module_name, "^__core__/lualib/") then
        local file_name = string.gsub(module_name, "^__core__/lualib/", "")
        local file_path = "{cache_dir}/core/lualib/" .. file_name .. ".lua"
        return dofile(file_path)
    end
    
    if string.match(module_name, "^__base__/prototypes/") then
        local file_name = string.gsub(module_name, "^__base__/prototypes/", "")
        local file_path = "{cache_dir}/base/prototypes/" .. file_name .. ".lua"
        return dofile(file_path)
    end
    
    if string.match(module_name, "^__base__%.prototypes%.") then
        local file_name = string.gsub(module_name, "^__base__%.prototypes%.", "")
        file_name = string.gsub(file_name, "%.", "/")
        local file_path = "{cache_dir}/base/prototypes/" .. file_name .. ".lua"
        return dofile(file_path)
    end
    
    if string.match(module_name, "^__base__%.graphics%.") then
        return {{}}
    end
    
    if string.match(module_name, "^__base__/menu%-simulations/") then
        return {{}}
    end
    
    if string.match(module_name, "^graphics%.") then
        return {{}}
    end
    
    if string.match(module_name, "^__base__%.lualib%.") then
        local file_name = string.gsub(module_name, "^__base__%.lualib%.", "")
        local file_path = "{cache_dir}/base/lualib/" .. file_name .. ".lua"
        return dofile(file_path)
    end
    
    return original_require(module_name)
end
""")

        # defines定義（core/data.lua読み込み前に必要）
        lua.execute("""
defines = {
    direction = {
        north = 0, northnortheast = 1, northeast = 2, eastnortheast = 3,
        east = 4, eastsoutheast = 5, southeast = 6, southsoutheast = 7,
        south = 8, southsouthwest = 9, southwest = 10, westsouthwest = 11,
        west = 12, westnorthwest = 13, northwest = 14, northnorthwest = 15
    },
    entity_status = {
        working = 1, no_power = 2, no_fuel = 3, no_recipe = 4,
        no_input_fluid = 5, no_research_in_progress = 6,
        insufficient_input = 7, full_output = 8, no_ingredients = 9,
        no_minable_resources = 10, low_input_fluid = 11,
        disabled_by_control_behavior = 12, disabled_by_script = 13,
        marked_for_deconstruction = 14
    },
    inventory = {
        lab_modules = 1, lab_input = 2, chest = 3, fuel = 4,
        burnt_result = 5, assembling_machine_input = 6,
        assembling_machine_output = 7, assembling_machine_modules = 8,
        furnace_source = 9, furnace_result = 10, furnace_modules = 11,
        character_main = 12, character_guns = 13, character_ammo = 14,
        character_armor = 15, character_vehicle = 16, character_trash = 17
    }
}
""")

        # data構造定義
        lua.execute("""
data = {
    raw = {},
    extend = function(self, prototypes)
        for _, prototype in ipairs(prototypes) do
            if prototype.type and prototype.name then
                if not self.raw[prototype.type] then
                    self.raw[prototype.type] = {}
                end
                self.raw[prototype.type][prototype.name] = prototype
            end
        end
    end
}
""")

        return lua

    def _mock_util_functions(self, lua: lupa.LuaRuntime) -> None:
        """util関数をモック化"""
        lua.execute("""
if util then
    util.sprite_load = function(path, options)
        return {
            filename = path,
            width = options and options.width or 32,
            height = options and options.height or 32,
            priority = options and options.priority or "medium"
        }
    end
    util.by_pixel = util.by_pixel or function(value) return value end
    util.empty_sprite = util.empty_sprite or function() return {} end
end
""")

    def _extract_and_save_prototypes(self, lua: lupa.LuaRuntime) -> None:
        """data.rawからプロトタイプを抽出してJSONファイルとして保存"""
        try:
            # lua.globalsからdataテーブルを取得
            data_table = lua.globals().data
            raw_data = dict(data_table.raw)

            # 全プロトタイプを統合したprototypes.jsonを作成
            all_prototypes = {}

            for prototype_type, prototypes_table in raw_data.items():
                prototypes = dict(prototypes_table)
                if prototypes:
                    # Luaテーブルを辞書に変換
                    json_data = {}
                    for name, prototype in prototypes.items():
                        json_data[name] = self._lua_table_to_dict(prototype)

                    all_prototypes[prototype_type] = json_data
                    logger.info(
                        f"Processed {len(json_data)} {prototype_type} prototypes"
                    )

            # 統合プロトタイプファイルとして保存
            prototypes_path = Path(self.intermediate_dir) / "prototypes.json"
            with open(prototypes_path, "w", encoding="utf-8") as f:
                json.dump(all_prototypes, f, ensure_ascii=False, indent=2)

            logger.info(f"Saved all prototypes to {prototypes_path}")
            logger.info(f"Total prototype types: {len(all_prototypes)}")

        except Exception as e:
            logger.error(f"Failed to extract prototypes: {e}")
            raise

    def _lua_table_to_dict(self, lua_table: Any) -> Any:
        """LuaテーブルをPython辞書に変換し、Factorio特有の構造を正規化"""
        if not hasattr(lua_table, "items"):
            return lua_table

        result: dict[Any, Any] = {}
        try:
            for key, value in dict(lua_table).items():
                if hasattr(value, "items"):  # ネストしたテーブル
                    converted_value = self._lua_table_to_dict(value)
                    # Factorio特有の正規化を適用
                    result[key] = self._normalize_factorio_data(key, converted_value)
                else:
                    # Factorio特有の正規化を適用
                    result[key] = self._normalize_factorio_data(key, value)
        except Exception:
            return lua_table

        return result

    def _normalize_factorio_data(self, key: str, value: Any) -> Any:
        """Factorio特有のデータ構造を既存システム互換形式に正規化"""
        # crafting_categoriesは数値インデックスの辞書を配列に変換
        if key == "crafting_categories" and isinstance(value, dict):
            # {1: 'basic-crafting', 2: 'crafting'} → ['basic-crafting', 'crafting']
            try:
                # 数値キーでソートして配列に変換
                sorted_items = sorted(value.items(), key=lambda x: int(x[0]))
                return [item[1] for item in sorted_items]
            except (ValueError, TypeError):
                # 数値キーでない場合は値のリストを返す
                return list(value.values())

        # allowed_effectsも同様の処理
        if key == "allowed_effects" and isinstance(value, dict):
            try:
                sorted_items = sorted(value.items(), key=lambda x: int(x[0]))
                return [item[1] for item in sorted_items]
            except (ValueError, TypeError):
                return list(value.values())

        # ingredientsやresultsも同様の処理が必要な場合
        if key in ["ingredients", "results"] and isinstance(value, dict):
            try:
                sorted_items = sorted(value.items(), key=lambda x: int(x[0]))
                return [item[1] for item in sorted_items]
            except (ValueError, TypeError):
                return list(value.values())

        # その他の数値インデックス辞書を配列に変換
        if isinstance(value, dict) and all(
            isinstance(k, (int, str)) and str(k).isdigit() for k in value.keys()
        ):
            try:
                sorted_items = sorted(value.items(), key=lambda x: int(x[0]))
                return [item[1] for item in sorted_items]
            except (ValueError, TypeError):
                pass

        return value
