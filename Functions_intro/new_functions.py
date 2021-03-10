def central_text(text):
    print("{}".format(text.center(80)))


# or


def text_central(*args, sep=" ", end="\n", file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


text_central("Chicken wings")
text_central("gimme some bones in this mf")
