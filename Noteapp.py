import os 

def display():
    print(" Welcome to Note Taking App")
    print(" 1 . View Notes")
    print(' 2 . Create Notes')
    print(' 3 . Delete Notes')
    print(' 4 . Exit')

def createNotes():
    notes_title = input(' Enter the Note title : ')
    notes_content = input(' Enter the Note Content : ')

    notes_dir = "notes"
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)
    notes_path = os.path.join(notes_dir,(f'{notes_title}.txt'))
    with open(notes_path,'a') as file:
        file.write(f'{notes_content}\n')
    print('notes added successfully')

def viewNotes():
    notes_dir = "notes"
    if not os.path.exists(notes_dir):
        print("Notes Not available")
        return
    for i in os.listdir(notes_dir):
        with open(os.path.join(notes_dir,i),'r') as file:
            content = file.read()
            print(f'{i[:-4]}:{content}')

def DeleteNotes():
    notes_title = input("Enter the note you want to delete : ")
    notes_dir = "notes"
    notes_path = os.path.join(notes_dir,f"{notes_title}.txt")

    if os.path.exists(notes_path):
        os.remove(notes_path)
        print(f"Note {notes_title} was removed successfully ")

def main():
    
    while True :
         display()
         val = input("Enter a number between 1 to 4 :")
         if val == '1':
             viewNotes()
         elif val == '2':
             createNotes()
         elif val == '3':
             DeleteNotes()
         elif val == '4':
             print("Exiting the Notes App Thank you :) ")
             break
         else:
             print("Please Enter valid Number")


if __name__ == "__main__" :
 main()
         
