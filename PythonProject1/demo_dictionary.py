from tkinter import Tk, Entry, Button, Label, StringVar

from dictionary import yoruba_dictionary

window = Tk()
window.geometry("600x250")
window.title("Yoruba Dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

def search(word):
    if word in yoruba_dictionary:
        result.set(yoruba_dictionary[word])
        print(yoruba_dictionary[word])
    else:
        result.set("Not Found")
        print("Not Found")

search_btn = Button(window, text="Search", command=lambda: search(entry_text.get()))
search_btn.pack()

window.mainloop()