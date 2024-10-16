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

def find_highest_number(var1, var2, var3, var4, var5):
    if var1 > var2:
        return var1
    elif var1 > var3:
        return var1
    elif var1 > var4:
        return var1
    elif var1 > var5:
        return var1
    

result = find_highest_number(5, 4, 3, 2, 1)
print(result)
