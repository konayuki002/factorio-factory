#!/bin/bash
# fetcher.sh: wube/factorio-data から item.lua, recipe.lua などを data/raw/ に取得するスクリプト
set -e

REPO_URL="https://github.com/wube/factorio-data.git"
# コマンドライン引数でバージョン指定可能（例: bash fetcher.sh 2.0.53）
VERSION="${1:-2.0.54}"
RAW_DIR="$(dirname "$0")/raw"
CACHE_DIR="$RAW_DIR/_factorio-data_cache"

# 取得したいLuaファイル一覧（必要に応じて追加）
FILES=(
  "base/prototypes/categories/recipe-category.lua"
  "base/prototypes/entity/entities.lua"
  "base/prototypes/entity/mining-drill.lua"
  "base/prototypes/entity/resources.lua"
  "base/prototypes/fluid.lua"
  "base/prototypes/item.lua"
  "base/prototypes/item-groups.lua"
  "base/prototypes/recipe.lua"
  "base/prototypes/technology.lua"
)

# rawディレクトリがなければ作成
test -d "$RAW_DIR" || mkdir -p "$RAW_DIR"

# キャッシュディレクトリがなければ作成し、権限を調整
if [ ! -d "$CACHE_DIR/.git" ]; then
  mkdir -p "$CACHE_DIR"
  chown "$(id -u):$(id -g)" "$CACHE_DIR"
  chmod 700 "$CACHE_DIR"
fi

# キャッシュディレクトリがなければclone、あればpullで更新
if [ ! -d "$CACHE_DIR/.git" ]; then
  echo "Cloning factorio-data ($VERSION) to cache..."
  git clone --depth 1 --branch "$VERSION" "$REPO_URL" "$CACHE_DIR"
  chown -R "$(id -u):$(id -g)" "$CACHE_DIR"
  chmod -R u+rwX "$CACHE_DIR"
else
  echo "Updating factorio-data cache to $VERSION..."
  git -C "$CACHE_DIR" fetch origin tag "$VERSION"
  git -C "$CACHE_DIR" checkout "tags/$VERSION"
  chown -R "$(id -u):$(id -g)" "$CACHE_DIR"
  chmod -R u+rwX "$CACHE_DIR"
fi

for FILE in "${FILES[@]}"; do
  SRC="$CACHE_DIR/$FILE"
  DST="$RAW_DIR/$(basename $FILE)"
  if [ -f "$SRC" ]; then
    if [ -f "$DST" ] && cmp -s "$SRC" "$DST"; then
      echo "Unchanged: $DST (skip)"
    else
      cp "$SRC" "$DST"
      echo "Copied: $FILE -> $DST"
    fi
  else
    echo "[ERROR] $FILE not found in repo (version: $VERSION)!" >&2
  fi

done

echo "Done."
