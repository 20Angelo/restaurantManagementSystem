import sqlite3
from tkinter import *
from tkinter import filedialog, messagebox
import random
import time
import requests
#line 771 change menu

#function that resets all the input of the user in GUI
def reset():
    textReceipt.delete(1.0, END)
    e_chicken.set('0')
    e_pancake.set('0')
    e_ribs.set('0')
    e_noodles.set('0')
    e_ravioli.set('0')
    e_paella.set('0')
    e_shrimp.set('0')
    e_sushi.set('0')
    e_lobster.set('0')

    e_frenchfries.set('0')
    e_guacamole.set('0')
    e_springrolls.set('0')
    e_nachos.set('0')
    e_quesadillas.set('0')
    e_icedcoffee.set('0')
    e_milkshakes.set('0')
    e_margaritas.set('0')
    e_juices.set('0')

    e_cheesecake.set('0')
    e_tiramisu.set('0')
    e_blackforest.set('0')
    e_gelato.set('0')
    e_applepie.set('0')
    e_brownies.set('0')
    e_mousse.set('0')
    e_churros.set('0')
    e_tart.set('0')

    textchicken.config(state=DISABLED)
    textpancake.config(state=DISABLED)
    textribs.config(state=DISABLED)
    textnoodles.config(state=DISABLED)
    textravioli.config(state=DISABLED)
    textpaella.config(state=DISABLED)
    textshrimp.config(state=DISABLED)
    textsushi.config(state=DISABLED)
    textlobster.config(state=DISABLED)

    textfrenchfries.config(state=DISABLED)
    textguacamole.config(state=DISABLED)
    textquesadillas.config(state=DISABLED)
    texticedcoffee.config(state=DISABLED)
    textnachos.config(state=DISABLED)
    textmargaritas.config(state=DISABLED)
    textmilkshakes.config(state=DISABLED)
    textspringrolls.config(state=DISABLED)
    textjuices.config(state=DISABLED)

    textcheesecake.config(state=DISABLED)
    texttiramisu.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
    textgelato.config(state=DISABLED)
    textapplepie.config(state=DISABLED)
    textbrownies.config(state=DISABLED)
    textmousse.config(state=DISABLED)
    textchurros.config(state=DISABLED)
    texttart.config(state=DISABLED)
#variables for food menu
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
#costs
    costofsninksvar.set('')
    costofmainvar.set('')
    costofsweetsvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
#function that sends the billnumber, date, subtotal costs, and orders to the database
def send():
    menu = []
    quantity = []
    o1 = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x1, y, z, a1]
    items = [item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14,
             item15, item16, item17, item18, item19, item20, item21, item22, item23, item24, item25, item26, item27]
    for b3 in items:
        if b3 == 0:
            pass
        else:
            quantity.append(b3)
    for b2 in o1:
        if b2 == "":
            pass
        else:
            menu.append(b2)
    orders = dict(zip(menu, quantity))
    orders = str(orders)
    connect = sqlite3.connect('customer.db')
    table_query = '''CREATE TABLE IF NOT EXISTS receipt(billnumber TEXT,date TEXT, subtotalcost INTEGER,orders TEXT)'''
    connect.execute(table_query)
    insert_query = '''INSERT INTO receipt( billnumber,date,subtotalcost,orders)VALUES(?,?,?,?)'''
    insert_tuple = (billnumber, date, subtotalvar.get(), orders)
    cursor = connect.cursor()
    cursor.execute(insert_query, insert_tuple)
    connect.commit()
    connect.close()
#function that save file
def save():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:
            bill_data = textReceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information', 'Your Bill Is Succesfully Saved')
