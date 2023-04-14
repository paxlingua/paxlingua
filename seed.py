"""The purpose of this function is to pull the seed.txt file and return it so it can be used through the GPT4 or future APIs"""

def get_seed_text():
    with open("seed.txt", "r") as seed_file:
        seed_text = seed_file.read()
    return seed_text
