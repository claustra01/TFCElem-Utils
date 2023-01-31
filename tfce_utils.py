import json
import os
import tfce_types

# read json
def read_json (file_path) -> dict:
    f = open(file_path, "r")
    dict = json.load(f)
    f.close
    return dict


# write json
def write_json(dict, file_path):
    f = open(file_path, "w")
    json.dump(dict, f, indent=2, ensure_ascii=False)
    f.close()
    
    
# create directory
def create_dir(dir_path):
    os.makedirs(dir_path, exist_ok=True)


# create nested dict
def create_nested_dict(list, val, dict, n=0):
    if n < len(list) - 1:
        dict[list[n]] = {}
        create_nested_dict(list, val, dict[list[n]], n + 1)
    else:
        dict[list[n]] = val
        

# ore to metal
def ore_to_metal(ore):
    for metal in tfce_types.metals:
        if ore[2] == metal[0]:
            return metal
    return None
  
      
# create simple state
def create_simple_state(dir_path, file_path, model_path):
    dict = {}
    create_dir(dir_path)
    create_nested_dict(["variants", "", "model"], model_path, dict)
    write_json(dict, file_path)


# create custom block model
def create_custom_block_model(dir_path, file_path, dict):
    create_dir(dir_path)
    write_json(dict, file_path)
    
    
# create simple blockitem model
def create_simple_blockitem_model(dir_path, file_path, parent_path):
    dict = {}
    dict["parent"] = parent_path
    create_dir(dir_path)
    write_json(dict, file_path)


# create simple item model
def create_simple_item_model(dir_path, file_path, texture_path):
    dict = {}
    dict["parent"] = "item/generated"
    create_nested_dict(["textures", "layer0"], texture_path, dict)
    create_dir(dir_path)
    write_json(dict, file_path)    


# create simple tag
def create_simple_tag(dir_path, file_path, values):
    dict = {}
    dict["replace"] = False
    dict["values"] = values
    create_dir(dir_path)
    write_json(dict, file_path) 


# heat registerer
def heat_registerer(dir_path, file_path, values, metal, cons):
    dict = {}
    dict["ingredient"] = values
    dict["heat_capacity"] = round(metal[6][3] * cons, 3)
    dict["forging_temperature"] = round(metal[6][1] * 0.6)
    dict["welding_temperature"] = round(metal[6][1] * 0.8)
    create_dir(dir_path)
    write_json(dict, file_path)


# anvil recipe
def create_anvil_recipe(file_path, input, output, count, tier, rules):
    dict = {}
    dict["type"] = "tfc:anvil"
    dict["input"] = {"tag":input}
    dict["result"] = {"item":output, "count":count}
    dict["tier"] = tier
    dict["rules"] = rules
    create_dir("../src/main/resources/data/tfc/recipes/anvil")
    write_json(dict, file_path)


# casting recipe
def create_casting_recipe(file_path, mold, fluid, amount, output, break_chance):
    dict = {}
    dict["type"] = "tfc:casting"
    dict["mold"] = {"item":mold}
    dict["fluid"] = {"ingredient":fluid, "amount":amount}
    dict["result"] = {"item":output}
    dict["break_chance"] = break_chance
    create_dir("../src/main/resources/data/tfc/recipes/casting")
    write_json(dict, file_path)

    
# welding recipe
def create_welding_recipe(file_path, input1, input2, output, tier):
    dict = {}
    dict["type"] = "tfc:welding"
    dict["first_input"] = {"tag":input1}
    dict["second_input"] = {"tag":input2}
    dict["tier"] = tier
    dict["result"] = {"item":output}
    create_dir("../src/main/resources/data/tfc/recipes/welding")
    write_json(dict, file_path)

