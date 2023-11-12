import tkinter as tk

# Initialize an empty inventory
inventory = {}

def add_item():
    item_name = item_name_entry.get()
    quantity = int(quantity_entry.get())
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    update_inventory_display()

def remove_item():
    item_name = item_name_entry.get()
    quantity = int(quantity_entry.get())
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
        else:
            status_label.config(text="Insufficient quantity in inventory.")
    else:
        status_label.config(text="Item not found in inventory.")
    update_inventory_display()

def update_inventory_display():
    inventory_text.config(state=tk.NORMAL)
    inventory_text.delete(1.0, tk.END)
    for item, quantity in inventory.items():
        # Create "+" and "-" buttons next to each item
        item_label = tk.Label(inventory_text, text=f"{item}: {quantity} ")
        add_button = tk.Button(inventory_text, text="+", command=lambda item=item: increment_item(item))
        subtract_button = tk.Button(inventory_text, text="-", command=lambda item=item: decrement_item(item))
        inventory_text.window_create(tk.END, window=item_label)
        inventory_text.window_create(tk.END, window=add_button)
        inventory_text.window_create(tk.END, window=subtract_button)
        inventory_text.insert(tk.END, "\n")
    inventory_text.config(state=tk.DISABLED)

def increment_item(item):
    inventory[item] += 1
    update_inventory_display()

def decrement_item(item):
    if inventory[item] > 0:
        inventory[item] -= 1
    update_inventory_display()

# Create the main window
root = tk.Tk()
root.title("Inventory Management")

# Create and pack GUI elements with larger dimensions
item_name_label = tk.Label(root, text="Item Name:", font=("Arial", 14))
item_name_label.pack()

item_name_entry = tk.Entry(root, font=("Arial", 14))
item_name_entry.pack()

quantity_label = tk.Label(root, text="Quantity:", font=("Arial", 14))
quantity_label.pack()

quantity_entry = tk.Entry(root, font=("Arial", 14))
quantity_entry.pack()

add_button = tk.Button(root, text="Add Item", command=add_item, font=("Arial", 14))
add_button.pack()

remove_button = tk.Button(root, text="Remove Item", command=remove_item, font=("Arial", 14))
remove_button.pack()

status_label = tk.Label(root, text="", font=("Arial", 14))
status_label.pack()

inventory_text = tk.Text(root, height=10, width=30, state=tk.DISABLED, font=("Arial", 14))
inventory_text.pack()

update_inventory_display()

root.geometry("400x500")  # Set the initial window size
root.mainloop()
