import streamlit as st
def find_largest(n1,n2,n3):
  return max(n1,n2,n3)
def main():
  st.title("Find the Laregest Number")
  n1=st.number_input("Enter 1st num")
  n2=st.number_input("Enter 2nd num")
  n3=st.number_input("Enter 3rd num")
  if st.button("Find Largest"):
    l=find_largest(n1,n2,n3)
    st.write(f"The largest number is:{l}")
if _name_ == "__main__":
  main()
