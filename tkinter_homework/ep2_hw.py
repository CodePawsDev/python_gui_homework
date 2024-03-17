from tkinter import *

# main screen
root = Tk()
root.title('โปรแกรมหารกัน')
root.geometry('350x350')

title_label = Label(root, text='โปรแกรมหารกัน', font=('Angsana New', 30, 'bold'))
title_label.pack()

total_price_label = Label(root, text='ราคาอาหารทั้งหมด (บาท)', font=('Angsana New', 20))
total_price_label.pack()

v_total_price = StringVar()
total_price_entry = Entry(root, textvariable=v_total_price, font=('Angsana New', 18))
total_price_entry.pack()

total_person_label = Label(root, text='จำนวนคน', font=('Angsana New', 20))
total_person_label.pack()

v_total_person = StringVar()
total_person_entry = Entry(root, textvariable=v_total_person, font=('Angsana New', 18))
total_person_entry.pack()

def calculate():
    total_price = float(v_total_price.get())
    total_person = int(v_total_person.get())
    price_per_person = total_price / total_person
    return price_per_person

def close_result_window(result_window):
    result_window.destroy()
    v_total_price.set('')
    v_total_person.set('')
    total_price_entry.focus_set()    

def open_result_window(price_per_person):
    msg = 'ต้องหารคนละ {:,.2f} บาท'.format(price_per_person)

    result_window = Tk()
    result_window.title('สรุปรายการ')
    result_window.geometry('250x100')

    result_label = Label(result_window, text=msg, font=('Angsana New', 20))
    result_label.pack()
    
    close_btn = Button(result_window, text='Close', command=lambda: close_result_window(result_window), bg='red', fg='white')
    close_btn.pack()

def calculate_and_show_result():
    price_per_person = calculate()
    open_result_window(price_per_person)

save_btn = Button(root, text='Calculate', command=calculate_and_show_result, bg='green', fg='white')
save_btn.pack(pady=15)

root.mainloop()
