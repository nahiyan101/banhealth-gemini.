import pandas as pd
import re

# Data structure to hold rows
rows = []

def add_row(genre_bn, genre_en, prompt_bn, prompt_en, resp_bn, resp_en, label):
    # Sanity checks for comma spacing
    # In Bengali and English, ensure space before comma " , "
    # Replace any plain comma with " , " correctly if not already spaced

    # Simple cleaner/formatter function
    def format_commas(text):
        # Replace multi-spaces
        text = re.sub(r'\s*,\s*', ' , ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    r_bn = format_commas(resp_bn)
    r_en = format_commas(resp_en)

    rows.append({
        'Symptoms Genres': genre_bn,
        'Symptoms Genres (Translated to English)': genre_en,
        'Used Prompts': prompt_bn,
        'Used Prompts (Translated to English)': prompt_en,
        'Response': r_bn,
        'Response (Translated to English)': r_en,
        'Lable': label
    })
