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
    ["double_ingot", 2],
    ["sheet", 2],
    ["double_sheet", 4],
    ["rod", 0.5]
]

types_tools = [
    ["tuyere", 4],
    ["fish_hook", 2],
    ["fishing_rod", 2],
    ["pickaxe", 1],
    ["pickaxe_head", 1],
    ["propick", 1],
    ["propick_head", 1],
    ["axe", 1],
    ["axe_head", 1],
    ["shovel", 1],
    ["shovel_head", 1],
    ["hoe", 1],
    ["hoe_head", 1],
    ["chisel", 1],
    ["chisel_head", 1],
    ["hammer", 1],
    ["hammer_head", 1],
    ["saw", 1],
    ["saw_blade", 1],
    ["javelin", 1],
    ["javelin_head", 1],
    ["sword", 2],
    ["sword_blade", 2],
    ["mace", 2],
    ["mace_head", 2],
    ["knife", 1],
    ["knife_blade", 1],
    ["scythe", 1],
    ["scythe_blade", 1],
    ["shears", 2],
    ["shield", 4]
]

types_armors = [
    ["helmet", 6],
    ["chestplate", 8],
    ["greaves", 6],
    ["boots", 4],
    ["unfinished_helmet", 4],
    ["unfinished_chestplate", 4],
    ["unfinished_greaves", 4],
    ["unfinished_boots", 2]
]