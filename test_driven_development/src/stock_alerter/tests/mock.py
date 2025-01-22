class Mock:
    def __init__(self):
        self.called = False
        self.params = ()

    def __call__(self, *args, **kwargs):
        self.called = True
        self.params = args, kwargs
