from setuptools import setup, find_packages


__version__ = "1.1.3"

setup(
    name="AllSafe",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "allsafe=allsafe.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="AllSafe, A Modern Password Generator",
    author="Mohamad Reza",
    url="https://github.com/emargi/AllSafe",
)
