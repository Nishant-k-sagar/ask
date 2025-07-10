from setuptools import setup

setup(
    name='ask',
    version='0.1',
    py_modules=['ask'],
    entry_points={
        'console_scripts': [
            'ask=ask:main',
        ],
    },
    install_requires=['groq', 'pyperclip'],
)
