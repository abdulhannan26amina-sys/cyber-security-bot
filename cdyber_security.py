from sklearn.tree import DecisionTreeClassifier
import streamlit as st
# password failed,Location
x=[[1,0],[2,1],[8,5],[10,4],[0,0],[9,6]]
y=[0,0,1,1,0,1]

status={0:"Real user",1:"Hacker user"}

model=DecisionTreeClassifier(max_depth=4,random_state=42)
model.fit(x,y)

password=st.number_input(" Enter the fales password ")
Location=st.number_input(" Enter the change Location ")

if st.button("check Usre Status"):
	prediction=model.predict([[password,Location]])
	dic=prediction[0]

	st.write(f" The user was {status[dic]} " ) 




