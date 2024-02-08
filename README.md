# Detect language from message

Reads a `*.csv` from argument.  
Takes string from `message` column.  
Detects most probable language.  
Saves ISO Code 639_1 name to `language` column.

**Usage** 
- `pip install pandas click lingua-language-detector`
- `python3 detect-language.py FILE.CSV`  


**Libraries Used**  
Uses [Pandas](https://pandas.pydata.org/) for CSV handling.  
Uses [Lingua](https://github.com/pemistahl/lingua-py) for very quick language detection.  
Uses [Click](https://click.palletsprojects.com/en/8.1.x/) for the CLI.
