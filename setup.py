import setuptools
from os.path import join, dirname, abspath


# Parse requirements.txt for dependencies
def read_requirement_file(req_file: str):
    req_files = join(dirname(abspath(__file__)), req_file)
    with open(req_files) as f:
        return [req.strip() for req in f.readlines()]


class ReqReader():
    def __init__(self, basename: str):
        self.basename = basename

    def read_requirements(self):
        requirement_txt = read_requirement_file(self.basename)
        install_token = "-r "
        base_parent_path = self.basename.split("/")[0]
        # Check for external file dependencies and parse all of them
        while any(install_token in req for req in requirement_txt):
            for req in requirement_txt:
                if install_token in req:
                    # Get parent path if necessary
                    file_path = req.split(install_token)[1]
                    if "/" in file_path:
                        parent_path = base_parent_path+file_path.split("/")[0]
                    else:
                        parent_path = base_parent_path
                    # Get packages of external path
                    new_requirement = read_requirement_file(parent_path+"/"+req.split(install_token)[1])

                    # Check for external file dependencies and if necessary add parent path
                    for new_req in new_requirement:
                        if install_token in new_req:
                            new_requirement.extend([new_req.split(" ")[0]+" "+parent_path+"/"+new_req.split(" ")[1]])
                            new_requirement.remove(new_req)

                    # Add parsed dependencies
                    requirement_txt.extend(new_requirement)
                    requirement_txt.remove(req)

        return requirement_txt


required_packages = ReqReader('requirements.txt').read_requirements()

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