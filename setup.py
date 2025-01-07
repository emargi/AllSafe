from setuptools import setup, find_packages


__version__ = "1.0.0"

setup(
    name="AllSafe",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "allsafe=main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="AllSafe, A Modern Password Generator",
    author="Emargi",
    url="https://github.com/emargi/AllSafe",
)