#function that shows the receipt order of the user
def receipt():
    global billnumber, date
    if costofmainvar.get() != '' or costofsweetsvar.get() != '' or costofsninksvar.get() != '':
        textReceipt.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')
        textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
        textReceipt.insert(END, '***************************************************************\n')
        textReceipt.insert(END, 'Items:\t\t Cost Of Items(pesos)\n')
        textReceipt.insert(END, '***************************************************************\n')
        if e_chicken.get() != '0':
            global a
            a = "Chicken"
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 180}\n\n')
        else:
            a = ""
        if e_pancake.get() != '0':
            global b
            b = "Pancake"
            textReceipt.insert(END, f'Pancake:\t\t\t{int(e_pancake.get()) * 120}\n\n')
        else:
            b = ""
        if e_ribs.get() != '0':
            global c
            c = "Ribs"
            textReceipt.insert(END, f'Ribs:\t\t\t{int(e_ribs.get()) * 250}\n\n')
        else:
            c = ""
        if e_paella.get() != '0':
            global d
            d = "Paella"
            textReceipt.insert(END, f'Paella:\t\t\t{int(e_paella.get()) * 300}\n\n')
        else:
            d = ""
        if e_noodles.get() != '0':
            global e
            e = "Noodles"
            textReceipt.insert(END, f'Noodles:\t\t\t{int(e_noodles.get()) * 150}\n\n')
        else:
            e = ""
        if e_sushi.get() != '0':
            global f
            f = "Sushi"
            textReceipt.insert(END, f'Sushi:\t\t\t{int(e_sushi.get()) * 220}\n\n')
        else:
            f = ""
        if e_ravioli.get() != '0':
            global g
            g = "Ravioli"
            textReceipt.insert(END, f'Ravioli:\t\t\t{int(e_ravioli.get()) * 200}\n\n')
        else:
            g = ""
        if e_lobster.get() != '0':
            global h
            h = "Chicken"
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_lobster.get()) * 500}\n\n')
        else:
            h = ""
        if e_shrimp.get() != '0':
            global i
            i = "Shrimp"
            textReceipt.insert(END, f'Shrimp:\t\t\t{int(e_shrimp.get()) * 280}\n\n')
        else:
            i = ""
        if e_frenchfries.get() != '0':
            global j
            j = "French Fries"
            textReceipt.insert(END, f'French Fries:\t\t\t{int(e_frenchfries.get()) * 80}\n\n')
        else:
            j = ""
        if e_guacamole.get() != '0':
            global k
            k = "Guacamole"
            textReceipt.insert(END, f'Guacamole:\t\t\t{int(e_guacamole.get()) * 90}\n\n')
        else:
            k = ""
        if e_springrolls.get() != '0':
            global l
            l = "Spring Rolls"
            textReceipt.insert(END, f'Spring Rolls:\t\t\t{int(e_springrolls.get()) * 100}\n\n')
        else:
            l = ""
        if e_nachos.get() != '0':
            global m
            m = "Nachos"
            textReceipt.insert(END, f'Nachos:\t\t\t{int(e_nachos.get()) * 120}\n\n')
        else:
            m = ""
        if e_quesadillas.get() != '0':
            global n
            n = "Quesadillas"
            textReceipt.insert(END, f'Quesadillas:\t\t\t{int(e_quesadillas.get()) * 150}\n\n')
        else:
            n = ""
        if e_icedcoffee.get() != '0':
            global o
            o = "Iced Coffee"
            textReceipt.insert(END, f'Iced Coffee:\t\t\t{int(e_icedcoffee.get()) * 110}\n\n')
        else:
            o = ""
        if e_milkshakes.get() != '0':
            global p
            p = "Milkshakes"
            textReceipt.insert(END, f'Milkshakes:\t\t\t{int(e_milkshakes.get()) * 130}\n\n')
        else:
            p = ""
        if e_margaritas.get() != '0':
            global q
            q = "Margaritas"
            textReceipt.insert(END, f'Margaritas:\t\t\t{int(e_margaritas.get()) * 180}\n\n')
        else:
            q = ""
        if e_juices.get() != '0':
            global r
            r = "Juices"
            textReceipt.insert(END, f'Juices:\t\t\t{int(e_juices.get()) * 70}\n\n')
        else:
            r = ""
        if e_cheesecake.get() != '0':
            global s
            s = "Cheesecake"
            textReceipt.insert(END, f'Cheesecake:\t\t\t{int(e_cheesecake.get()) * 150}\n\n')
        else:
            s = ""
        if e_tiramisu.get() != '0':
            global t
            t = "Tiramisu"
            textReceipt.insert(END, f'Tiramisu:\t\t\t{int(e_tiramisu.get()) * 180}\n\n')
        else:
            t = ""
        if e_blackforest.get() != '0':
            global u
            u = "Black Forest"
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 160}\n\n')
        else:
            u = ""
        if e_applepie.get() != '0':
            global v
            v = "Apple Pie"
            textReceipt.insert(END, f'Apple Pie:\t\t\t{int(e_applepie.get()) * 140}\n\n')
        else:
            v = ""
        if e_brownies.get() != '0':
            global w
            w = "Brownies"
            textReceipt.insert(END, f'Brownie:\t\t\t{int(e_brownies.get()) * 130}\n\n')
        else:
            w = ""
        if e_mousse.get() != '0':
            global x1
            x1 = "Mousse"
            textReceipt.insert(END, f'Mousse:\t\t\t{int(e_mousse.get()) * 110}\n\n')
        else:
            x1 = ""
        if e_churros.get() != '0':
            global y
            y = "Churros"
            textReceipt.insert(END, f'Churros:\t\t\t{int(e_churros.get()) * 100}\n\n')
        else:
            y = ""
        if e_tart.get() != '0':
            global z
            z = "Tart"
            textReceipt.insert(END, f'Tart:\t\t\t{int(e_tart.get()) * 130}\n\n')
        else:
            z = ""
        if e_gelato.get() != '0':
            global a1
            a1 = "Gelato"
            textReceipt.insert(END, f'Gelato:\t\t\t{int(e_gelato.get()) * 120}\n\n')
        else:
            a1 = ""
