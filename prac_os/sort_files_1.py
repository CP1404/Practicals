"""
CP1404/CP5632 Practical - Suggested Solution
Sort files based on extension
"""
import os


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        # We could maintain a list/set of extensions we've made folders for (LBYL)
        # Or we could just "try" making folders again and ignore errors (EAFP)
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print("{}/{}".format(extension, filename))
        os.rename(filename, "{}/{}".format(extension, filename))


main()
