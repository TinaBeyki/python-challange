"""
DocStrings are basically a way for us to create little bits of Documentaion as we are coding along in out functions
or in our other blocks of code
"""


def format_name(first_name, last_name):
    """Takes first name and last name and format it to return the title case version of the name"""
    if first_name == "" or last_name == "":
        return "You dident provide valid inputs."
    first_name = first_name.title()
    last_name = last_name.title()
    return f"Result {first_name} {last_name}"

