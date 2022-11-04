# Import pandas as pd
import pandas as pd


def replace_names(csv_path, names_to_replace, new_values):
    # Create data frame from the csv file
    df = pd.read_csv(csv_path)

    # Loop through names to replace and 
    for i in range(len(names_to_replace)):
        df = df.replace(to_replace=names_to_replace[i], value=f"{new_values[0]}{i}")

    # Export to csv
    df.to_csv(csv_path, index=False)


if __name__ == '__main__':
    faculty_data = "../input/FacultyAvailability.csv"
    student_data = "../input/StudentAvailabilityAndRanks.csv"

    faculty_names_to_replace = ["name1","name2","name3","name4","name5"]
    student_names_replace = ["name1","name2","name3","name4","name5"]
    
    replace_names(faculty_data, faculty_names_to_replace, ['Faculty'])
    replace_names(student_data, student_names_replace, ['Student'])
    replace_names(student_data, faculty_names_to_replace, ['Faculty'])
