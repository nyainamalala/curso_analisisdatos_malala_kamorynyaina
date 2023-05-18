class Traveldatabase:
    def __init__(self):
        self.travels = []

    def find_all(self): # SELECT * FROM travels
        return self.travels.copy()
        # return list(self.travels)
