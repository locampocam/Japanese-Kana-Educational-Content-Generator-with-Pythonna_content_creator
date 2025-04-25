import pandas as pd


# Full list of basic Katakana characters and their Romaji (pronunciations)
katakana_list = [
    ("ア", "A"), ("イ", "I"), ("ウ", "U"), ("エ", "E"), ("オ", "O"),
    ("カ", "KA"), ("キ", "KI"), ("ク", "KU"), ("ケ", "KE"), ("コ", "KO"),
    ("サ", "SA"), ("シ", "SHI"), ("ス", "SU"), ("セ", "SE"), ("ソ", "SO"),
    ("タ", "TA"), ("チ", "CHI"), ("ツ", "TSU"), ("テ", "TE"), ("ト", "TO"),
    ("ナ", "NA"), ("ニ", "NI"), ("ヌ", "NU"), ("ネ", "NE"), ("ノ", "NO"),
    ("ハ", "HA"), ("ヒ", "HI"), ("フ", "FU"), ("ヘ", "HE"), ("ホ", "HO"),
    ("マ", "MA"), ("ミ", "MI"), ("ム", "MU"), ("メ", "ME"), ("モ", "MO"),
    ("ヤ", "YA"), ("ユ", "YU"), ("ヨ", "YO"),
    ("ラ", "RA"), ("リ", "RI"), ("ル", "RU"), ("レ", "RE"), ("ロ", "RO"),
    ("ワ", "WA"), ("ヲ", "WO"), ("ン", "N")
]

# Build the dataframe
df_katakana = pd.DataFrame([
    {
        "Kana": kana,
        "Type": "Katakana",
        "Pronunciation": romaji,
        "Prompt": create_prompt(kana, romaji),
        "Educational Text": create_educational_text(kana, romaji)
    }
    for kana, romaji in katakana_list
])

# Save to CSV
file_path_katakana = "/mnt/data/katakana_content.csv"
df_katakana.to_csv(file_path_katakana, index=False)
file_path_katakana