#food costs in the receipt
        textReceipt.insert(END, '***************************************************************\n')
        if costofmainvar.get() != '0 pesos':
            textReceipt.insert(END, f'Cost Of Main:\t\t\t{priceofMain} pesos\n\n')
        if costofsninksvar.get() != '0 pesos':
            textReceipt.insert(END, f'Cost Of Sninks:\t\t\t{priceofSninks} pesos\n\n')
        if costofsweetsvar.get() != '0 pesos':
            textReceipt.insert(END, f'Cost Of Sweets:\t\t\t{priceofSweets} pesos\n\n')

        textReceipt.insert(END, f'Sub Total:\t\t\t{subtotalofItems} pesos\n\n')
        textReceipt.insert(END, f'Service Tax:\t\t\t{50} pesos\n\n')
        textReceipt.insert(END, f'Total Cost:\t\t\t{subtotalofItems + 50} pesos\n\n')
        textReceipt.insert(END, '***************************************************************\n')
#if the user does not select any items
    else:
        messagebox.showerror('Error', 'No Item Is selected')
#function to get the total cost of the ordered food/s
def totalcost():
    global priceofMain, priceofSninks, priceofSweets, subtotalofItems, item1, item2, item3, item4, item5, item6, item7,\
        item8, item9, item10, item11, item12, item13, item14, item15, item16, item17, item18, item19, item20, item21, \
        item22, item23, item24, item25, item26, item27
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
            var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
            var26.get() != 0 or var27.get() != 0:

        item1 = int(e_chicken.get())
        item2 = int(e_pancake.get())
        item3 = int(e_ribs.get())
        item4 = int(e_noodles.get())
        item5 = int(e_ravioli.get())
        item6 = int(e_paella.get())
        item7 = int(e_shrimp.get())
        item8 = int(e_sushi.get())
        item9 = int(e_lobster.get())

        item10 = int(e_frenchfries.get())
        item11 = int(e_guacamole.get())
        item12 = int(e_springrolls.get())
        item13 = int(e_nachos.get())
        item14 = int(e_quesadillas.get())
        item15 = int(e_icedcoffee.get())
        item16 = int(e_milkshakes.get())
        item17 = int(e_margaritas.get())
        item18 = int(e_juices.get())

        item19 = int(e_cheesecake.get())
        item20 = int(e_tiramisu.get())
        item21 = int(e_blackforest.get())
        item22 = int(e_gelato.get())
        item23 = int(e_applepie.get())
        item24 = int(e_brownies.get())
        item25 = int(e_mousse.get())
        item26 = int(e_churros.get())
        item27 = int(e_tart.get())
#setting the prices of the foods in the menu
        priceofMain = (item1 * 180) + (item2 * 120) + (item3 * 250) + (item4 * 150) + (item5 * 200) + (item6 * 300) + \
                      (item7 * 280) + (item8 * 220) + (item9 * 500)
        priceofSninks = (item10 * 80) + (item11 * 90) + (item12 * 100) + (item13 * 120) + (item14 * 150) \
                        + (item15 * 110)+ (item16 * 130) + (item17 * 180) + (item18 * 70)
        priceofSweets = (item19 * 150) + (item20 * 180) + (item21 * 160) + (item22 * 120) + (item23 * 140)\
                        + (item24 * 130)+ (item25 * 110) + (item26 * 100) + (item27 * 130)
#if the total button is clicked, the overall cost will be showed
        costofmainvar.set(str(priceofMain) + ' pesos')
        costofsninksvar.set(str(priceofSninks) + ' pesos')
        costofsweetsvar.set(str(priceofSweets) + ' pesos')

        subtotalofItems = priceofMain + priceofSninks + priceofSweets
        subtotalvar.set(str(subtotalofItems) + ' pesos')

        servicetaxvar.set('50 pesos')

        tottalcost = subtotalofItems + 50
        totalcostvar.set(str(tottalcost) + ' pesos')
    else:
        messagebox.showerror('Error', 'No item is selected.')
