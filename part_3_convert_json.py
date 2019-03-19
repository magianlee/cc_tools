import json
import cc_data
import cc_dat_utils
from cc_dat_utils import make_cc_data_from_dat


def make_datafile_from_json(json_data):
    # Initialize a new level set
    datafile = cc_data.CCDataFile()

    # Loop through the json_data
    for level in json_data["levels"]:

        # initiate a temp level
        new_level = cc_data.CCLevel()

        # general info
        new_level.level_number = level["level_number"]
        new_level.time = level["time"]
        new_level.num_chips = level["num_chips"]
        new_level.upper_layer = level["upper_layer"]
        new_level.lower_layer = level["lower_layer"]

        # go through optional fields
        fields = level["optional_fields"]
        for field in fields:
            type_val = field["type_val"]
            if type_val == 3:
                title = cc_data.CCMapTitleField(field["title"])
                new_level.add_field(title)
            elif type_val == 6:
                password = cc_data.CCEncodedPasswordField(field["password"])
                new_level.add_field(password)
            elif type_val == 7:
                hint = cc_data.CCMapHintField(field["hint"])
                new_level.add_field(hint)
            elif type_val == 10:
                monster_coordinates = []
                for coordinate in field["monsters"]:
                    monster_coordinates.append(cc_data.CCCoordinate(coordinate[0], coordinate[1]))
                monsters = cc_data.CCMonsterMovementField(monster_coordinates)
                new_level.add_field(monsters)
            elif type_val == 4:
                a = 0
                # cc_password = cc_data.CCEncodedPasswordField(field["password"])
                #level.add_field(cc_password)
            elif type_val == 5:
                b = 0
                #c c_password = cc_data.CCEncodedPasswordField(field["password"])
                #level.add_field(cc_password)

        # Add temp level to the level set
        datafile.add_level(new_level)

    return datafile


# define load and save file path
load_file_path = "data/yunhaol_cc_level_data.json"
save_file_path = "data/yunhaol_cc_level_data.dat"
with open(load_file_path, "r") as reader:
    data = json.load(reader)

# Convert JSON data to cc_data
level_set = make_datafile_from_json(data)

# Save converted data to DAT file
cc_dat_utils.write_cc_data_to_dat(level_set, save_file_path)

# test
# read_data = make_cc_data_from_dat(save_file_path)
# print(read_data)
