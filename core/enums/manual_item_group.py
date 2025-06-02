# 例）JSON に存在しない「特別カテゴリ」を定義
MANUAL_MEMBERS: dict[str, list[str]] = {
    "item_group": ["unmined-resource", "technology"],
    "item_subgroup": [
        "unmined-resource-basic-solid",
        "unmined-resource-basic-fluid",
        "technology",
    ],
}
