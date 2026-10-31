def create_bubble(text):
    width = len(text)

    return (
        " " + "_" * (width + 2) + "\n"
        f"< {text} >\n"
        " " + "-" * (width + 2)
    )
