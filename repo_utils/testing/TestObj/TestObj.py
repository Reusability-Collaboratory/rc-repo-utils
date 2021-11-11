class TestObj:
    static_item = "static_item"

    def __init__(self):
        print("init")
        self.test = "Hi"

    def __call__(self):
        print("call: {}".format(self.test))

    def static_func():
        return "static"

    def func(self):
        return "func"

    def __getitem__(self, item):
        return "item"
