import os
import emoji


def directory_tree(path):
    content = [c for c in os.listdir(path)]

    for c in content:
        if os.path.isdir(os.path.join(path, c)):
            print(emoji.emojize(f':file_folder: {c}'))
        else:
            print(emoji.emojize(f':page_facing_up: {c}'))
