import os
import shutil
import argparse

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav"],
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(path, prefix=None):
    counters = {}

    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if not os.path.isfile(full_path):
            continue

        category = get_category(file)
        category_path = os.path.join(path, category)
        os.makedirs(category_path, exist_ok=True)

        new_name = file
        if prefix:
            ext = os.path.splitext(file)[1]
            counters[category] = counters.get(category, 0) + 1
            new_name = f"{prefix}_{counters[category]}{ext}"

        shutil.move(full_path, os.path.join(category_path, new_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk File Organizer")
    parser.add_argument("--path", required=True, help="Folder path to organize")
    parser.add_argument("--prefix", help="Optional prefix for renaming")

    args = parser.parse_args()
    organize_files(args.path, args.prefix)

    print("✅ Files organized successfully.")

