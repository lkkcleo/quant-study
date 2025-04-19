def simple_interest(principal,interest_rate,time):
    return principal*interest_rate*time

def compond_interest(principal,interest_rate,time):
    return (principal*pow((1+interest_rate),time)-principal)
