import sys
if len(sys.argv) == 3:
    n1 = sys.argv[1]
    n2 = sys.argv[2]
    print("User provided input values:")
else:
    print("No input given - using default values:")
    n1 = "2"
    n2 = "1"
    n1=eval(n1)
    n2=eval(n2)
num = n1 / n2
print("n1")
print(n1)
print("n2")
print(n2)
print("n1 divided by n2 is:num")
