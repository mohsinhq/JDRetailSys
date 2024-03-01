# Implementing the list object
class Node:
    def __init__(self, d, n):
        self.data = d
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        if self.head == None: 
            return "empty"
        st = "-"
        ptr = self.head
        while ptr != None:
            
            st += "-> "+str(ptr.data)+" "
            ptr = ptr.next
        return st+"|"
        
    def search(self, d):
        i = 0
        ptr = self.head
        while ptr != None:
            if ptr.data == d:
                return i
            ptr = ptr.next
            i += 1
        return -1
    
    def append(self, d):
        if self.head == None:      
            self.head = Node(d,None) 
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(d,None)
        self.length += 1

    def insert(self, i, d):
        if self.head == None or i == 0:
            self.head = Node(d,self.head)
        else:
            ptr = self.head
            while i>1 and ptr.next != None:
                ptr = ptr.next
                i -= 1
            ptr.next = Node(d,ptr.next)
        self.length += 1

    def remove(self, i): # removes i-th element and returns it
        if self.head == None:
            return None
        if i == 0:
            val = self.head.data
            self.head = self.head.next
            self.length -= 1
            return val
        ptr = self.head
        while ptr.next != None:
            if i == 1:
                val = ptr.next.data
                ptr.next = ptr.next.next
                self.length -= 1
                return val                
            ptr = ptr.next
            i -= 1
            
    def removeVal(self, d):
        if self.head == None:
            return -1
        if self.head.data == d:
            self.head = self.head.next
            self.length -= 1
            return 0
        else:
            i = 0
            ptr = self.head	
            while ptr.next != None:
                if ptr.next.data == d:
                    ptr.next = ptr.next.next
                    self.length -= 1
                    return i+1
                ptr = ptr.next
                i += 1
        return -1
    
    def get(self, i):
        ptr = self.head
        while i > 0:
            ptr = ptr.next
            i -= 1
        return ptr.data
    
    def set(self, i, d):
        ptr = self.head
        while i > 0:
            ptr = ptr.next
            i -= 1
        ptr.data = d

# The shoe object, holding the information of each shoe
# Mistake made, shelves contain shoes, shoes don't contain shelves
class shoe:
    def __init__(self, name, UPC, shelf):
        self.name = name
        self.UPC = UPC
        self.shelf = shelf

# Class for gap request, 
class gapReq:
	def __init__(self, shoe):
		self.name = shoe.name
		self.UPC = shoe.UPC
		self.shelf = shoe.shelf
		self.status = "PENDING"
		
	def pick(self):
        self.status = "PICKED"
	
	def oos(self):
        self.status = "DENIED"
	
	def showDetails(self):
        print(self.name/n)
        print(self.status/n)
        print(self.shelf/n)
     
class db:
    def __init__(self):
        self.shoedb = LinkedList()
        self.shoedb.append(shoe("DUNK LOW WHT/BLK", 194502876055, "170401l"))
        self.shoedb.append(shoe("AJ1 LOW BLK/WHT/RED", 194502876062, "90404p"))
        self.shoedb.append(shoe("SAMBA WHT/BLK", 179078484895, "140101j"))

    def searchByShelf(self,shelf):
        i = 0
        ptr = self.shoedb.head
        while ptr != None:
            if ptr.data.shelf == shelf:
                return ptr
            ptr = ptr.next
            i += 1
        return -1

    def searchByBarcode(self,bc):
        i = 0
        ptr = self.shoedb.head
        while ptr != None:
            if ptr.data.UPC == bc:
                return ptr
            ptr = ptr.next
            i += 1
        return -1
    
class display:
    def __init__(self):
        self.db = db()
        self.gapList = LinkedList()
        print("User: 179029239420015 Pr: 1")
        print("1. Footwear Fill Up") 
        print("2. Gap Requests")
        print("3. Set Printer")
        self.option1 = input("Select option: ")
        while (self.option1 < 3 and self.option1 > 0):
            self.option1 = input("Select option: ")
            if (self.option1 == 1):
                self.FillUp()
            elif (self.option1 == 2):
                self.viewGaps()

    def addGap(self, shoebc):
        self.gapList.append(self.db.searchByBarcode(shoebc))
        
    def FillUp(self):
        self.shoebc = input("Enter barcode: ")
        while (self.db.searchByBarcode(self.shoebc) == -1):
            print("INVALID BARCODE"/n)
            self.shoebc = input("Enter barcode: ")
        addGap(self.shoebc)
        print("Label Printed")

    def viewGapsOnShelf(self, s):
        print("Orders on shelf:"/n)
        for i in range(1, self.gapList.length):
            print(i, ". ")
            if (self.gapList.get(i).shelf == s):
                self.gapList.get(i).showDetails()
                
            
        
    def viewGaps(self):
        for i in range(1, self.gapList.length):
            print(i, ". ")
            self.gapList.get(i).showDetails()
        self.shoeshelfinput = input("Scan Shelf:")
        while (self.db.searchByShelf(self.shoeshelfinput) == -1):
            print("NO ORDERS ON SHELF")
            self.shoeshelfinput = input("Scan Shelf: ")
        viewGapsOnShelf(self.shoeshelfinput)
        option2 = input("Enter line to change status:")