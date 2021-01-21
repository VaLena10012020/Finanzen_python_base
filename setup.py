import setuptools
from os.path import join, dirname, abspath


# Parse requirements.txt for dependencies
def read_requirements(basename):
    reqs_file = join(dirname(abspath(__file__)), basename)
    with open(reqs_file) as f:
        return [req.strip() for req in f.readlines()]


required_packages = read_requirements('requirements.txt')

# Parse Readme for long_description
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="finanzen_base",
    version="0.0.1",
    author="Valentin Kuhn",
    author_email="valentin.gabriel.kuhn@outlook.de",
    description="Base function and classes for setup a Server to gather and show all financial information",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=required_packages
)