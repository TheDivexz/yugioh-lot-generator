import os
import random

card_packs = '../card_packs'
# Number of Lots Desired
number_of_lots = 10
# number of cards a player should get per pack
cards_per_pack = 2
generated_lots = []
lots = []

for i in range(number_of_lots):
    generated_lots.append('../generated/package_'+str(i+1)+'.txt')

for i in generated_lots:
    lots.append(open(i,'w'))


for filename in os.scandir(card_packs):
    if filename.is_file():
        card_list = open(filename,'r').readlines()
        for lot in lots:
            for x in range(2):
                lot.write(card_list[random.randint(0,len(card_list)-1)])
