# Lab01vst.py
# The Mortgage Payment Program
# This is the student starting file of the Lab01 Assignment.
# Evin Lodder
# Date/Version: 8/26/22


def calc_monthly_payment(principal: float | int, interest: float, months: float | int) -> float:
    # calculate decimal monthly interest (R)
    monthly_interest: float = interest / 100 / 12
    # (1 + R)^N
    to_n_power: float = (1 + monthly_interest) ** months
    # R * (1 + R)^N
    numerator: float = to_n_power * monthly_interest
    # (1 + R)^N - 1
    denominator: float = to_n_power - 1
    fraction: float = numerator / denominator
    return fraction * principal


def main():
    # get inputs from user, turn years to months
    principal: float | int = eval(input("Enter principal: "))
    rate: float | int = eval(input("Enter annual rate: "))
    years: int = eval(input("Enter number of years: "))
    months: int = years * 12
    # get monthly payment, then calculate total payments and interest
    monthly_payments: float = round(calc_monthly_payment(principal, rate, months), 2)
    total_pay: float = round(monthly_payments * months, 2)
    total_interest: float = round(total_pay - principal, 2)
    # print output
    print(f"""
Principal:       ${principal}
Annual Rate:      {rate}%
Number of Years:  {years}
Monthly Payment: ${monthly_payments}
Total Payments:  ${total_pay}
Total Interest:  ${total_interest}
""")


if __name__ == "__main__":
    main()
