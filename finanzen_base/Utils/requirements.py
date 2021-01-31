def read_requirements(basename):
    def read_requirement_file(req_file: str):
        with open(req_file) as f:
            return [req.strip() for req in f.readlines()]

    requirement_txt = read_requirement_file(basename)
    install_token = "-r "
    base_path = basename.split("/")[0]+"/"
    for req in requirement_txt:
        if install_token in req:
            # Get packages of external path
            new_requirement = read_requirement_file(
                base_path+req.split(install_token)[1]
            )
            # Add parsed dependencies
            requirement_txt.extend(new_requirement)
            requirement_txt.remove(req)
    return requirement_txt
