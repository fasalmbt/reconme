import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="reconme", 

    version="1.0.0",

    author="f98m",

    author_email="",

    description="",

    long_description="refer README.md",

    long_description_content_type="text/markdown",

    url="https://github.com/f98m/reconme",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: GPL License",

        "Operating System :: OS Independent",

    ],

    python_requires='>=3.6',

)
