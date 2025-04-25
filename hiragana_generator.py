import pandas as pd

# Full list of basic Hiragana characters and their Romaji (pronunciations)
kana_list = [
    ("あ", "A"), ("い", "I"), ("う", "U"), ("え", "E"), ("お", "O"),
    ("か", "KA"), ("き", "KI"), ("く", "KU"), ("け", "KE"), ("こ", "KO"),
    ("さ", "SA"), ("し", "SHI"), ("す", "SU"), ("せ", "SE"), ("そ", "SO"),
    ("た", "TA"), ("ち", "CHI"), ("つ", "TSU"), ("て", "TE"), ("と", "TO"),
    ("な", "NA"), ("に", "NI"), ("ぬ", "NU"), ("ね", "NE"), ("の", "NO"),
    ("は", "HA"), ("ひ", "HI"), ("ふ", "FU"), ("へ", "HE"), ("ほ", "HO"),
    ("ま", "MA"), ("み", "MI"), ("む", "MU"), ("め", "ME"), ("も", "MO"),
    ("や", "YA"), ("ゆ", "YU"), ("よ", "YO"),
    ("ら", "RA"), ("り", "RI"), ("る", "RU"), ("れ", "RE"), ("ろ", "RO"),
    ("わ", "WA"), ("を", "WO"), ("ん", "N")
]

# Generate educational text and prompts automatically
def create_prompt(kana, romaji):
    return f"kawaii anime girl teaching {kana} with cute background"

def create_educational_text(kana, romaji):
    sounds_like = {
        "A": "a in 'car'", "I": "ee in 'see'", "U": "oo in 'moon'", "E": "e in 'bed'", "O": "o in 'open'",
        "KA": "ka in 'car'", "KI": "kee", "KU": "koo", "KE": "keh", "KO": "ko in 'coffee'",
        "SA": "sa in 'sand'", "SHI": "she", "SU": "soo", "SE": "se in 'set'", "SO": "so in 'song'",
        "TA": "ta in 'tap'", "CHI": "chee", "TSU": "tsu in 'tsunami'", "TE": "te in 'ten'", "TO": "to in 'top'",
        "NA": "na in 'nap'", "NI": "nee", "NU": "noo", "NE": "neh", "NO": "no in 'note'",
        "HA": "ha in 'hat'", "HI": "hee", "FU": "fu in 'fun'", "HE": "he in 'help'", "HO": "ho in 'hot'",
        "MA": "ma in 'map'", "MI": "me in 'meat'", "MU": "moo", "ME": "meh", "MO": "mo in 'more'",
        "YA": "ya in 'yarn'", "YU": "you", "YO": "yo in 'yoga'",
        "RA": "ra in 'rabbit'", "RI": "ree", "RU": "roo", "RE": "reh", "RO": "ro in 'robot'",
        "WA": "wa in 'water'", "WO": "wo in 'wonder'", "N": "n in 'sun'"
    }
    return f"{kana} is pronounced like '{sounds_like.get(romaji, romaji)}'. Imagine something cute to help you remember!"

# Build the dataframe
df = pd.DataFrame([
    {
        "Kana": kana,
        "Type": "Hiragana",
        "Pronunciation": romaji,
        "Prompt": create_prompt(kana, romaji),
        "Educational Text": create_educational_text(kana, romaji)
    }
    for kana, romaji in kana_list
])

# Save to CSV
file_path = "/mnt/data/hiragana_content.csv"
df.to_csv(file_path, index=False)
file_path
