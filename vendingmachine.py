from typing import Dict, List

itemList = [{"name": "Mineral Wotah", "price": 3}, {"name": "Red Bull Gives You Wings", "price": 6}, {"name": "Milo Dinosaur Rawr", "price": 20}]

# get ready for rushed spaghetti codes
class Item:
    name: str
    price: int

    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    BUYING = "buying"
    CANCEL = "cancel"
    SUCCESS = "success"
    currentItem: Item | None = None
    items: Dict[int, Item] = {}
    notes: List[int] = []
    status: str = BUYING
    
    def __init__(self) -> None:
        # initialize items
        for i, v in enumerate(itemList):
            self.items[i+1] = Item(v['name'], v['price'])
    # assume notes are 1,5,10
    
    def sumNotes(self):
        return sum(self.notes)
    
    def askNotes(self):
        if (not self.hasCurrentItem() and self.sumNotes() <= self.currentItem.price):
            return
        while self.sumNotes() <= self.currentItem.price:
            self.printDiv()
            print(f"Sum Inserted: {self.sumNotes()} \n")
            noteInput = self.askInput("Insert Notes (1,5,10), 0 to cancel:")
            if (noteInput == "" or noteInput == None):
                continue
            note = int(noteInput)
            if note == 0:
                # return notes
                self.setStatus(self.CANCEL)
                break
            elif note not in [1,5,10]:
                self.displayInvalid()
                print(f'rejecting note: {note}')
            else:
                self.insertNote(note)
            self.setStatus(self.SUCCESS)
    
    def setStatus(self, status: str):
        self.status = status
    
    def displayStatus(self):
        self.printDiv()
        if (self.status == self.CANCEL):
            print("Cancelling purchase!")
        else:
            print(f"Dispensing Item {self.currentItem.name}")

    def printDiv(self):
        print("================")
            

    def insertNote(self, num: int):
        self.notes.append(num)

    def returnNotes(self):
        self.printDiv()
        sumToReturn = self.sumNotes() - self.currentItem.price
        print(f'Total inserted: {self.sumNotes()}')
        print(f'Total balance: {sumToReturn}')
        while sumToReturn > 0:
            if (sumToReturn >= 10):
                print(f'Returning note: 10')
                sumToReturn -= 10
            elif (sumToReturn >= 5):
                print(f'Returning note: 5')
                sumToReturn -= 5
            else:
                print(f'Returning note: 1')
                sumToReturn -= 1
            # check if already empty
        self.printDiv()

    def selectItem(self, id: int):
        try:
            self.currentItem = self.items[id]
        except:
            # throw error?
            pass
        
    
    def hasCurrentItem(self) -> bool:
        if (self.currentItem != None):
            return True
        return False
    
    def displayItems(self):
        for key in self.items:
            print(f'{key}: {self.items[key].name} - RM{self.items[key].price}')
        print(f'0: Exit')
        self.printDiv()

    def displayPrice(self):
        if not self.hasCurrentItem():
            return
        price = self.currentItem.price
        print(f"Price is : {price}")
        
    def displayHello(self):
        print("===== Hello, welcome to snek vending machine =====")
    
    def checkItem(self, itemId) -> bool:
        if self.items.get(itemId) != None:
            return True
        return False
    
    def displayInvalid(self):
        print("Invalid option selected")
        
    def reset(self):
        self.status = self.BUYING
        self.currentItem = None
        self.notes = []
        
    def askInput(self, inputText: str) -> str:
        return input(inputText)
        



