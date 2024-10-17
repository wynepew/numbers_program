#define 5 variables
#compare var1 & var2
#if var1 is greater than var2
    #compare var1 to var3
    #if var1  is greater than var3
    #compare var1 to var4
    #if var1  is greater than var4
    #compare var1 to var5
    #if var1  is greater than var5
    #print var1
#if not
    #any var that is greater than var1
    #repeat the process till the last var
    #if the greater var is determined
    #print var n

# Step 1: Define 5 variables
var1 = int(input("Please enter a number for var1: "))
var2 = int(input("Please enter a number for var2: "))
var3 = int(input("Please enter a number for var3: "))
var4 = int(input("Please enter a number for var4: "))
var5 = int(input("Please enter a number for var5: "))

# Step 2: Compare var1 and var2
if var1 > var2:
    highest = var1
else:
    highest = var2

# Step 3: Compare the highest with var3
if highest < var3:
    highest = var3

# Step 4: Compare the highest with var4
if highest < var4:
    highest = var4

# Step 5: Compare the highest with var5
if highest < var5:
    highest = var5

# Step 6: Print the highest number
print(f"The highest number is: {highest}")
