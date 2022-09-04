# john Chat-of-Fisherman, a good man, bought a microcomputer to monitor the daily income of his work.
# Every time he brings in a weight of fish greater than that established by the fishing regulations of the state of São Paulo (50 kilos), 
# he must pay a fine of R$ 4.00 per excess kilo.
# John needs you to write a program that reads the weight variable (fish weight) and calculates the excess.
# Record in the excess variable the amount of kilos beyond the limit and in the fine variable the amount of the fine that João must pay. 
# Print the program data with the appropriate messages.

weight = int(input("fish weight:"))

count = 4

if weight > 50:
    sub = weight - 50
    fine = sub * count
    print("you will pay a fine:", fine,"dollars")
else: 
    print("Good! without much")