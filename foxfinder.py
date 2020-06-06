import random


def pick_fox():
    while True:
        # fox_box = {
        #     1:'Kaga',
        #     2:'Akagi'
        # }
        # for x in fox_box:
        #     print(x, '->', fox_box[x])
        # pick_fox = int(input('Pick a fox to find'))
        spacing = 0
        find_foxes()
        print('Another fox?')
        mainyn = input('YN?').casefold()
        if mainyn == 'n':
            break


# def find_foxes(times):
#    times = int(input('How many runs?'))
#    pick_fox()


def find_foxes():
    counter = 0
    total_counter = 0
    total_Akagi = 0
    total_Kaga = 0
    total_foxes = 0
    got_fox = False
    while got_fox == False:
        fox_looker = random.randint(0, 10000)
        print(fox_looker, 'says RNG')
        total_counter = total_counter + 1
        if fox_looker > 75:
            counter = counter + 1
            print('no fox here!')
        elif fox_looker <= 75:
            # print('Found a fox!')
            total_foxes = total_foxes + 1
            fox_chooser = random.randint(0, 10)
            if fox_chooser > 5:
                print('Found Kaga!')
                print(counter, 'tries')
                total_Kaga = total_Kaga + 1
            elif fox_chooser < 6:
                print('Found Akagi!')
                print(counter, 'tries')
                total_Akagi = total_Akagi + 1
            got_fox = True
        # print(total_counter, 'runs,', total_foxes, 'foxes', total_Akagi, 'Akagi', total_Kaga, 'Kaga')
        # this part isn't right, need to aggregate one more step


pick_fox()
