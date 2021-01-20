import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Finance Home Server",
    version="0.0.1",
    author="Valentin Kuhn",
    author_email="valentin.gabriel.kuhn@outlook.de",
    description="Setup a Server to gather and show all financial information",
    long_description=long_description,
    long_description_content_type="text/markdown",
#   url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
#    classifiers=[
#        "Programming Language :: Python :: 3",
#        "License :: OSI Approved :: MIT License",
#        "Operating System :: OS Independent",
#    ],
    python_requires='>=3.6',
)