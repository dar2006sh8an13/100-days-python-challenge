#Simple contact Book
contact = {}
def add_contact(name,phone):
    contact[name]=phone
def search_contact(name):
    return contact.get(name,"contact not found")
while True:
    print("\n1.add\n2.search\n3.viewall\n4.exit")
    choice = input("enter choice:")
    if choice == '1':
        n = input("name: ")
        p = input("phone: ")
        add_contact(n,p)
    elif choice=='2':
        n = input("seacher name :")
        print(search_contact(n))
    elif choice =='3':
        for n, p in contact.items():
            print(n,":",p)
    else:
        break