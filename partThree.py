def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    # TODO
    sign = d.replace("£","")
    return float(sign)

def percent_to_float(p):
    # TODO
     signper = p.replace("%","")
     return (float(signper))/100
main()
