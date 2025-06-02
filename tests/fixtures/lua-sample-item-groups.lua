data:extend(
{
-------------------------------------------------------------------------- GROUP1
  {
    type = "item-group",
    name = "group1",
    order = "a",
    icon = "__base__/graphics/item-group/group1.png",
    icon_size = 128,
  },
  {
    type = "item-subgroup",
    name = "subgroup1-1",
    group = "group1",
    order = "a"
  },
  {
    type = "item-subgroup",
    name = "subgroup1-2",
    group = "group1",
    order = "b"
  },
-------------------------------------------------------------------------- GROUP2
  {
    type = "item-group",
    name = "group2",
    order = "b",
    icon = "__base__/graphics/item-group/group2.png",
    icon_size = 128,
  },
  {
    type = "item-subgroup",
    name = "subgroup2-1",
    group = "group2",
    order = "a"
  },
  {
    type = "item-subgroup",
    name = "subgroup2-2",
    group = "group2",
    order = "b"
  },
})