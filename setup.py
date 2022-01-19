from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ghsearcher",
    version='0.0.3',
    author="David Tippett",
    description="A tool for searching GitHub",
    license='Apache Software License',
    license_files=['LICENSE'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="GitHub Replacement Automated Commit",
    url="https://github.com/dtaivpp/ghsearcher",
    packages=['ghsearcher'],
    install_requires=['ghapi','python-dotenv', 'wheel'],
    entry_points = {
        'console_scripts': ['ghsearcher=ghsearcher.searcher:cli_entry'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        'Intended Audience :: Developers',
        "Operating System :: OS Independent"
    ],
)