#functions for the food menu; main, sninks, and sweets
def chicken():
    if var1.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0, END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def pancake():
    if var2.get() == 1:
        textpancake.config(state=NORMAL)
        textpancake.delete(0, END)
        textpancake.focus()
    else:
        textpancake.config(state=DISABLED)
        e_pancake.set('0')

def ribs():
    if var3.get() == 1:
        textribs.config(state=NORMAL)
        textribs.delete(0, END)
        textribs.focus()
    else:
        textribs.config(state=DISABLED)
        e_ribs.set('0')

def noodles():
    if var4.get() == 1:
        textnoodles.config(state=NORMAL)
        textnoodles.focus()
        textnoodles.delete(0, END)
    elif var4.get() == 0:
        textnoodles.config(state=DISABLED)
        e_noodles.set('0')

def Ravioli():
    if var5.get() == 1:
        textravioli.config(state=NORMAL)
        textravioli.focus()
        textravioli.delete(0, END)
    elif var5.get() == 0:
        textravioli.config(state=DISABLED)
        e_ravioli.set('0')

def paella():
    if var6.get() == 1:
        textpaella.config(state=NORMAL)
        textpaella.focus()
        textpaella.delete(0, END)
    elif var6.get() == 0:
        textpaella.config(state=DISABLED)
        e_paella.set('0')

def shrimp():
    if var7.get() == 1:
        textshrimp.config(state=NORMAL)
        textshrimp.focus()
        textshrimp.delete(0, END)
    elif var7.get() == 0:
        textshrimp.config(state=DISABLED)
        e_shrimp.set('0')

def sushi():
    if var8.get() == 1:
        textsushi.config(state=NORMAL)
        textsushi.focus()
        textsushi.delete(0, END)
    elif var8.get() == 0:
        textsushi.config(state=DISABLED)
        e_sushi.set('0')

def lobster():
    if var9.get() == 1:
        textlobster.config(state=NORMAL)
        textlobster.focus()
        textlobster.delete(0, END)
    elif var9.get() == 0:
        textlobster.config(state=DISABLED)
        e_lobster.set('0')

def french_fries():
    if var10.get() == 1:
        textfrenchfries.config(state=NORMAL)
        textfrenchfries.focus()
        textfrenchfries.delete(0, END)
    elif var10.get() == 0:
        textfrenchfries.config(state=DISABLED)
        e_frenchfries.set('0')

def guacamole():
    if var11.get() == 1:
        textguacamole.config(state=NORMAL)
        textguacamole.focus()
        textguacamole.delete(0, END)
    elif var11.get() == 0:
        textguacamole.config(state=DISABLED)
        e_guacamole.set('0')

def spring_rolls():
    if var12.get() == 1:
        textspringrolls.config(state=NORMAL)
        textspringrolls.focus()
        textspringrolls.delete(0, END)
    elif var12.get() == 0:
        textspringrolls.config(state=DISABLED)
        e_springrolls.set('0')

def nachos():
    if var13.get() == 1:
        textnachos.config(state=NORMAL)
        textnachos.focus()
        textnachos.delete(0, END)
    elif var13.get() == 0:
        textnachos.config(state=DISABLED)
        e_nachos.set('0')

def quesadillas():
    if var14.get() == 1:
        textquesadillas.config(state=NORMAL)
        textquesadillas.focus()
        textquesadillas.delete(0, END)
    elif var14.get() == 0:
        textquesadillas.config(state=DISABLED)
        e_quesadillas.set('0')

def iced_coffee():
    if var15.get() == 1:
        texticedcoffee.config(state=NORMAL)
        texticedcoffee.focus()
        texticedcoffee.delete(0, END)
    elif var15.get() == 0:
        texticedcoffee.config(state=DISABLED)
        e_icedcoffee.set('0')

def milkshakes():
    if var16.get() == 1:
        textmilkshakes.config(state=NORMAL)
        textmilkshakes.focus()
        textmilkshakes.delete(0, END)
    elif var16.get() == 0:
        textmilkshakes.config(state=DISABLED)
        e_milkshakes.set('0')

def margaritas():
    if var17.get() == 1:
        textmargaritas.config(state=NORMAL)
        textmargaritas.focus()
        textmargaritas.delete(0, END)
    elif var17.get() == 0:
        textmargaritas.config(state=DISABLED)
        e_margaritas.set('0')

def juices():
    if var18.get() == 1:
        textjuices.config(state=NORMAL)
        textjuices.focus()
        textjuices.delete(0, END)
    elif var18.get() == 0:
        textjuices.config(state=DISABLED)
        e_juices.set('0')

