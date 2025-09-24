from contact import Contact


def get_menu_choice():
    print('Rolodex Menu:\n1. Display Contacts\n2. Add Contact\n3. Search Contacts\n4. Modify Contact\n5. Save and Quit')
    while True:
        try:
            choice=int(input('> '))
            if choice in range(1,6):
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print('Invalid input - should be an integer.')


#read contacts from the addresses.txt file
def read_file():
    contacts=[]
    with open('addresses.txt','r') as f:
        lines=f.readlines()                     #lines is a list and its elements are lines in the txt file.
        for line in lines:
            new_line=line.strip().split(',')    #new_line is a list [fn, ln, ph, addr, city, zip]
            if len(new_line)!=6:                #bypass the lines don't have enough 6 cols
                continue
            contact=Contact(new_line[0], new_line[1], new_line[2], new_line[3], new_line[4], new_line[5])
            contacts.append(contact)

    contacts.sort()     #will use __lt__() to sort by ln
    return contacts



#save contacts to the file 
def write_file(contacts):           # 'contacts' parameter here is the sorted contacts list created by the read_file() function, it can be modified before writing and save back to the the txt file. 
    with open('addresses.txt','w') as f:
        for contact in contacts:
            f.write(repr(contact)+'\n')


#modify contact
def modify_contact(contact):
    print(str(contact))
    print('\nModify Menu: ')

    menu={1:('fn','First name', 'Enter first name: '), 
          2:('ln','Last name', 'Enter last name: '), 
          3:('ph','Phone', 'Enter phone #: '), 
          4:('addr','Address', 'Enter address: '), 
          5:('city','City', 'Enter city: '),
          6:('zipcode','Zip', 'Enter zip: ')}
    
    for num in menu:
        print(f"{num}. {menu[num][1]}")
    print('7. Save')

    while True:
        try:
            pick=int(input('> '))
            if pick==7:
                break
            elif pick in menu:
                attr, _ , prompt = menu[pick]
                setattr(contact, attr, input(prompt))
            else:
                print('Invalid input - should be 1-7.')
        except ValueError:
            print('Invalid input - should be an integer.')
        

def main():
    contacts=read_file() 
    while True:
        choice=get_menu_choice()
        if choice==1:
             print(f"Number of contacts: {len(contacts)}")
             for i, contact in enumerate(contacts, start=1):
                 print(f"{i}. {str(contact)}\n")

        elif choice==2:
            print('Enter new contact:')
            try:
                fn=input('First name: ')
                ln=input('Last name: ')
                ph=input('Phone #: ')
                addr=input('Address: ')
                city=input('City: ')
                zipcode=input('Zip: ')
            
                contact=Contact(fn,ln,ph,addr,city,zipcode)
                contacts.append(contact)

                write_file(contacts)
            except Exception as e:
                print(f"Error found: {e}")

        elif choice==3:
            print("Search:")
            search_menu={1:('Search by last name','Enter last name: '), 2:('Search by zip','Enter zip: ')}
            for num in search_menu:
                print(f"{num}. {search_menu[num][0]}")
            
            while True:
                try:
                    pick=int(input('> '))
                    if pick in search_menu:
                        search=input(f"{search_menu[pick][1]}").strip()

                        results=[]
                        if pick==1:   #search by last name
                            for contact in contacts:
                                if contact.ln.strip().lower()==search.lower():
                                    results.append(contact)
                        elif pick==2: #search by zip
                            for contact in contacts:
                                if contact.zipcode.strip()==search:
                                    results.append(contact)
                        
                        if results:
                            results.sort()
                            for result in results:
                                print(f"\n{result}\n")
                        else:
                            print('Contact not found.')
                        break
                    else:
                        print('Please choose 1-2.')
                except ValueError:
                    print("Invalid input - should be an integer")

        elif choice==4:
            try:
                fn=input('Enter first name: ').strip()
                ln=input('Enter last name: ').strip()

                found=None
                for contact in contacts:
                    if contact.fn.strip().lower()==fn.lower() and contact.ln.strip().lower()==ln.lower():
                        found=contact
                        break
                
                if found:
                    modify_contact(found)
                    contacts.sort()
                    try:
                        write_file(contacts)
                    except Exception as e:
                        print('f"Error during saving: {e}')
                else:
                    print('Contact not found')
            except Exception as e:
                print(f"Error during modification: {e}")

        elif choice==5:
            try:
                write_file(contacts)
            except Exception as e:
                print(f"Error during saving: {e}")
            break

        else:
            print('Please choose 1-5')


if __name__=='__main__':
    main()

   






                    
                            



                            

                        


            


   



        

    



        


    



    
    


    
    


    



    


    
