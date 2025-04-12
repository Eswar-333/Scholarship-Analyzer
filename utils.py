def load_prompt_template(path="prompt_template.txt"):
    with open(path, "r") as file:
        return file.read()