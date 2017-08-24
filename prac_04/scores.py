"""
CP1404/CP5632 Practical - Suggested Solution
This solution was submitted (via GitHub PR) by 2017-2 student CraigMorris1986!
Note the effective use of the pop(0) list method to both use and remove the
first score in each list (moving it to a new list for each subject).

Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject
codes and converts the rest of the lines from a list of strings into a list of
numbers, which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the
results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    # print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    scores_by_subject = reorganise_scores_by_subject(score_values)
    display_subject_details(scores_by_subject, subjects)


def reorganise_scores_by_subject(score_values):
    """Process list of by-student scores into list of by-subject scores."""
    subject_scores = []
    number_of_subjects = len(score_values[0])
    for _ in range(number_of_subjects):
        scores_for_one_subject = []
        for scores in score_values:
            # pop first score from by-student scores into the by-subject scores
            scores_for_one_subject.append(scores.pop(0))
        subject_scores.append(scores_for_one_subject)
    return subject_scores


def display_subject_details(scores_by_subject, subject_names):
    """Display subject scores with statistics."""
    for i, scores_for_one_subject in enumerate(scores_by_subject):
        print(subject_names[i], "Scores:")
        for score in scores_for_one_subject:
            print("{:>2}".format(score))
        print("Max: {:3}".format(max(scores_for_one_subject)))
        print("Min: {:3}".format(min(scores_for_one_subject)))
        print("Avg: {:6.2f}\n".format(
            (sum(scores_for_one_subject) / len(scores_for_one_subject))))


main()
