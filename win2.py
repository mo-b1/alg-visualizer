import tkinter
import tkinter as tk
from settings import*
from _thread import start_new_thread
    # Python program to create a table

def show_matrix(matrix):
    root = tk.Tk()
    root.title("Matrix")

    def printt(add, entry,pos):
        before= entry.get()
        print(before)
        add.set("".join([num for num in entry.get() if num.isdigit()]))
        after = add.get()

        if before.isdigit() and after.isdigit():
            if int(before) != int(after):
                print(f"before: {before}")
                print(f"after: {after}")
    contents = {}

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            contents[i,j] = tk.StringVar()
            e = tk.Entry(root, width=2, fg="black",font=('Comic sans MS', 16, 'bold'), textvariable=contents[i,j])
            e.grid(row=i,column=j)
            e.insert(0, f"{matrix[i][j]}")

            contents[i,j].trace_add("write",lambda name, index,mode, i=i, j=j, entry=e: printt(contents[i,j], entry, (i,j)))


            '''label = tk.Label(root,text=f"{matrix[i][j]}")
            label.place(x=j*50,y=i*50)
            
    '''

    root.mainloop()

#show_matrix([[1,2],[2,4]])