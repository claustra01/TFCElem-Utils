import tfce_types
import tfce_utils

def anvil_recipe():
    
    for metal in tfce_types.metals:
        
        if metal[2]:
            
            # sheet
            file_path = "../src/main/resources/data/tfc/recipes/anvil/" + metal[0] + "_sheet.json"
            input = "forge:double_ingots/" + metal[0]
            output = "forge:sheet/" + metal[0]
            tfce_utils.create_anvil_recipe(file_path, input, output, 1, metal[6][0], ["hit_last", "hit_second_last", "hit_third_last"])            

            # rod
            file_path = "../src/main/resources/data/tfc/recipes/anvil/" + metal[0] + "_rod.json"
            input = "forge:ingots/" + metal[0]
            output = "forge:rod/" + metal[0]
            tfce_utils.create_anvil_recipe(file_path, input, output, 2, metal[6][0], ["bend_last", "draw_second_last", "draw_third_last"])
