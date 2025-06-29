# 🔤 NATO Phonetic Alphabet Converter

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/06/NATO-Alphabet-Project02.jpg" alt="Artwork Grid Example" />
</p>

A Python script that converts user input into its NATO phonetic alphabet equivalent using a CSV dataset.

## 🎯 Project Goal

- Practice working with **Pandas** DataFrames
- Learn dictionary comprehensions and row iteration
- Create a real-world data mapping application

## 🧠 Python Concepts Practiced

- `pandas.read_csv()` for reading CSV files
- `.iterrows()` to loop through DataFrame rows
- Dictionary comprehensions
- String manipulation with `.upper()`
- Exception handling for unknown characters (recommended for improvements)

## 📋 How It Works

1. Reads `nato_phonetic_alphabet.csv` into a dictionary format:  
   `{"A": "Alpha", "B": "Bravo", ...}`  
2. Prompts the user to enter a word.
3. Converts each letter into its phonetic code and prints a list like:  
   `["Mike", "India", "November", "Alpha"]`

## 🛠 How to Run

Ensure you have `pandas` installed and the file `nato_phonetic_alphabet.csv` in the same directory.

```bash
pip install pandas
python main.py
```

Input any word, and the program will return the NATO phonetic spelling.

---

Great practice for data lookups and user interaction using real-world datasets. 🧠📘
