import random, timeit


#set default rarity odds
rarity_3s = float(40)
rarity_4s = float(50)
rarity_5s = float(8)
rarity_6s = float(2)

#number of rolls since last 6 star
rolls_no_6s = 0

#main function
def Perform_Roll(roll_count):
    start_time = timeit.default_timer()
    #roll and track rarity of all rolls
    total_rarity = [0, 0, 0, 0]
    for _ in range(roll_count):
        rolled_rarity = Simulate_Roll_Rarity()
        match rolled_rarity:
            case [3]:
                total_rarity[0] += 1
            case [4]:
                total_rarity[1] += 1
            case [5]:
                total_rarity[2] += 1
            case [6]:
                total_rarity[3] += 1

    #print results
    print("Roll Results:")
    print("3 stars:", total_rarity[0])
    print("4 stars:", total_rarity[1])
    print("5 stars:", total_rarity[2])
    print("6 stars:", total_rarity[3])
    print("Total:", sum(total_rarity))
    print("Time Taken: %.2f seconds." % (timeit.default_timer() - start_time))

#roll for star rarity
def Simulate_Roll_Rarity():
    global rolls_no_6s
    if rolls_no_6s >= 99:
        Reset_Pity()
        return [6]
    else: 
        Perform_Pity()
        rarity_weights = [rarity_3s, rarity_4s, rarity_5s, rarity_6s]
        result = random.choices([3, 4, 5, 6], weights=(rarity_weights), k = 1)
        if result != [6]:
            rolls_no_6s += 1
        elif result == [6]:
            Reset_Pity()
            pass
        return result

#change odds for pity
def Perform_Pity():
    if rolls_no_6s >= 50:
        global rarity_3s, rarity_4s, rarity_5s, rarity_6s

        rarity_6s += 2
        x = float(2 / (rarity_3s + rarity_4s + rarity_5s))
        rarity_5s -= (x * rarity_5s)
        rarity_4s -= (x * rarity_4s)
        rarity_3s -= (x * rarity_3s)

#reset rarity to default
def Reset_Pity():
    global rarity_3s, rarity_4s, rarity_5s, rarity_6s, rolls_no_6s
    rarity_3s = float(40)
    rarity_4s = float(50)
    rarity_5s = float(8)
    rarity_6s = float(2)
    rolls_no_6s = 0


#ask for number of rolls to perform
while True:
    roll_request = input("Enter number of rolls to perform: ")
    if roll_request.isdigit():
        roll_request = int(roll_request)
        Perform_Roll(roll_request)
    else:
        print("Please Enter an Integer.")
