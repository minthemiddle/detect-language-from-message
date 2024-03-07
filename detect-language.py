import pandas as pd
import re
import click
from lingua import LanguageDetectorBuilder

def detect_language(text):
    detector = LanguageDetectorBuilder.from_all_languages().build()
    language = detector.detect_language_of(text)
    return language.iso_code_639_1.name if language else 'N/A'

@click.command()
@click.argument('filename')
def process_file(filename):
    df = pd.read_csv(filename)
    df['language'] = ''

    for idx, row in df.iterrows():
        message = row['message']
        language = detect_language(message)
        df.loc[idx, 'language'] = language
        df['language'] = df['language'].astype(str)

    df.to_csv(filename, index=False)

if __name__ == '__main__':
    process_file()
