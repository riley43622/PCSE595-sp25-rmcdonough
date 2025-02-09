import secrets as guilty_spark


storage=input("Enter how many random numbers you would like generated")
storage=int(storage)
file_entry=input("Enter which file you would like these written too Make sure to specify what type of file E.G <.txt>.")

secure_int = guilty_spark.randbelow(storage)

random_digits = ''.join(str(guilty_spark.randbelow(storage)) for _ in range(storage))
print(random_digits)



with open (file_entry,"w") as file:
    file.write("".join(random_digits))
