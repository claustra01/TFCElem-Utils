rocks = [
    "granite",
    "diorite",
    "gabbro",
    "shale",
    "claystone",
    "limestone",
    "conglomerate",
    "dolomite",
    "chert",
    "chalk",
    "rhyolite",
    "basalt",
    "andesite",
    "dacite",
    "quartzite",
    "slate",
    "phyllite",
    "schist",
    "gneiss",
    "marble"
]

ores = [
    # name, isGraded, metalName, hardness(wood/stone/iron/diamond/netherite)
    ["native_platinum", True, "platinum", "diamond"],
    ["bauxite", True, "aluminum", "iron"],
    ["native_osmium", True, "osmium", "diamond"]
]

grades = [
    "poor",
    "normal",
    "rich"
]

metals = [
    # name, enableTool, enablePart, enableArmor, enableUtility, [textureType(iron/silver/steel), h, s, v],
    # [tier, melt_temp, sp_heat_cap, base_heat_cap]
    ["lead", False, True, False, False, ["iron", 119, 25, -28],
     [2, 328, 0.02143, 2.857]],
    ["platinum", False, True, False, False, ["silver", 106, 46, 0],
     [6, 1768, 0.005, 0.667]],
    ["electrum", False, True, False, False, ["silver", 22, 163, 0],
     [3, 1064, 0.00857, 0.833]],
    ["invar", False, True, False, False, ["iron", 30, 18, 0],
     [4, 1687, 0.00857, 1.143]],
    ["constantan", False, True, False, False, ["iron", 6, 114, 0],
     [4, 1207, 0.00625, 1.143]],
    ["signalum", False, True, False, False, ["steel", 10, 255, -18],
     [5, 1080, 0.00857, 1.143]],
    ["lumium", False, True, False, False, ["steel", 25, 149, 3],
     [5, 961, 0.00625, 0.833]],
    ["enderium", False, True, False, False, ["steel", 94, 255, -28],
     [6, 1768, 0.005, 0.667]],
    ["aluminum", False, True, False, False, ["iron", 91, 35, 0],
     [5, 660, 0.00857, 1.143]],
    ["uranium", False, True, False, False, ["iron", 50, 165, -28],
     [6, 1132, 0.02143, 2.857]],
    ["osmium", False, True, False, False, ["iron", 95, 43, 0],
     [6, 3033, 0.02143, 2.857]],
    ["refined_obsidian", False, True, False, False, ["steel", -148, 18, 0],
     [6, 3033, 0.02143, 2.857]],
    ["refined_glowstone", False, True, False, False, ["steel", -148, 18, 0],
     [6, 3033, 0.02143, 2.857]],
]

types_parts = [
    "double_ingot",
    "sheet",
    "double_sheet",
    "rod"
]

types_tools = [
    "tuyere",
    "fish_hook",
    "fishing_rod",
    "pickaxe",
    "pickaxe_head",
    "propick",
    "propick_head",
    "axe",
    "axe_head",
    "shovel",
    "shovel_head",
    "hoe",
    "hoe_head",
    "chisel",
    "chisel_head",
    "hammer",
    "hammer_head",
    "saw",
    "saw_blade",
    "javelin",
    "javelin_head",
    "sword",
    "sword_blade",
    "mace",
    "mace_head",
    "knife",
    "knife_blade",
    "scythe",
    "scythe_blade",
    "shears",
    "shield"
]

types_armors = [
    "helmet",
    "chestplate",
    "greaves",
    "boots",
    "unfinished_helmet",
    "unfinished_chestplate",
    "unfinished_greaves",
    "unfinished_boots"
]