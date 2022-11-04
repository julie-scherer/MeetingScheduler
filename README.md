# Meeting scheduler program

## Personal note

I created this program a couple years back when I was working as an administrator in higher education. In fact, this was the first Python script I ever wrote! I haven't made any changes to the original code, as I want this to be something I can look back on and see my growth and progress over the many years to come.

## Background

I was charged with the incredibly difficult task of scheduling one-on-one interviews or meetings between 50-60 faculty and 80-100 prospective students for our admissions/recruitment weekend. Just to illustrate the complexity, consider these constraints:
- Students were asked to list the names of faculty they would like to meet with in order of preference. The objective was to schedule each student for _at least_ 3-4 meetings (but could go anywhere upward 9-10 in total), with at least 1 of the meetings being with one of their top 3 preferences.
- All meetings needed to be scheduled within a 7-hour timeblock (e.g., from 1-5pm on day 1 and 9-12pm on day 2).
- Both faculty _and_ student availability needed to be factored in (yes, students included, as some will arrive later in the weekend and others had to leave early).
- A complete, polished schedule needed to ready in less than **_one week_** due to other, contingent tasks.

I'm sure any administrator reading this, current or former, can relate to exactly how difficult and frustrating this kind of task can be! So, my solution? Write a Python script to automate the process for me! While it's unlikely I will ever use this program again as I've moved on to pursue a career in technology, I hope this can at least be a helpful starting point for others working in administration or higher education.


## Repository overview

There are 3 main components to this repo: the input, output, and Python script. Input files are stored in the [`input`](https://github.com/schererjulie/MeetingScheduler/tree/main/input) folder, output files are saved in the [`output`](https://github.com/schererjulie/MeetingScheduler/tree/main/output) folder, and [`run.py`](https://github.com/schererjulie/MeetingScheduler/blob/main/run.py) is where the magic happens.

    App
    |- input
    |- output
    |- run.py


## Running the program

* Use the command line to create and navigate to the directory where you will store the repo on your local computer

    ```
    mkdir meeting_scheduler
    cd ~/meeting_schduler
    ```

* Clone/fork the git repo

    ```
    git clone https://github.com/schererjulie/MeetingScheduler.git
    ```

* Update the `FacultyAvailability.csv` and `StudentAvailabilityAndRanks.csv` files in the `input` folder
    
    You can do this by simply copying and pasting your data into the csv, or you can find some other creative way to load the data. For instance, I wrote the `replace_names.py` script to deidentify the faculty and students before posting on Github -- maybe you can make use of this somehow!

    But whatever you do, **be careful not to change the column headers, name of the files, or just the general format/structure and syntax within the files**. If you do, you may need to update the `run.py` script, e.g., the header indexes or file names.

* Update `input/Timeslots.txt` with the exact same time slots you used as headers in the csv files

* Run the script via one of the options below

    **Option 1**
    * Create a virtual environment

        ```
        python3 -m venv venv
        ```

    * Install requirements

        ```
        pip install -r requirements.txt
        ```

    * Run the script from the command line

        ```
        python3 run.py
        ```

    **Option 2**
    * Install Docker. If you don't already have Docker installed:
        - [A easy-to-follow cheat sheet for installing Docker](https://github.com/wsargent/docker-cheat-sheet#installation)
        - Instructions to install Docker Desktop can be found in the [documentation](https://docs.docker.com/get-docker/)

    * Run the Python script via the [Python Docker image](https://hub.docker.com/_/python)

        ```
        // run the Docker image directly
        docker run -it --rm --name my-running-script -v "$PWD":/app -w /app python:3 python run.py

        // or, if preferred, build and run Docker image
        docker build -t meeting-scheduler .
        docker run -v "$PWD"/output:/output meeting-scheduler
        ```

Assuming everything worked as expected, you will find a list of all the one-on-one meetings saved in the `output` folder
    
    \\ sample output

    Timeslot,Faculty,Student
    F 1:00 PM,Faculty8,Student1
    F 1:00 PM,Faculty40,Student2
    F 1:00 PM,Faculty4,Student3
    F 1:00 PM,Faculty9,Student6


Thanks for reading! Happy coding!