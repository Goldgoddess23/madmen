from setuptools import setup, find_packages

setup(
    name="solgard_bot",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "bot_run = app.main:main",
        ]
    },
    author="Alex Traveylan",
    author_email="alex.traveylan@gmail.com",
    description="A bot for legend of solgard",
    url="https://github.com/AlexTraveylan/solgard-bot-last-refactoring",
    classifiers=[
        "Programming Language :: Python :: >3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
