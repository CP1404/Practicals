"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    scores_by_subject = organise_by_index(score_values, len(subjects))
    display_subject_details(scores_by_subject, subjects, len(subjects))


def organise_by_index(score_values, number_of_subjects):
    """This function takes in the list of scores values and number of subjects and pops the first index of each line
    of scores into a new list and returns that list. """
    subject_scores = []
    for i in range(number_of_subjects):
        temp_list = []
        for scores in score_values:
            temp_list.append(scores.pop(0))
        subject_scores.append(temp_list)
    return subject_scores


def display_subject_details(scores_by_subject, subject_names, number_of_subjects):
    """This function takes in the list of scores by subject code, the subject names list and the number of subjects
    to display formatted output to user. Print statements include the MAX, MIN, and Average calculations"""
    for i in range(number_of_subjects):
        print(subject_names[i], "Scores:")
        for score in scores_by_subject[i]:
            print("{:>2}".format(score))
        print("Max: ", max(scores_by_subject[i]))
        print("Min: ", min(scores_by_subject[i]))
        print("Avg: {:.2f}".format((int(sum(scores_by_subject[i]) / len(scores_by_subject[i])))), "\n")
main()
