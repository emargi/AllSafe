from setuptools import setup, find_packages


__version__ = "1.2.5"

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="AllSafe",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "allsafe=allsafe.main:run"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Security",
    ],
    description="AllSafe, A Modern Password Generator",
    author="Mohamad Reza",
    url="https://github.com/emargi/AllSafe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Source Code": "https://github.com/emargi/Allsafe#readme",
        "Bug Tracker": "https://github.com/emargi/AllSafe/issues",
    },
    keywords="password password-generator tool allsafe generator",
)
