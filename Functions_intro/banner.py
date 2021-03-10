def banner_text(text: str = " ", width: int = 80) -> None:
    """
    Centralize `text` into a specified `width`, with ** on either side.

    :param text: The string which is to be centralized.
        An asterisk will result in a row of asterisks.
        The default prints a blank line.
    :param width: The screen width to which the `text` will
        be centralized about (including the 4 spaces for the **
        either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    if len(text) > width - 4:
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, width))

    if text == "*":
        print("*" * width)
    else:
        output_string = "**{0}**".format(text.center(width - 4))
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you have forgotten!", 60)
banner_text("And that's to laugh, smile and dance and sing,", 60)
banner_text(width=60)
banner_text("When you are feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And always look on the bright side of life...", 60)
banner_text("*", 60)
