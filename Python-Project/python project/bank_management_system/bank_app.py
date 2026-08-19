import streamlit as st

# ---------------- SESSION STORAGE ----------------

if "accounts" not in st.session_state:
    st.session_state.accounts = {}

if "bank_name" not in st.session_state:
    st.session_state.bank_name = "National Python Bank"


# ---------------- OOP CLASS ----------------

class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance


    # Object Method
    def deposit(self, amount):
        self.balance = self.add(self.balance, amount)


    # Object Method
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance = self.subtract(self.balance, amount)


    # Object Method
    def display(self):
        return {
            "Bank": st.session_state.bank_name,
            "Customer": self.name,
            "Account Number": self.account_number,
            "Balance": self.balance
        }


    # Class Method
    @classmethod
    def change_bank_name(cls, new_name):
        st.session_state.bank_name = new_name


    # Static Methods
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):      
        return a - b


# ---------------- UI ----------------

st.title("🏦 Bank Management System")

st.write(f"### Bank: {st.session_state.bank_name}")


# ---------------- ROLE SELECTION ----------------

role = st.sidebar.selectbox(
    "Login As",
    ["Admin", "User"]
)


# ================= ADMIN =================

if role == "Admin":

    st.sidebar.header("Admin Menu") 

    admin_menu = st.sidebar.selectbox(
        "Select Option",
        ["Create Account", "Change Bank Name"]
    )


    # Create Account
    if admin_menu == "Create Account":

        st.header("Create New Account")

        name = st.text_input("Customer Name")
        acc = st.number_input("Account Number", step=1)
        bal = st.number_input("Initial Balance")

        if st.button("Create Account"):

            if acc in st.session_state.accounts:
                st.error("Account already exists")

            else:
                st.session_state.accounts[acc] = BankAccount(name, acc, bal)
                st.success("Account Created Successfully")


    # Change Bank Name
    elif admin_menu == "Change Bank Name":

        st.header("Change Bank Name")

        new_name = st.text_input("Enter New Bank Name")

        if st.button("Update Bank Name"):

            BankAccount.change_bank_name(new_name)
            st.success("Bank Name Updated Successfully")



# ================= USER =================

elif role == "User":

    st.sidebar.header("User Menu")

    user_menu = st.sidebar.selectbox(
        "Select Option",
        ["Check Account Details", "Deposit", "Withdraw"]
    )


    # Check Account
    if user_menu == "Check Account Details":

        st.header("Account Details")

        acc = st.number_input("Enter Account Number", step=1)

        if st.button("Check Details"):

            if acc in st.session_state.accounts:

                data = st.session_state.accounts[acc].display()

                for k, v in data.items():
                    st.write(f"**{k}:** {v}")

            else:
                st.error("Account Not Found")


    # Deposit
    elif user_menu == "Deposit":

        st.header("Deposit Money")

        acc = st.number_input("Enter Account Number", step=1)
        amount = st.number_input("Enter Amount")

        if st.button("Deposit"):

            if acc in st.session_state.accounts:

                st.session_state.accounts[acc].deposit(amount)
                st.success("Deposit Successful")

            else:
                st.error("Account Not Found")


    # Withdraw
    elif user_menu == "Withdraw":

        st.header("Withdraw Money")

        acc = st.number_input("Enter Account Number", step=1)
        amount = st.number_input("Enter Amount")

        if st.button("Withdraw"):

            if acc in st.session_state.accounts:

                msg = st.session_state.accounts[acc].withdraw(amount)

                if msg:
                    st.error(msg)
                else:
                    st.success("Withdrawal Successful")

            else:
                st.error("Account Not Found") 