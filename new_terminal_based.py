import os


class Colors:
    SEA_BLUE = '\033[38;5;32m'
    OCEAN_BLUE = '\033[38;5;33m'
    SKY_BLUE = '\033[38;5;39m'
    AQUA = '\033[38;5;45m'
    WAVE_BLUE = '\033[38;5;27m'
    WARNING_RED = '\033[38;5;196m'
    ALERT_RED = '\033[38;5;160m'
    DANGER_RED = '\033[38;5;124m'
    EXIT_COLOR = '\033[38;5;208m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


grocery_list = []
status_dict = {}
categories = ["Fruits & Vegetables", "Dairy", "Bakery", "Meat & Seafood", "Pantry Staples", "Snacks", "Beverages",
              "Other"]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def mapping():
    for item in grocery_list:
        if item["name"] not in status_dict:
            status_dict[item["name"]] = "Incompleted"
    for item_name in list(status_dict.keys()):
        if item_name not in [i["name"] for i in grocery_list]:
            del status_dict[item_name]


def add_item():
    print(Colors.SEA_BLUE + "\n📝 Add New Grocery Item" + Colors.ENDC)
    new_item = input("Enter item name (or 0 to cancel): ").strip()
    if new_item == "0":
        return
    category = input(f"Choose a category {categories}: ")
    quantity = int(input("Enter quantity: "))
    unit = input("Enter unit (pcs/kg/liters/packs): ")
    price = float(input("Enter estimated price (optional, default 0): ") or 0.0)
    grocery_list.append({"name": new_item, "category": category, "quantity": quantity, "unit": unit, "price": price})
    mapping()
    print(Colors.EXIT_COLOR + f"'{new_item}' added successfully!" + Colors.ENDC)


def preview():
    print(Colors.SEA_BLUE + "\n-- Grocery List --\n" + Colors.ENDC)
    if not grocery_list:
        print("No items yet.")
        return
    for idx, item in enumerate(grocery_list, 1):
        print(f"{idx}. {item['quantity']} {item['unit']} {item['name']} ({item['category']}) - ${item['price']:.2f}")


def toggle_status():
    preview()
    if not grocery_list:
        return
    task_number = int(input("Enter the item number to toggle status (or 0 to return): "))
    if task_number == 0:
        return
    if 1 <= task_number <= len(grocery_list):
        selected_item = grocery_list[task_number - 1]["name"]
        new_status = "Completed" if status_dict[selected_item] == "Incompleted" else "Incompleted"
        status_dict[selected_item] = new_status
        print(Colors.SEA_BLUE + f"\nItem '{selected_item}' updated to '{new_status}'!" + Colors.ENDC)


def remove_item():
    preview()
    if not grocery_list:
        return
    task_number = int(input("Enter the item number to remove (or 0 to return): "))
    if task_number == 0:
        return
    if 1 <= task_number <= len(grocery_list):
        removed_item = grocery_list.pop(task_number - 1)
        del status_dict[removed_item["name"]]
        print(Colors.EXIT_COLOR + f"'{removed_item['name']}' removed successfully!" + Colors.ENDC)


def main_menu():
    while True:
        print(Colors.SKY_BLUE + "\nGrocery Shopping List:\n" +
              Colors.OCEAN_BLUE + "1. Add Item\n" +
              Colors.AQUA + "2. View List\n" +
              Colors.WAVE_BLUE + "3. Toggle Item Status\n" +
              Colors.WARNING_RED + "4. Remove Item\n" +
              Colors.EXIT_COLOR + "5. Exit" + Colors.ENDC)

        choice = input("Choose an option: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            preview()
        elif choice == "3":
            toggle_status()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print(Colors.EXIT_COLOR + "\nExiting Grocery Shopping List. Goodbye!" + Colors.ENDC)
            break
        else:
            print(Colors.ALERT_RED + "Invalid choice. Please try again." + Colors.ENDC)
main_menu()