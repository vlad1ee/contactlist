class ContactList(list):
    def __init__(self, list1):
        self.list1 = list1
        self.list2 = []

    def search_by_name(self, name):
        for i in self.list1:
            i.title()
        if name.title() in self.list1:
            self.list2.append(name.title())
            return self.list2
        else:
            return 'name isn\'t found'

all_contacts = ContactList(['Ivan', 'Masha', 'Jenya'])
print(all_contacts.list1)
print(all_contacts.search_by_name('masha'))