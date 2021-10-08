#Initializing the linked list class
class linkedlist:
    def __init__(self, node, nextnode = 'null'):
        self.node = node
        self.nextnode = nextnode

#Defining the data to be stored in the array.
first = linkedlist('January')
second = linkedlist('February')
third = linkedlist('March')
fourth = linkedlist('April')
fifth = linkedlist('May')
sixth = linkedlist('June')
seventh = linkedlist('July')
eigth = linkedlist('August')
ninth = linkedlist('September')
tenth = linkedlist('October')
eleventh = linkedlist('November')
twelfth = linkedlist('December')

#first data points to the location of the next data
first.nextnode = second
second.nextnode = third
third.nextnode = fourth
fourth.nextnode = fifth
fifth.nextnode = sixth
sixth.nextnode = seventh
seventh.nextnode = eigth
eigth.nextnode = ninth
ninth.nextnode = tenth
tenth.nextnode = eleventh
eleventh.nextnode = twelfth
twelfth.nextnode = 'null'

firstmonth = first
while 1:
    print(firstmonth.node, '->', end=" ")
    if firstmonth.nextnode == 'null':
        print('No new data')
        break
    firstmonth = firstmonth.nextnode