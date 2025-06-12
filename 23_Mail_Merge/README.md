# 💌 Mail Merge Letter Generator

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/06/the-mail-merge.jpg" alt="Artwork Grid Example" />
</p>

This Python script automates the process of generating personalized letters by replacing placeholders in a template letter with actual names from a provided list. A perfect beginner-friendly project for mastering file handling and string manipulation.

## 🎯 Project Goal

- Practice reading from and writing to files in Python.
- Learn how to manipulate strings using placeholders.
- Automate letter creation using basic programming logic.

## 🧠 Python Concepts Practiced

- **File Handling**: Reading `.txt` files using `with open(...) as file`
- **Reading lines**: `.readlines()` to load multiple names
- **String replacement**: `.replace()` to swap `[name]` with each actual name
- **Stripping whitespace**: `.strip()` to clean names
- **Looping through data**: `for` loop to iterate over name list
- **Dynamic file creation**: Writing personalized output to new `.txt` files

## 📋 How It Works

1. Reads the name list from `./Input/Names/invited_names.txt`
2. Loads the letter template from `./Input/Letters/starting_letter.txt`
3. Replaces the `[name]` placeholder with each individual name
4. Saves the personalized letters in `./Output/ReadyToSend/` as `letter_for_<name>.txt`

## 🛠 How to Run

Make sure your project directory has the following structure:

```
.
├── main.py
├── Input
│   ├── Names
│   │   └── invited_names.txt
│   └── Letters
│       └── starting_letter.txt
└── Output
    └── ReadyToSend
```

Then run:

```bash
python main.py
```

Check the `Output/ReadyToSend` folder for your personalized letters.

---

Speed up your outreach with automated letters! ✉️✨
