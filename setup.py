from setuptools import setup, find_packages

setup(
    name='notes-cli',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'notes-cli= notes-cli.cli:app',  # Replace with your entry point function
        ],
    },
    install_requires=[
        'fastapi==0.115.12',
        'httpx==0.28.1',
        'pydantic==2.11.4',
        'rich==14.0.0',
        'typer==0.15.4'
    ],
    author='Ankita',
    author_email='ankita.av.934@gmail.com',
    description='A simple CLI tool for managing notes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ankita311/notes-cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
