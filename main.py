from vendingmachine import VendingMachine

# def countDivisible(x, y, d):
#     count = 0
#     for i in range(x,y):
#         if (i % d == 0):
#             count += 1
#     return count


# def reverseStr(s):
#     return s[::-1]

# def solution(x: str):
#     while True:
#         original = x
#         x = x.replace("XX", "")
#         x = x.replace("YY", "")
#         x = x.replace("ZZ", "")
        
#         if (x == original):
#             break
        
#     return x


# ehh.. main loop
if __name__ == "__main__":
    # create new instance of vending machine
    v = VendingMachine()
    while True:
        # display item list for selection @_@
        v.displayHello()
        # ask for user input on item ?_?
        v.displayItems()
        itemIdInput = v.askInput("Please Select Item: ")
        
        if (itemIdInput == "0"):
            print('goodbye!')
            break 
        else:
            itemId = int(itemIdInput)
            # do vending machine stuff :o
            # send the item id to vending machine, display price :>
            if not v.checkItem(itemId):
                v.displayInvalid()
                continue
            v.selectItem(itemId)
            v.displayPrice()
            # ask user to input notes (1,5,10 only) $_$
            v.askNotes()
            # check status after notes flow is done <_<
            v.displayStatus()
            # return $$$
            v.returnNotes()
            v.reset()
            continue
        