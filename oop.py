from pprint import pp


def class_and_dict():
    strdemo = "hello world"
    i = 2.0
    l = []
    d = {"a": 1, "b": 2, "c": 3}
    t = ("a", "b", "c")
    n = None
    pp(
        {
            "s": strdemo.__class__,
            "i": i.__class__,
            "l": l.__class__,
            "d": d.__class__,
            "t": t.__class__,
            "n": n.__class__,
            "cls": n.__class__.__class__ # metaclass
        }
    )


if __name__ == "__main__":
    class_and_dict()
