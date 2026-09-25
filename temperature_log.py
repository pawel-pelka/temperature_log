import json


def average_temp(measurements):
    sum_T = 0
    for i in measurements:
        sum_T = sum_T + i["temperature"] 
    average_T = sum_T / len(measurements)
    return average_T
            
    
try:
    with open("measurements.json", "r", encoding="utf-8") as file:
        measurements = json.load(file)
except FileNotFoundError:
    measurements = []


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
            print("You haven't save any measurements")
        else:
            print(f"There is {len(measurements)} measurements")
            for number, i in enumerate(measurements, start=1):
                print(f"Measurement {number}: city: {i["city"]},"
                f" temperature: {i["temperature"]} °C")
            print(f"the average temperature from measurements was"
            f" {average_temp(measurements)} °C")
        break
        

with open("measurements.json", "w", encoding="utf-8") as file:
    json.dump(measurements, file, indent = 4)

        

    



