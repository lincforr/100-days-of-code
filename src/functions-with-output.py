# Functions with Outputs


def format_name(f_name, l_name):
    """
    Takes a f_name and a l_name and changes it to title case
    """
    if f_name or l_name == "":
        return "Invalid arguments"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name("RUNlEveL", "f")

print(formated_string)
