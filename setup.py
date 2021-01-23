import setuptools
from os.path import join, dirname, abspath


def read_requirements(basename):
    def read_requirement_file(req_file: str):
        req_files = join(dirname(abspath(__file__)), req_file)
        with open(req_files) as f:
            return [req.strip() for req in f.readlines()]

    requirement_txt = read_requirement_file(basename)
    install_token = "-r "
    base_path = basename.split("/")[0]+"/"
    for req in requirement_txt:
        if install_token in req:
            # Get packages of external path
            new_requirement = read_requirement_file(base_path+req.split(install_token)[1])
            # Add parsed dependencies
            requirement_txt.extend(new_requirement)
            requirement_txt.remove(req)
    return requirement_txt


required_packages = read_requirements('requirements/prod.txt')

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