def oreo():
    if var19.get() == 1:
        textcheesecake.config(state=NORMAL)
        textcheesecake.focus()
        textcheesecake.delete(0, END)
    elif var19.get() == 0:
        textcheesecake.config(state=DISABLED)
        e_cheesecake.set('0')

def apple():
    if var20.get() == 1:
        texttiramisu.config(state=NORMAL)
        texttiramisu.focus()
        texttiramisu.delete(0, END)
    elif var20.get() == 0:
        texttiramisu.config(state=DISABLED)
        e_tiramisu.set('0')

def kitkat():
    if var21.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    elif var21.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')

def vanilla():
    if var22.get() == 1:
        textgelato.config(state=NORMAL)
        textgelato.focus()
        textgelato.delete(0, END)
    elif var22.get() == 0:
        textgelato.config(state=DISABLED)
        e_gelato.set('0')

def banana():
    if var23.get() == 1:
        textapplepie.config(state=NORMAL)
        textapplepie.focus()
        textapplepie.delete(0, END)
    elif var23.get() == 0:
        textapplepie.config(state=DISABLED)
        e_applepie.set('0')

def brownie():
    if var24.get() == 1:
        textbrownies.config(state=NORMAL)
        textbrownies.focus()
        textbrownies.delete(0, END)
    elif var24.get() == 0:
        textbrownies.config(state=DISABLED)
        e_brownies.set('0')

def pineapple():
    if var25.get() == 1:
        textmousse.config(state=NORMAL)
        textmousse.focus()
        textmousse.delete(0, END)
    elif var25.get() == 0:
        textmousse.config(state=DISABLED)
        e_mousse.set('0')

def chocolate():
    if var26.get() == 1:
        textchurros.config(state=NORMAL)
        textchurros.focus()
        textchurros.delete(0, END)
    elif var26.get() == 0:
        textchurros.config(state=DISABLED)
        e_churros.set('0')

def tart():
    if var27.get() == 1:
        texttart.config(state=NORMAL)
        texttart.focus()
        texttart.delete(0, END)
    elif var27.get() == 0:
        texttart.config(state=DISABLED)
        e_tart.set('0')
#creating window
root = Tk()
root.geometry('1270x690+0+0')
#root.resizable(0, 0)
root.title('Canteen Management System created by GROUP 4')
root.config(bg='firebrick4')
topFrame = Frame(root, bd=10, relief=RIDGE, bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame, text='Canteen Information System', font=('arial', 30, 'bold'), fg='yellow', bd=9,
                   bg='red4', width=51)
labelTitle.grid(row=0, column=0)

