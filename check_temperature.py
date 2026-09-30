import sys
from temperature_log import loading_measurements



def input_validation(symbol, temp):
    while True:
        if symbol not in ("<", "=", ">"):
            print("Type '<' - (lower than),  '>' - (biger than), or '=' - (equal to)")
            symbol = input()
        else:
            break

        
    while True:
        try:
            temp = float(temp)
        except Exception:
            print("Give numerical value of temperature")
            temp = input()
            continue
        break
    return symbol, temp

def check(measurements, symbol, temp):
    

    results = set()
    if symbol == "<":
        for i in measurements:
            if i["temperature"] < temp:
                results.add(i["city"])
    elif symbol == "=":
        for i in measurements:
            if i["temperature"] == temp:
                results.add(i["city"])
    elif symbol == ">":
        for i in measurements:
            if i["temperature"] > temp:
                results.add(i["city"])
    else:
        raise ValueError("Wrong symbol input")
    return sorted(results)


def main(symbol, temp):   
    measurements = loading_measurements("measurements.json")
    symbol, temp = input_validation(symbol, temp)
    results = check(measurements, symbol, temp)
    return results
            
 

if __name__ == "__main__":
    try:
        symbol = sys.argv[1]
    except IndexError:
        while True:
            symbol = input("Type '<' - (lower than),  '>' - (biger than), or '=' - (equal to)\n")
            if symbol in ("<", "=", ">"):
                break
            else:
                continue
            
        
    try:
        temp = float(sys.argv[2])
    except IndexError, ValueError:
        while True:
            temp = input("Give numerical value of temperature\n")
            try:
                temp = float(temp)
            except Exception:
                continue
            break
    print(main(symbol, temp))