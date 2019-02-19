import test_data
import json


# Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    # Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    # Loop through the json_data
    for game in json_data:
        new_game = test_data.Game()
        #  title
        new_game.title = game["title"]
        #  year
        new_game.year = game["year"]
        #  platform (which requires reading name and launch_year)
        new_game.platform = test_data.Platform(game["platform"]["name"], game["platform"]["launch_year"])
        # Add that Game object to the game_library
        game_library.add_game(new_game)

    return game_library

# Part 2
input_json_file = "data/test_data.json"

# Open the file specified by input_json_file
with open(input_json_file, "r") as reader:
    # Use the json module to load the data from the file
    game_library_json = json.load(reader)

    # Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
    game_library_data = make_game_library_from_json(game_library_json)

# Print out the resulting GameLibrary data using print()
print("JSON data:")
print(game_library_json)
print("GameLibrary data:")
print(game_library_data)
