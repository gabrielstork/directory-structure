# directory-tree

Print a directory tree structure in your Python code.

Steps to use:

1. Clone the repository to your local machine.
2. Enter the directory.
3. Download necessary modules/libraries.

```sh
git clone https://github.com/gabrielstork/directory-tree.git
cd directory-tree
pip install -r requirements.txt
```

## Examples

When `complete=True`:

```python
from tree import Tree

path = Tree('C:/Users/User/Desktop/directory-tree', complete=True)
print(path)
```

```text
📂 C:
|_📂 Users
  |_📂 User
    |_📂 Desktop
      |_📂 directory-tree
        |_📁 .git
        |_📄 LICENSE
        |_📄 README.md
        |_📄 requirements.txt
        |_📄 tree.py
```

When `complete=False`:

```python
from Tree import Tree

path = Tree('C:/Users/User/Desktop/directory-tree', complete=False)
print(path)
```

```text
📂 directory-tree
|_📁 .git
|_📄 LICENSE
|_📄 README.md
|_📄 requirements.txt
|_📄 tree.py
```
