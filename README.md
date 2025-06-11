# Memo Application

This project is a simple memo tool that stores the text you provide and automatically categorizes it.

## Usage

Add a note:

```bash
python memo.py add "Your note text"
```

List all notes:

```bash
python memo.py list
```

List notes from a specific category:

```bash
python memo.py list --category work
```

Categories are determined by basic keyword matching. Currently supported categories are `shopping`, `work`, `personal`, and `other`.
