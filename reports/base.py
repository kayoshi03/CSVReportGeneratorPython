class Base:
    name = None
    title = []

    def generate(self, rows):
        raise NotImplementedError("Report must implement generate()")