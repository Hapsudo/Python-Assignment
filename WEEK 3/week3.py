#Question 1
def calculate_discount(price, discount_percent):
    #Apply discount only if it is greater or equal to 20%
    if discount_percent >= 20:
        return price - (price * (discount_percent/100))
    else:
        return price
    

 #Question 2
 #prompts user for input
price = float(input("Enter the original price of the item: "))
discount_percent =float(input("Enter the discount percentage: "))

#Calculating final price
final_price = calculate_discount(price, discount_percent)

#Printing final price
print(f"The final price is: {final_price}")

    