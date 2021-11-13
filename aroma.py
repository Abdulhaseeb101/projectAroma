import json

# Dictionary for storing prices for all the ingredients
ingredientsDict = {}

# List for storing ingredients entered by the user
ingredientsAndQuantDict = dict()

# Loading price values from the json file
with open('rawPrice.json') as f:
    ingredientsDict = json.load(f)

def cvtPPKGToPPG(dict):
    '''
    Convert prices of items from price per KG to 
    price per gram 
    '''
    dictKeys = dict.keys()

    for key in dictKeys:
        dict[key] = dict[key] / 1000

    return dict


def getIngredientsAndQuantity():
    '''
    Get ingredients and quantity from user for calculating 
    the total price of the recipe
    '''
    lists = dict()

    lists['itemLst'] = []
    lists['quantLst'] = []


    print('Enter ingredients followed by quantity in grams or enter "end"')
    while True:
        item = input('-------------------------------\n')
        
        if item == 'end':
            break

        quantity = float(input())
        print('------------------------------\n')
        
        lists['itemLst'].append(item)
        lists['quantLst'].append(quantity)

    return lists


def calculatePrice(iQDict, priceDict):
    '''
    Use iQDict and priceDict to calculate the price of the whole
    recipe
    '''
    totPrice = 0.0
    
    for item, quant in zip(iQDict['itemLst'], iQDict['quantLst']):
        itemPriceG = priceDict[item]
        totPrice = totPrice + (float(quant) * itemPriceG) 

    return totPrice



# Convert price per kg to price per gram and store
ingredientsDict = cvtPPKGToPPG(ingredientsDict)

# Store ingredients entered by the user
ingredientsAndQuantDict = getIngredientsAndQuantity()

# Calculate price of the recipe
totalPrice = calculatePrice(ingredientsAndQuantDict, ingredientsDict)

print("Production cost of recipe " + totalPrice)
