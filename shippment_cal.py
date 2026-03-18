'''
Shipping Calculator
Goal: < 2kg ($5), 2-10kg ($10), > 10kg ($20). Add $5 if Express is True.
| Input | Output |
| :--- | :--- |
| 1 (kg), False | $5.00 |
| 5 (kg), True | $15.00 |

'''
weight = int(input("Enter the weight"))
express = input("Do you want Express ").lower()
# true , false "true" True TRUE -> true
if weight < 2:
    total = 5
elif weight<10:
    total = 10
else:
    total = 20

if express == "true":
    total += 5
    
print(total)