# frames
menuFrame = Frame(root, bd=10, relief=RIDGE, bg='firebrick4')
menuFrame.pack(side=LEFT)
costFrame = Frame(menuFrame, bd=4, relief=RIDGE, bg='firebrick4', pady=10)
costFrame.pack(side=BOTTOM)
foodFrame = LabelFrame(menuFrame, text='Main', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4', )
foodFrame.pack(side=LEFT)
drinksFrame = LabelFrame(menuFrame, text='Snack&Drink(Sninks)', font=('arial', 19, 'bold'), bd=10, relief=RIDGE,
                         fg='red4')
drinksFrame.pack(side=LEFT)
cakesFrame = LabelFrame(menuFrame, text='Sweets', font=('arial', 19, 'bold'), bd=10, relief=RIDGE, fg='red4')
cakesFrame.pack(side=LEFT)
rightFrame = Frame(root, bd=15, relief=RIDGE, bg='red4')
rightFrame.pack(side=RIGHT)
calculatorFrame = Frame(rightFrame, bd=1, relief=RIDGE, bg='red4')
calculatorFrame.pack()
recieptFrame = Frame(rightFrame, bd=4, relief=RIDGE, bg='red4')
recieptFrame.pack()
buttonFrame = Frame(rightFrame, bd=3, relief=RIDGE, bg='red4')
buttonFrame.pack()

# Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
#setting string variables for main
e_chicken = StringVar()
e_pancake = StringVar()
e_noodles = StringVar()
e_paella = StringVar()
e_ribs = StringVar()
e_shrimp = StringVar()
e_ravioli = StringVar()
e_lobster = StringVar()
e_sushi = StringVar()
#setting string variables for snacks and drinks
e_frenchfries = StringVar()
e_guacamole = StringVar()
e_springrolls = StringVar()
e_nachos = StringVar()
e_icedcoffee = StringVar()
e_quesadillas = StringVar()
e_milkshakes = StringVar()
e_margaritas = StringVar()
e_juices = StringVar()
#setting string variables for sweets
e_cheesecake = StringVar()
e_blackforest = StringVar()
e_gelato = StringVar()
e_tiramisu = StringVar()
e_tart = StringVar()
e_applepie = StringVar()
e_brownies = StringVar()
e_mousse = StringVar()
e_churros = StringVar()
#setting string variables for costs
costofmainvar = StringVar()
costofsninksvar = StringVar()
costofsweetsvar = StringVar()
subtotalvar = StringVar()
servicetaxvar = StringVar()
totalcostvar = StringVar()
#setting the value 0
e_chicken.set('0')
e_pancake.set('0')
e_noodles.set('0')
e_ribs.set('0')
e_ravioli.set('0')
e_paella.set('0')
e_shrimp.set('0')
e_lobster.set('0')
e_sushi.set('0')

e_frenchfries.set('0')
e_guacamole.set('0')
e_springrolls.set('0')
e_icedcoffee.set('0')
e_nachos.set('0')
e_quesadillas.set('0')
e_milkshakes.set('0')
e_margaritas.set('0')
e_juices.set('0')

e_blackforest.set('0')
e_applepie.set('0')
e_mousse.set('0')
e_tiramisu.set('0')
e_churros.set('0')
e_cheesecake.set('0')
e_tart.set('0')
e_brownies.set('0')
e_gelato.set('0')

#check button for main foods
chicken = Checkbutton(foodFrame, text='Chicken', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var1
                      , command=chicken)
chicken.grid(row=0, column=0, sticky=W)

pancake = Checkbutton(foodFrame, text='Pancake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var2
                      , command=pancake)
pancake.grid(row=1, column=0, sticky=W)

ribs = Checkbutton(foodFrame, text='Ribs', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var3
                   , command=ribs)
ribs.grid(row=2, column=0, sticky=W)

noodles = Checkbutton(foodFrame, text='Noodles', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var4
                      , command=noodles)
noodles.grid(row=3, column=0, sticky=W)

Ravioli = Checkbutton(foodFrame, text='Ravioli', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var5
                      , command=Ravioli)
Ravioli.grid(row=4, column=0, sticky=W)

paella = Checkbutton(foodFrame, text='Paella', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var6
                     , command=paella)
paella.grid(row=5, column=0, sticky=W)

shrimp = Checkbutton(foodFrame, text='Shrimp', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var7,
                     command=shrimp)
shrimp.grid(row=6, column=0, sticky=W)

sushi = Checkbutton(foodFrame, text='Sushi', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var8
                    , command=sushi)
sushi.grid(row=7, column=0, sticky=W)

lobster = Checkbutton(foodFrame, text='Lobster', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var9
                      , command=lobster)
lobster.grid(row=8, column=0, sticky=W)

# Entry Fields for Main Items
textchicken = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=0, column=1)

textpancake = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pancake)
textpancake.grid(row=1, column=1)

textribs = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_ribs)
textribs.grid(row=2, column=1)

textnoodles = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_noodles)
textnoodles.grid(row=3, column=1)

textravioli = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_ravioli)
textravioli.grid(row=4, column=1)

textpaella = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paella)
textpaella.grid(row=5, column=1)

textshrimp = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_shrimp)
textshrimp.grid(row=6, column=1)

textsushi = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sushi)
textsushi.grid(row=7, column=1)

textlobster = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lobster)
textlobster.grid(row=8, column=1)

#check button for snacks and drinks
french_fries = Checkbutton(drinksFrame, text='French Fries', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                           variable=var10, command=french_fries)
french_fries.grid(row=0, column=0, sticky=W)

guacamole = Checkbutton(drinksFrame, text='Guacamole', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var11,
                        command=guacamole)
guacamole.grid(row=1, column=0, sticky=W)

spring_rolls = Checkbutton(drinksFrame, text='SpringRolls', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                           variable=var12, command=spring_rolls)
spring_rolls.grid(row=2, column=0, sticky=W)

nachos = Checkbutton(drinksFrame, text='Nachos', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var13
                     , command=nachos)
nachos.grid(row=3, column=0, sticky=W)

quesadillas = Checkbutton(drinksFrame, text='Quesadillas', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                          variable=var14, command=quesadillas)
quesadillas.grid(row=4, column=0, sticky=W)

iced_coffee = Checkbutton(drinksFrame, text='Iced Coffee', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                          variable=var15, command=iced_coffee)
iced_coffee.grid(row=5, column=0, sticky=W)

