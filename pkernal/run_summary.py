import glob
import importlib

translation_files = glob.glob("p*.py")  # Adjust the pattern to match the files containing the dictionaries

translations = []

for file in translation_files:
    print(file)
    module_name = file[:-3]  # Remove the '.py' extension from the filename
    module = importlib.import_module(module_name)

    paxlingua_phrases = getattr(module, "paxlingua_phrases")

    for key, value in paxlingua_phrases.items():
        paxlingua_phrase = value["Paxlingua"]
        english_phrase = value["English"]
        translations.append((paxlingua_phrase, english_phrase))

for translation in translations:
    print(translation)
