# Meeting scheduler program

### Personal note

I created this program a couple years back when I was working as an administrator in higher education. In fact, this was the first Python script I ever wrote! I haven't made any changes to the original code, as I want this to be something I can look back on and see my growth and progress over the many years to come.

### Background

I was charged with the incredibly difficult task of scheduling one-on-one interviews or meetings between 50-60 faculty and 80-100 prospective students for our admissions/recruitment weekend. Just to illustrate the complexity, consider these constraints:
- Students were asked to list the names of faculty they would like to meet with in order of preference. The objective was to schedule each student for _at least_ 3-4 meetings (but could go anywhere upward 9-10 in total, with at least 1 of the meetings being with one of their top 3 preferences.
- All meetings needed to be scheduled within a pre-determined, fairly constrained timeblock (e.g., from 1-5pm on day 1 and 9-12pm on day 2 for a total of 7 hours).
- Both faculty _and_ student availability need to be factored in (yes, students included, as some will arrive later in the weekend and others had to leave early).
- A complete, polished schedule needed to ready in less than **_one week_**, as it needed to be approved/confirmed by the faculty afterwards and then we needed to create and send the students their individual schedules so they had adequate time to prepare before the event.

I'm sure any [former] administrator reading this can relate to exactly how difficult and frustrating this kind of task can be! So, my solution? Write a Python script to automate the process for me! While it's unlikely I will ever use this program again as I've moved on to pursue a career in technology, I hope this can be at minimum at helpful starting point for others working in administration or higher education.


### About the program

There are 3 main components to this repo: the input, output, and Python script

    App
    |- input
    |- output
    |- run.py

Input files are stored in the `input` folder, output files are saved in the `output` folder, and `run.py` is where the magic happens.

Now here's what you need to do to get started and run the program:

1. Update the `FacultyAvailability.csv` and `StudentAvailabilityAndRanks.csv` files in the `input` folder
    
    You can do this by simply copying and pasting your data into the csv, or you can find some other creative way to load the data. For instance, I wrote the `replace_names.py` script to deidentify the faculty and students before posting on Github -- maybe you can make use of this somehow!

    But whatever you do, be careful not to change the column headers, name of the files, or just the general format/structure and syntax within the files. If you do, you may need to update the `run.py` script, e.g., the header indexes or file names.

2. Update `input/Timeslots.txt` with the exact same time slots you used as headers in the csv files. 

3. Run the script

    ```
    cd ~\path\to\main\dir
    python3 run.py
    ```

Assuming everything went as planned, you will find a list of all the one-on-one meetings saved in the `output` folder. 

Happy coding!