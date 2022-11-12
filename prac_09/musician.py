"""Musician class for CP1404"""


class Musician:
    """Musician class"""

    def __init__(self, name=""):
        self.name = name
        self.instruments = []

    def __str__(self):
        return f"{self.name} ({self.instruments})"

    def __repr__(self):
        return str(vars(self))

    def play(self):
        if not self.instruments:
            return f"{self.name} needs an instrument!"
        return f"{self.name} is playing: {self.instruments[0]}"


if __name__ == '__main__':
    from guitar import Guitar

    musician = Musician()
    assert not musician.name
    assert not musician.instruments

    musician.name = "Lincoln Brewster"
    musician.instruments.append(Guitar("Fender Lincoln Brewster Stratocaster", 2020, 3419.0))
    musician.instruments.append(Guitar("Ernie Ball Music Man Silhouette Special", 1993, 2499.0))
    print(musician)
    print(musician.play())
