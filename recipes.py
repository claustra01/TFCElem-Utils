import tfce_types
import tfce_utils

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
