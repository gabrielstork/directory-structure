import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='directory-structure',
    version='1.1.0',
    author='Gabriel Stork',
    author_email='storkdeveloper@gmail.com',
    description='Print a directory tree structure in your Python code.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gabrielstork/directory-structure',
    project_urls={
        'Bug Tracker': 'https://github.com/gabrielstork/directory-structure/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3',
    install_requires=['emoji'],
)

