import json
import argparse
import os

NOTES_FILE = 'notes.json'

CATEGORIES = {
    'shopping': ['buy', '购物', 'purchase', '买'],
    'work': ['work', 'project', 'meeting', '项目', '会议'],
    'personal': ['personal', 'family', '家', '生日'],
}

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_notes(notes):
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

def categorize(text):
    lowered = text.lower()
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw.lower() in lowered:
                return category
    return 'other'

def add_note(text):
    notes = load_notes()
    category = categorize(text)
    note = {'text': text, 'category': category}
    notes.append(note)
    save_notes(notes)
    print(f"Added note to category '{category}'")

def list_notes(category=None):
    notes = load_notes()
    for note in notes:
        if category is None or note['category'] == category:
            print(f"[{note['category']}] {note['text']}")

def main():
    parser = argparse.ArgumentParser(description='Simple memo application with auto categorization')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new note')
    add_parser.add_argument('text', help='Text of the note')

    list_parser = subparsers.add_parser('list', help='List notes')
    list_parser.add_argument('--category', help='Filter by category')

    args = parser.parse_args()

    if args.command == 'add':
        add_note(args.text)
    elif args.command == 'list':
        list_notes(args.category)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
