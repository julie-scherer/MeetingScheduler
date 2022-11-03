# pip install python-csv
# https://pypi.org/project/python-csv/

import os.path as osp
import csv


class Student():
    def __init__(self, name, ranks, availability):
        self.name = name
        self.ranks = ranks
        while '' in self.ranks:
            self.ranks.remove('') # remove emtpy string
        self.it = 0
        self.timeslots = set()
        self.fac_scheduled = set()
        self.availability = availability

    def __repr__(self):
        return f'"{self.name}"'

class Faculty():
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability
        self.timeslots = set()

    def __repr__(self):
        return f'"{self.name}"'

class Timeslot():
    def __init__(self, time):
        self.time = time
        self.fac_scheduled = set() # fac_scheduled contains faculty scheduled AND faculty unavailable (!)
        self.stu_scheduled = set()
        self.meetings = [] # list of tupels (faculty, student)

    def __repr__(self):
        return f'{self.time}'


# * CREATE ALL_TIMESLOT_RECORDS MASTER DICTIONARY
def import_timeslot_names(rawdata):
    timeslots = [] # list of Timeslot objects
    with open(rawdata, 'r', newline = '') as f:
        reader = csv.reader(f)
        for line in reader:
            time = line[0]
            timeslot = Timeslot(time)
            timeslots.append(timeslot)

    return timeslots


# * CREATE ALL_STUDENT_RANK_RECORDS MASTER DICTIONARY
def import_student_facultyranks(rawdata, timeslots, verbose = False):
    students = [] # list of Student objects
    with open(rawdata, newline='') as f:
        header = f.readline().split(',')
        header = [i.strip() for i in header]
        reader = csv.reader(f)

        for line in reader:
            studentname = line[0]
            facultyranks = line[1:11]
            availability = line[11:]
            student = Student(studentname, facultyranks, availability)
            students.append(student)
            for i, avail_i in enumerate(availability):
                if avail_i != 'Y':
                    try:
                        time_unavailable = header[i+11]
                        timeslot = timeslots[i] # indexing should be off by 1
                        if verbose:
                            print("{} is unavailable at {}".format(studentname, time_unavailable))
                    except Exception as e:
                        return time_unavailable == timeslot.time, f"time_unavailable {time_unavailable} does not match timeslot.time {timeslot.time}, probably an indexing issue i = {i}"
                    timeslot.stu_scheduled.add(student)  

    return students


# * IMPORT TIMES FACULTY ARE UNAVAILABLE
def import_faculty_availability(rawdata, timeslots, verbose = False):
    faculty_dict = {} # dict name : Faculty object
    with open(rawdata, newline='') as f:
        header = f.readline().split(',')
        header = [i.strip() for i in header]
        reader = csv.reader(f)
        for i, line in enumerate(reader):
            name = line[0]
            availability = line[1:]
            faculty = Faculty(name, availability)
            faculty_dict[name] = faculty
            for i, avail_i in enumerate(availability):
                if avail_i != 'Y':
                    time_unavailable = header[i+1]
                    timeslot = timeslots[i] # indexing should be off by 1
                    assert time_unavailable == timeslot.time, f"time_unavailable {time_unavailable} does not match timeslot.time {timeslot.time}, probably an indexing issue i = {i}"
                    if verbose:
                        print("{} is unavailable at {}".format(name, time_unavailable))
                    timeslot.fac_scheduled.add(faculty)

    return faculty_dict


# * SCHEDULE MEETINGS
def meeting_scheduler(students, timeslots, faculty_dict, verbose = False):
    converged = False
    while not converged:
        converged = True # will change to False if something changes
        i = 0 # current student index
        # using while loop because we may stay at one student for multiple iterations
        while i < len(students):
            student = students[i]
            i += 1 # increment to next student
            # stu_meet = students[i]['meetings_with']
            if student.it < len(student.ranks): # we have not gone through all the student's ranks
                fac_name = student.ranks[student.it] # zeroth iteration is their first faculty rank, etc
                if fac_name in faculty_dict:
                    faculty = faculty_dict[fac_name]
                else:
                    print(f'Warning: {fac_name} not in faculty_dict! Skipping')
                    # print(faculty_dict.items())
                    continue
                student.it += 1
                ## assign the faculty rank selected to one of the timeslots
                for timeslot in timeslots:
                    if faculty not in timeslot.fac_scheduled and student not in timeslot.stu_scheduled and faculty not in student.fac_scheduled:
                        #...schedule faculty member at that timeslot...
                        timeslot.fac_scheduled.add(faculty)
                        timeslot.stu_scheduled.add(student)
                        timeslot.meetings.append((faculty,student)) # add faculty-student pair to faculty-student meetings at timeslot
                        student.fac_scheduled.add(faculty) # make a note of the faculty member scheduled w/ student(i) in student dir
                        student.timeslots.add(timeslot)
                        faculty.timeslots.add(timeslot)
                        converged = False
                        break
                else:
                    i -= 1 # decrement to stay at current student

                if verbose:
                    print("\n*************************************\n")
                    print(f"Timeslot: {timeslot}\n\nFaculty Scheduled: {timeslot.fac_scheduled}\n\nStudent Scheduled: {timeslot.stu_scheduled}\n")

    if verbose:
        print("Meetings:")
        for timeslot in timeslots:
            print(f'\n{timeslot.time}')
            for m in timeslot.meetings:
                    print("\t",m)


# * EXPORT MEETING TIMES
from datetime import date
def export_meeting_txt(dir, timeslots):
    csvList = [['Timeslot', 'Faculty', 'Student']]
    for timeslot in timeslots:
        for meeting in timeslot.meetings:
            rowList = [timeslot.time, meeting[0].name, meeting[1].name]
            csvList.append(rowList)

    with open(osp.join(dir,f"output-{date.today()}.txt"),'w',  newline = '') as f:
        wr = csv.writer(f)
        wr.writerows(csvList)



def main():
    timeslots = import_timeslot_names("./input/Timeslots.txt")
    students = import_student_facultyranks("./input/StudentAvailabilityAndRanks.csv",timeslots)
    faculty_dict = import_faculty_availability("./input/FacultyAvailability.csv", timeslots)
    meeting_scheduler(students, timeslots, faculty_dict, False)
    export_meeting_txt("./output", timeslots)

if __name__ == '__main__':
    main()
