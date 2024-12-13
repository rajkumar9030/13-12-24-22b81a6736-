import streamlit as st


class Newbank:
    amount_bal = 1000000
    withdraw_count = 0

    def viewoptions(self):
        st.write("1. Deposit\n2. Withdraw\n3. Balance enquiry\n0. Exit")

    def validate(self):
        pin_no = st.text_input("Enter PIN number: ", type="password", key="pin_input")

        if pin_no == "1234":
            while True:
                # Display options using st.radio with a unique key to avoid duplicate ID issues
                choice = st.radio("Choose an option:",
                                  ["Deposit", "Withdraw", "Balance enquiry", "Exit"],
                                  key="choice_radio")

                if choice == "Deposit":
                    amount_deposit = st.number_input("Enter deposit amount:", min_value=100, step=100,
                                                     key="deposit_amount")
                    if amount_deposit < 100:
                        st.write("Enter only amount more than 100.")
                    elif amount_deposit % 100 != 0:
                        st.write("Only multiples of 100 are allowed.")
                    elif amount_deposit > 50000:
                        st.write("Deposit only available up to 50k.")
                    else:
                        self.amount_bal += amount_deposit
                        st.write(f"Deposit of {amount_deposit} successful. Current balance: {self.amount_bal}.")

                elif choice == "Withdraw":
                    if self.withdraw_count >= 3:
                        st.write("Withdrawal limit reached for today.")
                        break

                    amount_withdraw = st.number_input("Enter withdraw amount:", min_value=100, step=100,
                                                      key="withdraw_amount")
                    if amount_withdraw < 100:
                        st.write("Enter only amount more than 100.")
                    elif amount_withdraw % 100 != 0:
                        st.write("Only multiples of 100 are allowed.")
                    elif amount_withdraw > self.amount_bal:
                        st.write("Balance not available.")
                    elif self.amount_bal <= 500:
                        st.write("Withdraw not possible. Insufficient funds.")
                    elif amount_withdraw > 20000:
                        st.write("Limit exceeded. Only 20k possible.")
                    else:
                        self.amount_bal -= amount_withdraw
                        self.withdraw_count += 1
                        st.write(f"Withdraw of {amount_withdraw} successful. Current balance: {self.amount_bal}.")

                elif choice == "Balance enquiry":
                    st.write(f"Your current balance is: {self.amount_bal}")

                elif choice == "Exit":
                    st.write("Exiting...")
                    break
        else:
            st.write("Incorrect PIN. Please try again.")
            st.stop()  # Stops execution, prompting user to re-enter PIN.


if __name__ == "__main__":
    obj = Newbank()
    obj.validate()
