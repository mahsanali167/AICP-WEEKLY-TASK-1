def input_data():
    names = []
    weights_first_day = []
    weights_last_day = []

    print("Enter the names and weights of 30 pupils for the first day of term:")
    for i in range(1, 31):
        name = input(f"Enter name of pupil {i}: ")
        weight_first_day = float(input(f"Enter weight of pupil {i} on the first day of term in kilograms: "))
        weight_last_day = float(input(f"Enter weight of pupil {i} on the last day of term in kilograms: "))

        names.append(name)
        weights_first_day.append(weight_first_day)
        weights_last_day.append(weight_last_day)

    return names, weights_first_day, weights_last_day

def calculate_weight_difference(weights_first_day, weights_last_day):
    differences = [last - first for first, last in zip(weights_first_day, weights_last_day)]
    return differences

def output_data(names, weights_first_day, weight_differences):
    print("\nNames and weights of pupils for the first day of term:")
    for name, weight in zip(names, weights_first_day):
        print(f"Name: {name}, Weight: {weight}kg")

    print("\nWeight differences between the first and last day of term:")
    for name, difference in zip(names, weight_differences):
        print(f"Name: {name}, Weight difference: {difference:.2f}kg")

    print("\nPupils with a weight difference exceeding 2.5 kilograms:")
    for name, difference in zip(names, weight_differences):
        if abs(difference) > 2.5:
            change_type = "rise" if difference > 0 else "fall"
            print(f"{name}: Weight difference: {abs(difference):.2f}kg, {change_type}")

def main():
    names, weights_first_day, weights_last_day = input_data()

    weight_differences = calculate_weight_difference(weights_first_day, weights_last_day)

    output_data(names, weights_first_day, weight_differences)

if __name__ == "__main__":
    main()
