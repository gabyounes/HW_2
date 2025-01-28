def calculate_net_salary():
    try:
        gross = float(input("Enter the gross salary: "))
        children = int(input("Enter the number of children: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Determine the tax rate based on gross salary
    if gross < 1000:
        tax_rate = 10
    elif gross < 2000:
        tax_rate = 12
    elif gross < 4000:
        tax_rate = 14
    else:
        tax_rate = 18

    # Determine the tax cut per child based on gross salary
    if gross < 2000:
        tax_cut_per_child = 1
    else:
        tax_cut_per_child = 0.5

    # Calculate the total tax cut
    total_tax_cut = children * tax_cut_per_child

    # Ensure total tax cut doesn't drop the tax rate below 0
    final_tax_rate = max(0, tax_rate - total_tax_cut)

    # Calculate net salary
    net = gross * (1 - final_tax_rate / 100)

    print(f"The net salary is: {net}")

# Call the function to execute
calculate_net_salary()