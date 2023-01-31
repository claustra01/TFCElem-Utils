import tfce_types
import tfce_utils

def register_tag():

    # ingots
    values = []
    for metal in tfce_types.metals:
        values.append("tfc:metal/ingot/" + metal[0])
    dir_path = "../src/main/resources/data/forge/tags/items"
    tfce_utils.create_simple_tag(dir_path, dir_path + "/ingots.json", values)
    dir_path = "../src/main/resources/data/tfc/tags/items"
    tfce_utils.create_simple_tag(dir_path, dir_path + "/pileable_ingots.json", values)
    
    # parts
    if metal[2]:
        for type in tfce_types.types_parts:
            values = []
            for metal in tfce_types.metals:
                values.append("tfc:metal/" + type[0] + "/" + metal[0])
            dir_path = "../src/main/resources/data/forge/tags/items"
            tfce_utils.create_simple_tag(dir_path, dir_path + "/" + type[0] + "s.json", values)
            if type == "sheet":
                dir_path = "../src/main/resources/data/tfc/tags/items"
                tfce_utils.create_simple_tag(dir_path, dir_path + "/pileable_sheets.json", values)


def register_metal():
    for metal in tfce_types.metals:
        
        dict = {}
        dir_path = "../src/main/resources/data/tfc/tfc/metals"
        file_path = dir_path + "/" + metal[0] + ".json"
        dict["tier"] = metal[6][0]
        dict["fluid"] = "tfc:metal/" + metal[0]
        dict["melt_temperature"] = metal[6][1]
        dict["specific_heat_capacity"] = metal[6][2]
        dict["ingots"] = {"tag" : "forge:ingots/" + metal[0]}
        dict["sheets"] = {"tag" : "forge:sheets/" + metal[0]}
        tfce_utils.create_dir(dir_path)
        tfce_utils.write_json(dict, file_path)
        
