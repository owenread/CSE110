"""
For creativity I decided to throw in a while loop to allow the user to keep
inputting years until they want to exit. I also added an over all time and countries 
average in the summary. 

Analizing the data for life expectancy

- Cool thing I learned is that you should not use ^ 
for an exponential, rather you should use **. I had
no idea the caret symbol had other operations!

Author: Owen Read
"""

while True:

    # user input year
    user_input = input("Enter the year of interest or 'stop' to exit: ")

    # break the loop if user wants to exit
    if user_input.lower() == "stop":
        print("Have a good day!")
        break
    chosen_year = int(user_input)
    # open the dataset
    with open("life-expectancy.csv") as web_file:
        # declare all variables

        # variables for overall data 
        overall_lowest_life = 10**21
        overall_lowest_life_country = ""
        overall_lowest_life_year = 0

        overall_highest_life = -1
        overall_highest_life_country = ""
        overall_highest_life_year = 0

        #variables for evaluating the overall average
        overall_life_total = 0
        overall_life_count = 0

        # chosen year specific variables
        year_lowest_life = 10**21
        year_lowest_life_country = ""

        year_highest_life = -1
        year_highest_life_country = ""

        # variables for evaluating the average for the chosen year
        year_life_total = 0
        year_life_count = 0

        # remove the header to process the data
        header = next(web_file)

        #iterate through the data by line
        for line in web_file:

            # remove end line
            no_end_line = line.strip()
            # split on ","
            info = no_end_line.split(",")

            country = info[0].title()
            year = int(info[2])
            life_expectancy = float(info[3])

            # Get the overall totals to evaluate the average later
            overall_life_total += life_expectancy
            overall_life_count += 1

            # highest life expectancy
            if life_expectancy > overall_highest_life:
                overall_highest_life = life_expectancy
                overall_highest_life_country = country
                overall_highest_life_year = year
            
            # lowest life expectancy
            if life_expectancy < overall_lowest_life:
                overall_lowest_life = life_expectancy
                overall_lowest_life_country = country
                overall_lowest_life_year = year

            # work with data in the chosen year
            if year == chosen_year:
                # add together the life expectancy data to get the average later
                year_life_total += life_expectancy
                year_life_count += 1

                # country with highest life expectancy
                if life_expectancy > year_highest_life:
                    year_highest_life = life_expectancy
                    year_highest_life_country = country

                # country with lowest life expectancy
                if life_expectancy < year_lowest_life:
                    year_lowest_life = life_expectancy
                    year_lowest_life_country = country

    # outputs

    # overall output
    print("")
    print(f"The overall max life expectancy is: {overall_highest_life} from {overall_highest_life_country} in {overall_highest_life_year}.")
    print(f"The overall min life expectancy is: {overall_lowest_life} from {overall_lowest_life_country} in {overall_lowest_life_year}.")
    print("")

    # overall average 
    if overall_life_count > 0:
        overall_average = overall_life_total / overall_life_count
        print(f"The overall average life expectancy across the world and all available years is: {overall_average:.2f}")

    # chosen year output
    if year_life_count > 0:
        # get the average life expectancy for the year
        year_average = year_life_total / year_life_count
        
        print(f"For the year {chosen_year}:")
        print(f"The average life expectancy across all countries was {year_average:.2f}")
        print(f"The max life expectancy was in {year_highest_life_country} with {year_highest_life}")
        print(f"The min life expectancy was in {year_lowest_life_country} with {year_lowest_life}")
        print("")

    # output if user put in a year not in the data
    else:
        print(f"There's nothing for the year, '{chosen_year}'.")
        print("")


