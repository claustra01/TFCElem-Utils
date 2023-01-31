import tfce_types
import tfce_utils

def create_metal_item_heating_recipe(metal, types):
    for type in types:
        file_path = "../src/main/resources/data/tfc/recipes/heating/" + metal[0] + "_" + type[0] + ".json"
        input = "tfc:metal/" + type[0] + "/" + metal[0]
        output = "tfc:metal/" + metal[0]
        tfce_utils.create_heating_recipe(file_path, input, output, metal, type[1])


def metal_recipe():
    
    for metal in tfce_types.metals:
        
        # ingot
        file_path = "../src/main/resources/data/tfc/recipes/casting/" + metal[0] + "_ingot.json"
        mold = "tfc:ceramic/ingot_mold"
        fluid = "tfc:metal/" + metal[0]
        output = "tfc:metal/ingot/" + metal[0]
        tfce_utils.create_casting_recipe(file_path, mold, fluid, 100, output, 0.1) 
        
        if metal[2]:
            
            # double ingot
            file_path = "../src/main/resources/data/tfc/recipes/welding/" + metal[0] + "_double_ingot.json"
            input1 = "forge:ingots/" + metal[0]
            input2 = "forge:ingots/" + metal[0]
            output = "tfc:metal/double_ingot/" + metal[0]
            tfce_utils.create_welding_recipe(file_path, input1, input2, output, metal[6][0]) 

            # sheet
            file_path = "../src/main/resources/data/tfc/recipes/anvil/" + metal[0] + "_sheet.json"
            input = "forge:double_ingots/" + metal[0]
            output = "tfc:metal/sheet/" + metal[0]
            tfce_utils.create_anvil_recipe(file_path, input, output, 1, metal[6][0], ["hit_last", "hit_second_last", "hit_third_last"]) 
            
            # double sheet           
            file_path = "../src/main/resources/data/tfc/recipes/welding/" + metal[0] + "_double_sheet.json"
            input1 = "forge:sheets/" + metal[0]
            input2 = "forge:sheets/" + metal[0]
            output = "tfc:metal/double_sheet/" + metal[0]
            tfce_utils.create_welding_recipe(file_path, input1, input2, output, metal[6][0]) 

            # rod
            file_path = "../src/main/resources/data/tfc/recipes/anvil/" + metal[0] + "_rod.json"
            input = "forge:ingots/" + metal[0]
            output = "tfc:metal/rod/" + metal[0]
            tfce_utils.create_anvil_recipe(file_path, input, output, 2, metal[6][0], ["bend_last", "draw_second_last", "draw_third_last"])
            

def heating_ores():
    
    for ore in tfce_types.ores:
        
        file_path = "../src/main/resources/data/tfc/recipes/heating/normal_" + ore[0] + ".json"
        metal = tfce_utils.ore_to_metal(ore)
        input = "tfc:ore/normal_" + ore[0]
        output = "tfc:metal/" + metal[0]
        tfce_utils.create_heating_recipe(file_path, input, output, metal, 0.25)

        file_path = "../src/main/resources/data/tfc/recipes/heating/poor_" + ore[0] + ".json"
        metal = tfce_utils.ore_to_metal(ore)
        input = "tfc:ore/poor_" + ore[0]
        output = "tfc:metal/" + metal[0]
        tfce_utils.create_heating_recipe(file_path, input, output, metal, 0.15)

        file_path = "../src/main/resources/data/tfc/recipes/heating/rich_" + ore[0] + ".json"
        metal = tfce_utils.ore_to_metal(ore)
        input = "tfc:ore/rich_" + ore[0]
        output = "tfc:metal/" + metal[0]
        tfce_utils.create_heating_recipe(file_path, input, output, metal, 0.35)

        file_path = "../src/main/resources/data/tfc/recipes/heating/small_" + ore[0] + ".json"
        metal = tfce_utils.ore_to_metal(ore)
        input = "tfc:ore/small_" + ore[0]
        output = "tfc:metal/" + metal[0]
        tfce_utils.create_heating_recipe(file_path, input, output, metal, 0.1)


def heating_metals():
    
    for metal in tfce_types.metals:
        
        file_path = "../src/main/resources/data/tfc/recipes/heating/" + metal[0] + "_ingot.json"
        input = "tfc:metal/ingot/" + metal[0]
        output = "tfc:metal/" + metal[0]
        tfce_utils.create_heating_recipe(file_path, input, output, metal, 1)
        
        if metal[2]:
            create_metal_item_heating_recipe(metal, tfce_types.types_parts)