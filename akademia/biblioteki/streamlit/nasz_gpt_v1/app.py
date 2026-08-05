import streamlit as st

st.title(":parrot: Papuga")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("O co chcesz zapytać papugę?")
if prompt:
    with st.chat_message("human"):
        st.markdown(prompt)

    st.session_state["messages"].append({"role": "human", "content": prompt})


with st.chat_message("ai"):
    response = f"Papuga powtarza: {prompt}"
    st.markdown(response)
    st.session_state["messages"].append({"role": "ai", "content": response})