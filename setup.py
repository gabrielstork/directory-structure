import setuptools

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setuptools.setup(
    name='directory-structure',
    version='1.1.2',
    description='Print a directory tree structure in your Python code.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gabrielstork/directory-structure',
    author='Gabriel Stork',
    author_email='storkdeveloper@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='directory structure tree emoji folder file',
    packages=setuptools.find_packages(),
    install_requires=['emoji'],
    python_requires='>=3',
)
