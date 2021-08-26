# directory-structure

![PyPI](https://img.shields.io/pypi/v/directory-structure?color=blue)
![PyPI - Downloads](https://img.shields.io/pypi/dm/directory-structure?color=blue)
![PyPI - License](https://img.shields.io/pypi/l/directory-structure?color=blue)
![GitHub watchers](https://img.shields.io/github/watchers/gabrielstork/directory-structure?color=blue)
![GitHub Repo stars](https://img.shields.io/github/stars/gabrielstork/directory-structure?color=blue)
![GitHub forks](https://img.shields.io/github/forks/gabrielstork/directory-structure?color=blue)

Print a directory tree structure in your Python code.

## Download

You can simply:

```sh
pip install directory-structure
```

Or you can also:

1. Clone the repository to your local machine.
2. Enter the directory.
3. Download necessary modules/libraries.

```sh
git clone https://github.com/gabrielstork/directory-structure.git
cd directory-structure
pip install -r requirements.txt
```

## Examples

```python
from directory_structure import Tree
```

* Using absolute path.

```python
path = Tree('C:/Users/User/Desktop/directory-structure', absolute=True)
print(path)
```

```text
📂 C:
|_📂 Users
  |_📂 User
    |_📂 Desktop
      |_📂 directory-structure
        |_📁 .git
        |_📁 directory_structure
        |_📁 dist
        |_📄 LICENSE
        |_📄 pyproject.toml
        |_📄 README.md
        |_📄 requirements.txt
        |_📄 setup.py
```

```python
path = Tree('C:/Users/User/Desktop/directory-structure', absolute=False)
print(path)
```

```text
📂 directory-structure
|_📁 .git
|_📁 directory_structure
|_📁 dist
|_📄 LICENSE
|_📄 pyproject.toml
|_📄 README.md
|_📄 requirements.txt
|_📄 setup.py
```

* Accessing a folder in current working directory.

```python
path = Tree('./directory_structure', absolute=True)
print(path)
```

```text
📂 C:
|_📂 Users
  |_📂 User
    |_📂 Desktop
      |_📂 directory-structure
        |_📂 directory_structure
          |_📄 tree.py
          |_📄 __init__.py
```

```python
path = Tree('./directory_structure', absolute=False)
print(path)
```

```text
📂 directory_structure
|_📄 tree.py
|_📄 __init__.py
```

* Getting all from the directory where your current working directory is.

```python
path = Tree('../', absolute=False)
print(path)
```

```text
📂 Desktop
|_📁 dados-futebol-brasileiro
|_📁 directory-structure
|_📁 fast-ml
|_📁 learning-django
|_📁 text-codifier
|_📁 to-do-list
|_📄 Discord.lnk
|_📄 Owlboy.url
|_📄 Spotify.lnk
|_📄 Steam.lnk
|_📄 Sublime Text 3.lnk
|_📄 Telegram.lnk
|_📄 The Binding of Isaac Rebirth.url
|_📄 Visual Studio Code.lnk
|_📄 WhatsApp.lnk
```

You can write any valid path, and it will work. These were only few examples.

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/gabrielstork)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/gabrielstork)
