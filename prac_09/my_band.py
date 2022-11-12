"""Band example with list of musicians."""
from band import Band
from musician import Musician
from guitar import Guitar


def main():
    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.instruments.append(Guitar("Washburn N4", 1990, 2499.95))
    nuno.instruments.append(Guitar("Takamine acoustic", 1986, 1200.0))
    band.musicians.append(nuno)
    band.musicians.append(Musician("Gary Cherone"))
    pat = Musician("Pat Badger")
    pat.instruments.append(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
    band.musicians.append(pat)
    kevin = Musician("Kevin Figueiredo")
    band.musicians.append(kevin)

    print("band.play()")
    print(band.play())
    print("band (str)")
    print(band)


main()
