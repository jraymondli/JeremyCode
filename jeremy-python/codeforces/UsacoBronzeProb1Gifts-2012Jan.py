GiftsMoney = raw_input().split(' ')
gifts = int(GiftsMoney[0])
money = int(GiftsMoney[1])
minGiftPrices = []
totalGiftPrice = 0
counter = 0
giftsBought = 0

GiftCosts = []
GiftPrices = []


for x in range(gifts):
    GiftCosts.append(raw_input().split(' '))
    GiftPrices.append(int(GiftCosts[x][0])+int(GiftCosts[x][1]))
    totalGiftPrice = totalGiftPrice + int(GiftCosts[x][0])+int(GiftCosts[x][1])

print GiftCosts

for x in range(gifts):
    GiftPrices = []                 
    for y in range(gifts):             
        if counter != y:            
            GiftPrices.append(int(GiftCosts[y][0])+int(GiftCosts[x][1]))
        elif counter == y:
            GiftPrices.append(int(GiftCosts[y][0])/2+int(GiftCosts[x][1]))
        print counter, GiftPrices
        while totalGiftPrice < money:                                                     
            totalGiftPrice.append('0')
    counter = counter + 1


print totalGiftPrice


'''
while totalGiftPrice < money:
    counter = min(GiftPrices)
    minGiftPrices.append(counter)
    totalGiftPrice = totalGiftPrice + int(counter)
    GiftPrices.remove(counter)

counter = 0

while x in range(gifts):
    x = x + 1
    try:
        if int(GiftCosts[x][0])/2+int(GiftCosts[x][1]) > money:
            counter = counter + 1
    except IndexError:
        break
print gifts, counter
if counter >= gifts:
    print 0
    exit()
    
if totalGiftPrice + int(GiftCosts[len(minGiftPrices)][0])/2 +\
int(GiftCosts[len(minGiftPrices)][1]) < money:
    print len(minGiftPrices) + 1
else:
    print len(minGiftPrices)
'''
