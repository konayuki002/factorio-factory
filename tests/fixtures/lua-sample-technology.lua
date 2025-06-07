data:extend({
  {
    type = "technology",
    name = "sample-tech-1",
    icon = "__base__/graphics/technology/sample-tech-1.png",
    icon_size = 128,
    prerequisites = {"automation"},
    effects = {
      { type = "unlock-recipe", recipe = "sample-recipe-1" }
    },
    unit = {
      count = 50,
      ingredients = {{"automation-science-pack", 1}},
      time = 15
    },
    order = "a-b-a"
  },
  {
    type = "technology",
    name = "sample-tech-2",
    icon = "__base__/graphics/technology/sample-tech-2.png",
    icon_size = 128,
    prerequisites = {"sample-tech-1"},
    effects = {
      { type = "unlock-recipe", recipe = "sample-recipe-2" }
    },
    unit = {
      count = 100,
      ingredients = {{"automation-science-pack", 1}, {"logistic-science-pack", 1}},
      time = 30
    },
    order = "a-b-b"
  }
})
