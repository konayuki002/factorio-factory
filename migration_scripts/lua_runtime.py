from pathlib import Path
from typing import Any, Dict

import lupa

cache_dir = Path("data/raw/_factorio-data_cache")


lua = lupa.LuaRuntime(unpack_returned_tuples=True)

lua.execute(
    f"""
    package.path = "{cache_dir}/?.lua;{cache_dir}/?/init.lua;{cache_dir}/core/?.lua;{cache_dir}/core/lualib/?.lua;{cache_dir}/base/?.lua;{cache_dir}/base/prototypes/?.lua;" .. package.path
"""
)

# カスタムrequire関数（__core__、__base__対応）
lua.execute(
    f"""
    local original_require = require
    
    require = function(module_name)
        -- __core__.lualib.xxx を core/lualib/xxx.lua に変換（ドット区切り）
        if string.match(module_name, "^__core__%.lualib%.") then
            local file_name = string.gsub(module_name, "^__core__%.lualib%.", "")
            local file_path = "{cache_dir}/core/lualib/" .. file_name .. ".lua"
            return dofile(file_path)
        end
        
        -- __core__/lualib/xxx を core/lualib/xxx.lua に変換（スラッシュ区切り）
        if string.match(module_name, "^__core__/lualib/") then
            local file_name = string.gsub(module_name, "^__core__/lualib/", "")
            local file_path = "{cache_dir}/core/lualib/" .. file_name .. ".lua"
            return dofile(file_path)
        end
        
        -- __base__/prototypes/xxx を base/prototypes/xxx.lua に変換（スラッシュ区切り）
        if string.match(module_name, "^__base__/prototypes/") then
            local file_name = string.gsub(module_name, "^__base__/prototypes/", "")
            local file_path = "{cache_dir}/base/prototypes/" .. file_name .. ".lua"
            return dofile(file_path)
        end
        
        -- __base__.prototypes.xxx を base/prototypes/xxx.lua に変換（ドット区切りをスラッシュに）
        if string.match(module_name, "^__base__%.prototypes%.") then
            local file_name = string.gsub(module_name, "^__base__%.prototypes%.", "")
            -- ドット区切りをスラッシュに変換
            file_name = string.gsub(file_name, "%.", "/")
            local file_path = "{cache_dir}/base/prototypes/" .. file_name .. ".lua"
            return dofile(file_path)
        end
        
        -- __base__.graphics.xxx はグラフィックファイルなのでダミーテーブルを返す
        if string.match(module_name, "^__base__%.graphics%.") then
            return {{}} -- 空のテーブルの配列を返す（グラフィック定義として）
        end
        
        -- __base__/menu-simulations/xxx はシミュレーションファイルなのでダミーテーブルを返す
        if string.match(module_name, "^__base__/menu%-simulations/") then
            return {{}} -- 空のテーブルを返す（シミュレーション定義として）
        end
        
        -- graphics.xxx（プレフィックスなし）もグラフィックファイルなのでダミーテーブルを返す
        if string.match(module_name, "^graphics%.") then
            return {{}} -- 空のテーブルの配列を返す（グラフィック定義として）
        end
        
        -- __base__.lualib.xxx を base/lualib/xxx.lua に変換
        if string.match(module_name, "^__base__%.lualib%.") then
            local file_name = string.gsub(module_name, "^__base__%.lualib%.", "")
            local file_path = "{cache_dir}/base/lualib/" .. file_name .. ".lua"
            return dofile(file_path)
        end
        
        return original_require(module_name)
    end
"""
)

lua.execute(
    """
        defines = {
            direction = {
                north = 0,
                northnortheast = 1,
                northeast = 2,
                eastnortheast = 3,
                east = 4,
                eastsoutheast = 5,
                southeast = 6,
                southsoutheast = 7,
                south = 8,
                southsouthwest = 9,
                southwest = 10,
                westsouthwest = 11,
                west = 12,
                westnorthwest = 13,
                northwest = 14,
                northnorthwest = 15 
            },
            entity_status = {
                working = 1,
                no_power = 2,
                no_fuel = 3,
                no_recipe = 4,
                no_input_fluid = 5,
                no_research_in_progress = 6,
                insufficient_input = 7,
                full_output = 8,
                no_ingredients = 9,
                no_minable_resources = 10,
                low_input_fluid = 11,
                disabled_by_control_behavior = 12,
                disabled_by_script = 13,
                marked_for_deconstruction = 14
            },
            inventory = {
                lab_modules = 1,
                lab_input = 2,
                chest = 3,
                fuel = 4,
                burnt_result = 5,
                assembling_machine_input = 6,
                assembling_machine_output = 7,
                assembling_machine_modules = 8,
                furnace_source = 9,
                furnace_result = 10,
                furnace_modules = 11,
                character_main = 12,
                character_guns = 13,
                character_ammo = 14,
                character_armor = 15,
                character_vehicle = 16,
                character_trash = 17
            }
        }
    """
)

lua.execute(
    """
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
    """
)

core_lua = cache_dir / "core/data.lua"
base_lua = cache_dir / "base/data.lua"

lua.execute(f"dofile('{core_lua}')")

# core/data.lua読み込み後にutil関数をモック化
lua.execute(
    """
        -- util.sprite_loadなどのグラフィック関連関数をモック化
        if util then
            local original_sprite_load = util.sprite_load
            util.sprite_load = function(path, options)
                -- グラフィックファイルの読み込みをスキップし、空のテーブルを返す
                return {
                    filename = path,
                    width = options and options.width or 32,
                    height = options and options.height or 32,
                    priority = options and options.priority or "medium"
                }
            end
            
            -- その他のutil関数もモック化（必要に応じて）
            util.by_pixel = util.by_pixel or function(value) return value end
            util.empty_sprite = util.empty_sprite or function() return {} end
        end
    """
)
lua.execute(f"dofile('{base_lua}')")

# data.rawの内容を確認
print("=== Factorio Data Successfully Loaded ===")

# data.extendのデバッグを先に行う
lua.execute(
    """
    print("Checking data structure:")
    if data then
        print("data exists")
        if data.raw then
            print("data.raw exists")
            local count = 0
            for k, v in pairs(data.raw) do
                count = count + 1
                local item_count = 0
                for _, _ in pairs(v) do
                    item_count = item_count + 1
                end
                if item_count > 0 then
                    print("  " .. k .. ": " .. item_count .. " items")
                end
            end
            print("Total types in data.raw: " .. count)
        else
            print("data.raw is nil")
        end
    else
        print("data is nil")
    end
"""
)

# プロトタイプタイプの一覧を表示
raw_data = dict(lua.globals().data.raw)
print(f"\nTotal prototype types: {len(raw_data)}")

# 実際にデータが入っているタイプを確認
non_empty_types = {}
for k, v in raw_data.items():
    v_dict = dict(v)
    if len(v_dict) > 0:
        non_empty_types[k] = len(v_dict)

print(f"Non-empty prototype types: {len(non_empty_types)}")

if non_empty_types:
    print("Types with data:")
    for prototype_type, count in sorted(non_empty_types.items()):
        print(f"  {prototype_type}: {count} items")
else:
    print("No data found! This suggests data.extend was not called properly.")

print("\n=== Data loading completed! ===")