milkshakes = Checkbutton(drinksFrame, text='Milkshakes', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                         variable=var16, command=milkshakes)
milkshakes.grid(row=6, column=0, sticky=W)

margaritas = Checkbutton(drinksFrame, text='Margaritas', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                         variable=var17, command=margaritas)
margaritas.grid(row=7, column=0, sticky=W)

juices = Checkbutton(drinksFrame, text='Juices', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                     variable=var18, command=juices)
juices.grid(row=8, column=0, sticky=W)

# entry fields for drink items
textfrenchfries = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                        textvariable=e_frenchfries)
textfrenchfries.grid(row=0, column=1)

textguacamole = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_guacamole)
textguacamole.grid(row=1, column=1)

textspringrolls = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                        textvariable=e_springrolls)
textspringrolls.grid(row=2, column=1)

textnachos = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_nachos)
textnachos.grid(row=3, column=1)

textquesadillas = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                        textvariable=e_quesadillas)
textquesadillas.grid(row=4, column=1)

texticedcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_icedcoffee)
texticedcoffee.grid(row=5, column=1)

textmilkshakes = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_milkshakes)
textmilkshakes.grid(row=6, column=1)

textmargaritas = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_margaritas)
textmargaritas.grid(row=7, column=1)

textjuices = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_juices)
textjuices.grid(row=8, column=1)

#check button for Sweets
cheesecake = Checkbutton(cakesFrame, text='Cheesecake', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                         variable=var19, command=oreo)
cheesecake.grid(row=0, column=0, sticky=W)

tiramisu = Checkbutton(cakesFrame, text='Tiramisu', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var20,
                       command=apple)
tiramisu.grid(row=1, column=0, sticky=W)

black_forest = Checkbutton(cakesFrame, text='BlackForest', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,
                           variable=var21, command=kitkat)
black_forest.grid(row=2, column=0, sticky=W)

gelato = Checkbutton(cakesFrame, text='Gelato', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var22,
                     command=vanilla)
gelato.grid(row=3, column=0, sticky=W)

apple_pie = Checkbutton(cakesFrame, text='Apple Pie', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var23,
                        command=banana)
apple_pie.grid(row=4, column=0, sticky=W)

brownies = Checkbutton(cakesFrame, text='Brownies', font=('arial', 18, 'bold'), onvalue=1, offvalue=0, variable=var24,
                       command=brownie)
brownies.grid(row=5, column=0, sticky=W)

mousse = Checkbutton(cakesFrame, text='Mousse', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var25,
                     command=pineapple)
mousse.grid(row=6, column=0, sticky=W)

churros = Checkbutton(cakesFrame, text='Churros', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var26,
                      command=chocolate)
churros.grid(row=7, column=0, sticky=W)

tart = Checkbutton(cakesFrame, text='Tart', font=('arial', 18, 'bold'), onvalue=1, offvalue=0,variable=var27,
                   command=tart)
tart.grid(row=8, column=0, sticky=W)

# entry fields for sweets
textcheesecake = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_cheesecake)
textcheesecake.grid(row=0, column=1)

texttiramisu = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tiramisu)
texttiramisu.grid(row=1, column=1)

textblackforest = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,
                        textvariable=e_blackforest)
textblackforest.grid(row=2, column=1)

textgelato = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_gelato)
textgelato.grid(row=3, column=1)

textapplepie = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_applepie)
textapplepie.grid(row=4, column=1)

textbrownies = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownies)
textbrownies.grid(row=5, column=1)

textmousse = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mousse)
textmousse.grid(row=6, column=1)

textchurros = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_churros)
textchurros.grid(row=7, column=1)

texttart = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_tart)
texttart.grid(row=8, column=1)

