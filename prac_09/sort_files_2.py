"""
CP1404/CP5632 Practical - Suggested Solution
Sort files based on extension and user categorisation
"""
import os


def main():
    """Move files into where user wants to store them based on extension."""
    # The following dictionary will allow us to map extensions to the destination folder names
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(extension))
            # Now we can map this new extension to a folder name
            extension_to_category[extension] = category
            try:
                # We don't expect to get an exception due to the if statement
                # But we'll play it safe anyway in case the user chooses an existing folder
                os.mkdir(category)
            except FileExistsError:
                pass

        # We don't need a separate loop for this next step
        # We're already in a loop per file and we now know where to put it
        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()
