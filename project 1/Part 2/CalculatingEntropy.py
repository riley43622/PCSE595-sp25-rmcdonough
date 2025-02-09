import math
from collections import Counter


user_file=input("Enter the file you would like to read please ensure it is a <.txt> file")


with open(user_file, "r") as file:
    content=file.read()
print("Your Encrypted Sample Number is:\n",content)

content = ''.join(filter(str.isdigit, content))


def calculator_entr(info):
    digits_counter=Counter(info)
    digital_length=len(info)

    if digital_length==0:
        return 0


    prob={digit: count / digital_length for digit, count in digits_counter.items()}
    entr=-sum(p* math.log2(p) for p in prob.values())
    return entr

def maxer(info):
    digital_length = len(info)
    if digital_length==0:
        return 0
    max_calc=math.log2(digital_length)

    return max_calc




print("Your Real Entropy value for this encryption is:",calculator_entr(user_file))
print("Your Max Entropy value for this encryption is:",maxer(user_file))

