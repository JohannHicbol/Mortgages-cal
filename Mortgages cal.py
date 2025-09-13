
class MonthlyPaymentFormula:
    def __init__(self):
        #self.down_payment = 5000
        #self.interest_rate = 6.91
        #self.mortgage_term = 1
        #self.principal = 10000
        self.down_payment = int(input("How much is the down payment: "))
        self.interest_rate = float(input("Enter the interest_rate: "))
        self.mortgage_term = int(input("Enter the duration of mortgage: "))
        self.principal = int(input("What the is the cost of the home: "))
        self.PERCENT = 100
        self.MONTHS_IN_THE_YEAR = 12
    def __repr__(self):
        if self.mortgage_term ==30:
            return (f"With a {(float(self.down_payment / self.principal)):,.0%} down payment of ${self.
            down_payment:,.2f}. A ${self.principal:,.2f} monthly mortgage on a {self.mortgage_term}yr."
            f"fixed with a {self.interest_rate:.2f}% APR is: ${self.c:,.2f} a month.")
        elif self.mortgage_term ==15:
            return (f"With a {(float(self.down_payment / self.principal)):,.0%} down payment of ${self.
            down_payment:,.2f}. A ${self.principal:,.2f} monthly mortgage on a {self.mortgage_term}yr."
            f"fixed with a {self.interest_rate:.2f}% APR is: ${self.c:,.2f} a month.")
        elif self.mortgage_term ==10:
            return (f"With a {(float(self.down_payment / self.principal)):,.0%} down payment of ${self.
            down_payment:,.2f}. A ${self.principal:,.2f} monthly mortgage on a {self.mortgage_term}yr."
            f"fixed with a {self.interest_rate:.2f}% APR is: ${self.c:,.2f} a month.")
        else:
            return (f"With a {(float(self.down_payment / self.principal)):,.0%} down payment of ${self.
            down_payment:,.2f}. A ${self.principal:,.2f} monthly mortgage on a {self.mortgage_term}yr."
            f"fixed with a {self.interest_rate:.2f}% APR is: ${self.c:,.2f} a month.")

    def mortgage_Calculation(self):
        self.d = self.down_payment
        self.r = self.interest_rate / self.PERCENT / self.MONTHS_IN_THE_YEAR
        self.n = -abs(self.mortgage_term) * self.MONTHS_IN_THE_YEAR
        self.p = self.principal
        self.c = (self.r * (self.p - self.d)) / (1-((1+ self.r)**self.n))
        return (self.c)

    def totalInterestPaid(self):
        self.i = ((self.c * (self.n / self.MONTHS_IN_THE_YEAR))-self.p) - -abs(self.p)
        print(f"Interest Amount Paid: ${abs(self.i):,.2f}")

    def totalPaidWithInterest(self):
        self.i = (self.c * (self.n / self.MONTHS_IN_THE_YEAR)-self.p)
        print(f"Total Paid With Interest: ${abs(self.i):,.2f}")
m1 = MonthlyPaymentFormula()
m1.mortgage_Calculation()
m1.totalInterestPaid()
m1.totalPaidWithInterest()
print(m1)