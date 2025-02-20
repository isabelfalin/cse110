year_largest = 0
answer = int(input("Enter the year of interest: "))
country_answer = input("Enter a country/continent: ")

min_life_country = 10000
max_life_country = -1
min_year_country = None
max_year_country = None

max_life = -1
min_life = 10000

min_life_answer = 10000
max_life_answer = -1
min_country_answer = None
max_country_answer = None
total = 0
counter = 0

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
            max_year = year

        if life_expetancy < min_life:
            min_life = life_expetancy
            min_country = country
            min_year = year

        if year == answer:
            total += life_expetancy
            counter += 1
            if life_expetancy > max_life_answer:
                max_life_answer = life_expetancy
                max_country_answer = country

            if life_expetancy < min_life_answer:
                min_life_answer = life_expetancy
                min_country_answer = country

        
        if country.lower() == country_answer.lower():
            if life_expetancy > max_life_country:
                max_life_country = life_expetancy
                max_year_country = year

            if life_expetancy < min_life_country:
                min_life_country = life_expetancy
                min_year_country = year



    print(f"The overall max life expectancy is: {max_life} from {max_country} in {year}")
    print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")

print(f"For the year: {answer}")
print()
print(f"The average life expectancy across all countries is: {total / counter:.2f}")
print(f"The max life expectancy was in {max_country_answer} with {max_life_answer} ")
print(f"The min life expectancy was in {min_country_answer} with {min_life_answer}")

if max_year_country == None:
    print(f"{country_answer} is not a valid country/continent")
else:
    print()
    print(f"For the country: {country_answer.capitalize()}")
    print()
    print(f"The max life expectancy was in {max_year_country} with {max_life_country} ")
    print(f"The min life expectancy was in {min_year_country} with {min_life_country}")

                
                

               
                       


# For the year 1959:
# The average life expectancy across all countries was 54.95

# The max life expectancy was in Norway with 73.49
# The min life expectancy was in Mali with 28.077
