import tfce_types
import tfce_utils
import tfce_images

def gen_texture():
    for metal in tfce_types.metals:
        
        # pile
        temp_path = "../src/main/resources/assets/tfc/textures/block/metal/full/base.png"
        file_path = "../src/main/resources/assets/tfc/textures/block/metal/full/" + metal[0] + ".png"
        tfce_images.change_hsv(temp_path, file_path, metal[5][1], metal[5][2], metal[5][3])

