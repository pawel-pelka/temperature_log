import json


def average_temp(measurements):
    if len(measurements) == 0:
        raise ValueError("No measurements")
    sum_T = 0
    for i in measurements:
        sum_T = sum_T + i["temperature"] 
    average_T = sum_T / len(measurements)
    return average_T

def average_cities_T(measurements):
    cities_total_T = {}
    cities_average_T = {}
    for i in measurements:
        if  i["city"] not in cities_total_T:
            cities_total_T[i["city"]] = {"total_T": 0, "total_m": 0}
    for i  in measurements:
        cities_total_T[i["city"]]["total_T"] = cities_total_T[i["city"]]["total_T"] + i["temperature"]
        cities_total_T[i["city"]]["total_m"] = cities_total_T[i["city"]]["total_m"] + 1
    for i in cities_total_T:
        cities_average_T[i] = cities_total_T[i]["total_T"] / cities_total_T[i]["total_m"]
    return cities_average_T


def warmest_cities(measurements):
    j = 0
    warmest_cities = []
    for number, i in enumerate (measurements):
        if i["temperature"] > measurements[j]["temperature"]:
            warmest_cities.clear()
            j = number
            warmest_cities.append(i["city"])
        if i["temperature"] == measurements[j]["temperature"]:
            if warmest_cities == []:
                warmest_cities.append(i["city"])
            elif i["city"] not in warmest_cities:
                warmest_cities.append(i["city"])
    return warmest_cities

def loading_measurements(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            measurements = json.load(file)
    except FileNotFoundError:
        measurements = []
    except json.JSONDecodeError:
        print(f"could't read the {filename}, invalid JSON")
        raise SystemExit(1)
    return measurements 

def saving_measurements(filename, measurements):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(measurements, file, indent = 4)



def main():
    measurements = loading_measurements("measurements.json")

    print("Do you want to add new measurement? (y/n)")
    while True:
        answer = input()
        if answer not in ("y", "n"):
            print("Wrong input, type 'y' for yes, or 'n' for no")
            continue

        elif answer == "y":
            city = input('At which city measurement was done?\n')
            print("What temperature was measured?[°C]")
            while True:
                try:
                    temperature = float(input())
                except ValueError:
                    print("Wrong input, give a numerical value of temeprature")
                    continue
                break
            measurements.append({"city": city, "temperature": temperature})
            print("Do you want to add another measurement?")

        else:
            if not measurements:
                print("You haven't saved any measurements")
            else:
                print(f"There is {len(measurements)} measurements")
                for number, i in enumerate(measurements, start=1):
                    print(f"Measurement {number}: city: {i["city"]},"
                    f" temperature: {i["temperature"]} °C")
                print(f"the average temperature from measurements was"
                f" {average_temp(measurements)} °C\n"
                f"and the warmest cities are {warmest_cities(measurements)}.\n"
                f"Average temperatue in cities:")
                cities_average_T = average_cities_T(measurements)
                for i in cities_average_T:
                    print(f"{i}: {cities_average_T[i]}")

            break
    
            
    saving_measurements("measurements.json", measurements)

if __name__ == "__main__":
    main()

    



