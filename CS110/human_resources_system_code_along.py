with open("hr_system.txt") as hr_data:
    
    # Skipping the first line 'header data'
    header = next(hr_data)
    for line in hr_data:
        # removing the end line
        no_end_line = line.strip()
        #splitting info based on " "
        info = no_end_line.split(" ")

        name = info[0].capitalize()
        id_number = int(info[1])
        job_title = info[2].capitalize()
        salary = float(info[3])
        paycheck = salary / 24

        # bonus of $1,000 to the engineers
        if (job_title == "Engineer"):
            paycheck = paycheck + 1000


        print(f"Here is the user data: {name} (ID: {id_number}), {job_title} - ${paycheck:.2f}")

