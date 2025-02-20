year_largest = 0
answer = input("Enter the year of interest: ")
max_life = -1
min_life = 10000

with open("life-expectancy.csv") as data_file:
    next(data_file)
    for line in data_file:
        split_person = line.strip().split(",")
        country = split_person[0]
        abbriviation = split_person[1]
        year = int(split_person[2])
        life_expetancy = float(split_person[3])

        if life_expetancy > max_life:
            max_life = life_expetancy
            max_country = country

        if life_expetancy < min_life:
            min_life = life_expetancy
            min_country = country
            min_year = year
    print(f"The overall max life expectancy is: {max_life} from {max_country} in {year}")
    print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")

               
                       



# Enter the year of interest: 1959

# The overall max life expectancy is: 86.751 from Monaco in 2019
# The overall min life expectancy is: 17.76 from Iceland in 1882
