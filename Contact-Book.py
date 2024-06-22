class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self) :
        return f"Name : {self.name}\nPhone : {self.phone}\tEmail : {self.email}\n"

class ContactBook:
    def __init__(self) :
        self.contacts = []
        
    def add_contacts(self,contact) :
        self.contacts.append(contact)
    
    def delete_contact(self,name) :
        for contact in self.contacts :
            if contact.name.lower() == name.lower() :
                self.contacts.remove(contact)
                
    def search_contact(self,name) :
        for contact in self.contacts:
            if contact.name.lower() == name.lower() :
                return contact
        return None

    def display_contact(self):
        for contact in self.contacts :
            print(contact)
            

if __name__ == "__main__" :
    contact_book = ContactBook()

    while True :
        print('\nContact Book Menu : ')
        print('1. Add Contact')
        print('2. Delete Contact')
        print('3. Search Contact')
        print('4. Display all Contacts')
        print('5. Quit')
        
        choice = int(input("Enter your Choice: "))
        
        if choice == 1 : #Adding
            name = input("Enter the Name : ")
            phone = input("Enter the Phone Number : ")
            email = input("Enter the Email : ")
            contact = Contact(name,phone,email)
            contact_book.add_contacts(contact)
            print("Contact Saved Successfully")
            
        elif choice == 2 : #Deleting
            name = input("Enter the Name of contact to Delete :")
            contact_book.delete_contact(name)
            print("Contact Deleted")
            
        elif choice == 3 : #Searching
            name = input("Enter the Contact Name to Search : ")
            contact = contact_book.search_contact(name)
            if contact :
                print("Contact Fouond\n--------------")
                print(contact)
            else :
                print("Contact Not Found")
                
        elif choice == 4 : #Displaying
            print("All Contacts\n--------------")
            contact_book.display_contact()
            
        elif choice == 5:
            print("Quiting Contact Book")
            break
        else :
            print("Invalid Choice. PLease Select again...")
            
