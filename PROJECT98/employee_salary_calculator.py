# PROJECT NO =  98
# EMPLOYEE SALARY CALCULATOR

def calculate_hra(basic_salary):
    hra = basic_salary * 20 / 100
    return hra

def calculate_da(basic_salary):
    da = basic_salary * 10 / 100
    return da

def calculate_pf(basic_salary):
    pf = basic_salary * 12 / 100
    return pf

def calculate_gross(basic_salary, hra, da):
    gross_salary = basic_salary + hra + da
    return gross_salary

def calculate_tax(gross_salary):

    if gross_salary <= 25000:
        tax = 0

    elif gross_salary <= 50000:
        tax = gross_salary * 5 / 100

    else:
        tax = gross_salary * 10 / 100

    return tax


def calculate_net(gross_salary, pf, tax):
    net_salary = gross_salary - pf - tax
    return net_salary

def print_slip(name, employee_id, basic_salary,
               hra, da, pf, gross_salary, tax, net_salary):

    print("\n")
    print("==========================================")
    print("           EMPLOYEE SALARY SLIP")
    print("==========================================")

    print("Employee Name  :", name)
    print("Employee ID    :", employee_id)

    print("------------------------------------------")

    print("Basic Salary   : Rs.", basic_salary)
    print("HRA (20%)      : Rs.", hra)
    print("DA (10%)       : Rs.", da)
    print("Gross Salary   : Rs.", gross_salary)

    print("------------------------------------------")

    print("PF (12%)       : Rs.", pf)
    print("Tax            : Rs.", tax)

    print("------------------------------------------")

    print("Net Salary     : Rs.", net_salary)

    print("==========================================")
    print("          THANK YOU!")
    print("==========================================")


def main():

    print("==========================================")
    print("       EMPLOYEE SALARY CALCULATOR")
    print("==========================================")

    while True:

        name = input("\nEnter Employee Name: ").strip()

        if not name:
            print("Invalid name. Please enter a name.")
            continue

        employee_id = input("Enter Employee ID: ").strip()

        if not employee_id:
            print("Invalid ID. Please enter Employee ID.")
            continue

        try:
            basic_salary = float(input("Enter Basic Salary: "))

            if basic_salary <= 0:
                print("Invalid salary. Enter a positive number.")
                continue

        except ValueError:
            print("Invalid salary. Please enter a number.")
            continue

        hra = calculate_hra(basic_salary)

        da = calculate_da(basic_salary)

        pf = calculate_pf(basic_salary)

        gross_salary = calculate_gross(
            basic_salary, hra, da
        )

        tax = calculate_tax(gross_salary)

        net_salary = calculate_net(
            gross_salary, pf, tax
        )

        print_slip(
            name,
            employee_id,
            basic_salary,
            hra,
            da,
            pf,
            gross_salary,
            tax,
            net_salary
        )

        choice = input(
            "\nDo you want to calculate another employee salary? (yes/no): "
        ).strip().lower()

        if choice != "yes":
            print("\nThank you for using Employee Salary Calculator!")
            break

if __name__ == "__main__":
    main()
