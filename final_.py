import streamlit as st

if 'grocery_list' not in st.session_state:
    st.session_state.grocery_list = []

if 'categories' not in st.session_state:
    st.session_state.categories = ["Fruits & Vegetables", "Dairy", "Bakery", "Meat & Seafood", "Pantry Staples",
                                   "Snacks", "Beverages", "Other"]


def mapping():
    if 'status_dict' not in st.session_state:
        st.session_state.status_dict = {}

    for item in st.session_state.grocery_list:
        if item["name"] not in st.session_state.status_dict:
            st.session_state.status_dict[item["name"]] = "Incompleted"

    for item_name in list(st.session_state.status_dict.keys()):
        if item_name not in [i["name"] for i in st.session_state.grocery_list]:
            st.session_state.status_dict.pop(item_name)


def add_items():
    with st.form("Add Items"):
        st.subheader("📝 Add New Grocery Item")
        new_item = st.text_input("Enter item name")
        category = st.selectbox("Category", st.session_state.categories)
        quantity = st.number_input("Quantity", min_value=1, step=1, value=1)
        unit = st.selectbox("Unit", ["pcs", "kg", "liters", "packs"])
        price = st.number_input("Estimated Price (Optional)", min_value=0.0, step=0.5)

        submitted = st.form_submit_button("Add Item")

        if submitted and new_item:
            st.session_state.grocery_list.append({
                "name": new_item,
                "category": category,
                "quantity": quantity,
                "unit": unit,
                "price": price
            })
            mapping()
            st.success(f"'{new_item}' added successfully!")


def quick_add():
    st.subheader("⚡ Quick Add Common Items")

    common_items = ["Milk", "Eggs", "Bread", "Bananas", "Chicken", "Rice", "Tomatoes"]
    col1, col2, col3 = st.columns(3)

    for idx, item in enumerate(common_items):
        with (col1 if idx % 3 == 0 else col2 if idx % 3 == 1 else col3):
            if st.button(f"➕ {item}"):
                st.session_state.grocery_list.append({
                    "name": item,
                    "category": "Other",
                    "quantity": 1,
                    "unit": "pcs",
                    "price": 0.0
                })
                st.success(f"'{item}' added!")
                mapping()


def preview():
    tab1, tab2, tab3 = st.tabs(["All", "Completed", "Incompleted"])

    with tab1:
        if not st.session_state.grocery_list:
            st.write("No items yet.")
        else:
            for idx, item in enumerate(st.session_state.grocery_list, 1):
                checked = st.checkbox(
                    f"{idx}. {item['quantity']} {item['unit']} {item['name']} ({item['category']}) - ${item['price']:.2f}",
                    value=st.session_state.status_dict[item["name"]] == "Completed")
                if checked:
                    st.session_state.status_dict[item["name"]] = "Completed"
                else:
                    st.session_state.status_dict[item["name"]] = "Incompleted"

    with tab2:
        for idx, item in enumerate(st.session_state.grocery_list, 1):
            if st.session_state.status_dict[item["name"]] == "Completed":
                st.write(
                    f"✅ {idx}. {item['quantity']} {item['unit']} {item['name']} ({item['category']}) - ${item['price']:.2f}")

    with tab3:
        for idx, item in enumerate(st.session_state.grocery_list, 1):
            if st.session_state.status_dict[item["name"]] == "Incompleted":
                st.write(
                    f"❌ {idx}. {item['quantity']} {item['unit']} {item['name']} ({item['category']}) - ${item['price']:.2f}")


def remove_item():
    for idx, item in enumerate(st.session_state.grocery_list):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(
                f"{idx + 1}. {item['quantity']} {item['unit']} {item['name']} ({item['category']}) - ${item['price']:.2f}")
        with col2:
            if st.button("❌ Remove", key=f"remove_{idx}"):
                st.session_state.grocery_list.remove(item)
                mapping()

def main():
    st.set_page_config(page_title="Grocery List", layout="wide", initial_sidebar_state="expanded")
    st.title("🛒 Grocery Shopping List")

    page = st.sidebar.radio("Navigation", ["Quick Add", "Add Item", "View List", "Remove Items"])

    if page == "Quick Add":
        quick_add()
    elif page == "Add Item":
        add_items()
        mapping()
    elif page == "View List":
        preview()
        mapping()
    elif page == "Remove Items":
        remove_item()
        mapping()


if __name__ == "__main__":
    main()