# costlabels & entry fields
labelCostofFood = Label(costFrame, text='Cost of Main', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelCostofFood.grid(row=0, column=0)

textCostofFood = Entry(costFrame, font=('arial', 16, 'bold'),bd=6,width=14,state='readonly',textvariable=costofmainvar)
textCostofFood.grid(row=0, column=1, padx=41)

labelCostofDrinks = Label(costFrame, text='Cost of Sninks', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelCostofDrinks.grid(row=1, column=0)

textCostofDrinks = Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofsninksvar)
textCostofDrinks.grid(row=1, column=1, padx=41)

labelCostofCakes = Label(costFrame, text='Cost of Sweets', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelCostofCakes.grid(row=2, column=0)

textCostofCakes = Entry(costFrame, font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofsweetsvar)
textCostofCakes.grid(row=2, column=1, padx=41)

labelSubTotal = Label(costFrame, text='Sub Total', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelSubTotal.grid(row=0, column=2)

textSubTotal = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly', textvariable=subtotalvar)
textSubTotal.grid(row=0, column=3, padx=41)

labelServiceTax = Label(costFrame, text='Service Tax', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelServiceTax.grid(row=1, column=2)

textServiceTax = Entry(costFrame, font=('arial', 16, 'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1, column=3, padx=41)

labelTotalCost = Label(costFrame, text='Total Cost', font=('arial', 16, 'bold'), bg='firebrick4', fg='white')
labelTotalCost.grid(row=2, column=2)

textTotalCost = Entry(costFrame, font=('arial', 16, 'bold'), bd=6, width=14, state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2, column=3, padx=41)

# Buttons
buttonTotal = Button(buttonFrame, text='Total', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5,
                     command=totalcost)
buttonTotal.grid(row=0, column=0)

buttonReceipt = Button(buttonFrame, text='Receipt', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5,
                    command=receipt)
buttonReceipt.grid(row=0, column=1)

buttonSave = Button(buttonFrame, text='Save', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5,
                    command=save)
buttonSave.grid(row=0, column=2)

buttonSend = Button(buttonFrame, text='Send', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5,
                    command=send)
buttonSend.grid(row=0, column=3)

buttonReset = Button(buttonFrame, text='Reset', font=('arial', 14, 'bold'), fg='white', bg='red4', bd=3, padx=5,
                     command=reset)
buttonReset.grid(row=0, column=4)

# textarea for receipt
textReceipt = Text(recieptFrame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
textReceipt.grid(row=0, column=0)

# Calculator
operator = ''

def buttonClick(numbers):
    global operator
    operator = operator + numbers
    calculatorField.delete(0, END)
    calculatorField.insert(END, operator)

def clear():
    global operator
    operator = ''
    calculatorField.delete(0, END)

def answer():
    global operator
    result = str(eval(operator))
    calculatorField.delete(0, END)
    calculatorField.insert(0, result)
    operator = ''

calculatorField = Entry(calculatorFrame, font=('arial', 16, 'bold'), width=32, bd=4)
calculatorField.grid(row=0, column=0, columnspan=4)

button7 = Button(calculatorFrame, text='7', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('7'))
button7.grid(row=1, column=0)

button8 = Button(calculatorFrame, text='8', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                 command=lambda: buttonClick('8'))
button8.grid(row=1, column=1)

button9 = Button(calculatorFrame, text='9', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                 , command=lambda: buttonClick('9'))
button9.grid(row=1, column=2)

buttonPlus = Button(calculatorFrame, text='+', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                    , command=lambda: buttonClick('+'))
buttonPlus.grid(row=1, column=3)

button4 = Button(calculatorFrame, text='4', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                 , command=lambda: buttonClick('4'))
button4.grid(row=2, column=0)

button5 = Button(calculatorFrame, text='5', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                 , command=lambda: buttonClick('5'))
button5.grid(row=2, column=1)

button6 = Button(calculatorFrame, text='6', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                 , command=lambda: buttonClick('6'))
button6.grid(row=2, column=2)

buttonMinus = Button(calculatorFrame, text='-', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                     , command=lambda: buttonClick('-'))
buttonMinus.grid(row=2, column=3)

button1 = Button(calculatorFrame, text='1', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                 , command=lambda: buttonClick('1'))
button1.grid(row=3, column=0)

button2 = Button(calculatorFrame, text='2', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                 , command=lambda: buttonClick('2'))
button2.grid(row=3, column=1)

button3 = Button(calculatorFrame, text='3', font=('arial', 16, 'bold'), fg='red4', bg='white', bd=6, width=6
                 , command=lambda: buttonClick('3'))
button3.grid(row=3, column=2)

buttonMult = Button(calculatorFrame, text='*', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                    , command=lambda: buttonClick('*'))
buttonMult.grid(row=3, column=3)

buttonAns = Button(calculatorFrame, text='Ans', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                   command=answer)
buttonAns.grid(row=4, column=0)

buttonClear = Button(calculatorFrame, text='Clear', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                     , command=clear)
buttonClear.grid(row=4, column=1)

button0 = Button(calculatorFrame, text='0', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6
                 , command=lambda: buttonClick('0'))
button0.grid(row=4, column=2)

buttonDiv = Button(calculatorFrame, text='/', font=('arial', 16, 'bold'), fg='yellow', bg='red4', bd=6, width=6,
                   command=lambda: buttonClick('/'))
buttonDiv.grid(row=4, column=3)
#method will loop forever, waiting for events from the user, until the user exits the program
root.mainloop()