"""
CP1404/CP5632 Practical - Suggested Solution
Demos of various os module examples
"""
import os


def main():
    """Demo of os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # TODO: Use exception handling to avoid the crash (just pass)
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Process all subdirectories using os.walk()
    os.chdir('..')  # '..' means to go 'up' one directory
    lyrics_path = os.getcwd()  # store the path so we can get back to it
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)

        # TODO: change into the directory and print the current working directory
        # then change back to the lyrics_path
        # TODO: add a loop (in between directory changes) to rename the files
        os.chdir(directory_name)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))
            os.rename(filename, new_name)
        os.chdir(lyrics_path)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


main()
