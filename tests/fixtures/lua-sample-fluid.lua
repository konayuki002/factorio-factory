data:extend(
{
  {
    type = "fluid",
    name = "sample-fluid",
    subgroup = "fluid",
    default_temperature = 20,
    max_temperature = 100,
    heat_capacity = "1kJ",
    base_color = {0.8, 0.2, 0.2},
    flow_color = {0.9, 0.3, 0.3},
    icon = "__base__/graphics/icons/fluid/sample-fluid.png",
    order = "a[fluid]-c[sample]-b[fluid]",
  },
  {
    type = "fluid",
    name = "sample-fluid-2",
    subgroup = "fluid",
    default_temperature = 15,
    max_temperature = 80,
    heat_capacity = "0.5kJ",
    base_color = {0.2, 0.8, 0.2},
    flow_color = {0.3, 0.9, 0.3},
    icon = "__base__/graphics/icons/fluid/sample-fluid-2.png",
    order = "a[fluid]-c[sample]-c[fluid-2]",
  },
})
