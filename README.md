# directory-tree

Print a directory tree structure in your Python code.

## Examples

When `complete=True`:

```python
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
        |_📄 directory_tree.py
        |_📄 LICENSE
        |_📄 README.md
```

When `complete=False`:

```python
path = Tree('C:/Users/User/Desktop/directory-tree', complete=False)
print(path)
```

```text
📂 directory-tree
|_📁 .git
|_📄 directory_tree.py
|_📄 LICENSE
|_📄 README.md
```
