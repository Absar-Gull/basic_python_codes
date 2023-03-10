food_chart={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
try:
    ts=0
    item=input("item:")
    item=item.lower()
    item=item.title()
    pr=food_chart[item]
    print(f"Cost of {item} =", pr)
    ts+=pr
    for _ in food_chart:
    
        item=input("Add another item or press 'ctrl+d' to end order: ")
        item=item.title()
        
        if item not in food_chart:
            continue
        pr=food_chart[item]
        print(f"Cost of {item} =", pr)
        ts +=pr
        print("Total amount to be paid:",ts, "$")

except EOFError:
    print("\nTotal amount to be paid:",ts, "$")
    
