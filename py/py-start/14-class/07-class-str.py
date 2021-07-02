class Washer():
    def __init__(self) -> None:
        self.width = 200

    def __str__(self) -> str:
        return 'Washer class __str__ method'


w1 = Washer()

print(w1)