import streamlit as st

with st.sidebar:
    example_name = st.selectbox(
        "Wybierz przykład do pokazania",
        [
            "Kolumny",
            "Dialog",
            "Popover",
            "Expander",
            "Taby",
        ],
    )

#
# Columns
#
if example_name == "Kolumny":
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkJP2a69-Bp0jAGh4EcxMJPMFPc8XuGhLGUb2pvFFZxOWPukvqaWKq2x50pdDL4MJvZ1o&usqp=CAU")

    with col2:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxx1_8Yb61UaQpbn7bgEvJm04LfhWeqmdROdD93sR__0gIJsm06ymTOLO7nVY5CqFA0ew&usqp=CAU")

    with col3:
        st.image("https://miro.medium.com/v2/resize:fit:1200/1*QB9UaIfx-Gll2-kaeDJN4A.jpeg")

#
# Dialog
#
elif example_name == "Dialog":
    @st.dialog("Oddaj głos")
    def vote(item):
        st.write(f"Dlaczego {item} to twoje fundamentalne oddziaływanie?")
        reason = st.text_input("Ponieważ...")
        if st.button("Prześlij"):
            st.session_state["vote"] = {"item": item, "reason": reason}
            st.button("Wyczyść")
            st.rerun()

    if "vote" not in st.session_state:
        st.write("Jakie jest twoje ulubione ulubione fundamentalne oddziaływanie?")
        if st.button("Grawitacja", use_container_width=True):
            vote("Grawitacja")
        if st.button("Elektromagnetyzm", use_container_width=True):
            vote("Elektromagnetyzm")
        if st.button("Oddziaływanie silne", use_container_width=True):
            vote("Oddziaływanie silne")
        if st.button("Oddziaływanie słabe", use_container_width=True):
            vote("Oddziaływanie słabe")
    else:
        f"Głos oddany na {st.session_state.vote['item']} ponieważ {st.session_state.vote['reason']}"

        if st.button("Wyczyść", key="clear_vote"):
            del st.session_state["vote"]
            st.rerun()




#
# Popover
#
elif example_name == "Popover":
    with st.popover("Otwórz"):
        st.markdown("Witam!")
        name = st.text_input("Jak masz na imię?")

    st.write("Cześć!", name)


#
# Expander
#
elif example_name == "Expander":
    st.image("https://miro.medium.com/v2/resize:fit:1200/1*QB9UaIfx-Gll2-kaeDJN4A.jpeg")

    with st.expander("Dlaczego jabłko spada?"):
        st.markdown('''
Jabłko spada z drzewa z powodu grawitacji. Grawitacja jest siłą przyciągania, która działa pomiędzy dwoma ciałami posiadającymi masę. W tym przypadku, Ziemia przyciąga jabłko ku sobie.

Sir Isaac Newton, angielski fizyk i matematyk, sformułował prawo powszechnego ciążenia, które wyjaśnia, dlaczego jabłko spada. Prawo to mówi, że każdy obiekt w kosmosie przyciąga każdy inny obiekt z siłą, która jest wprost proporcjonalna do iloczynu ich mas i odwrotnie proporcjonalna do kwadratu odległości między nimi.

Matematycznie można to wyrazić równaniem:
$$ F = G \\frac{m_1 m_2}{r^2} $$

gdzie:
- $ F $ to siła grawitacji,
- $ G $ to stała grawitacji,
- $ m_1 $ i $ m_2 $ to masy dwóch obiektów,
- $ r $ to odległość między środkami tych obiektów.

W przypadku jabłka spadającego z drzewa, siła grawitacji przyciąga jabłko ku Ziemi, powodując jego ruch w dół.
        ''')

#
# Tabs
#
elif example_name == "Taby":
    tab0, tab1, tab2, tab3 = st.tabs(["Grawitacja", "Elektromagnetyzm", "Oddziaływanie silne", "Oddziaływanie słabe"])
    with tab0:
        st.write("""
Grawitacja jest siłą przyciągania działającą między masami. Jest najsłabszym z czterech fundamentalnych oddziaływań,
ale ma nieskończony zasięg. Jest odpowiedzialna za takie zjawiska jak przyciąganie Ziemi do Słońca, utrzymywanie
planet na orbitach, oraz przyciąganie ciał do powierzchni Ziemi. Opisuje ją ogólna teoria względności Einsteina,
choć na poziomie klasycznym można używać prawa powszechnego ciążenia Newtona.
""")

    with tab1:
        st.write("""
Elektromagnetyzm jest siłą działającą między cząstkami naładowanymi elektrycznie. Odpowiada za zjawiska elektryczne,
magnetyczne i elektromagnetyczne, w tym światło. Jest znacznie silniejszy od grawitacji i ma nieskończony zasięg.
Przewodzi oddziaływania za pomocą fotonów, cząstek bez masy. Prawo Coulomba opisuje oddziaływania między ładunkami
elektrycznymi, a teoria kwantowej elektrodynamiki (QED) opisuje te procesy na poziomie kwantowym.
""")

    with tab2:
        st.write("""
Oddziaływanie silne jest najsilniejszym z fundamentalnych oddziaływań, ale ma bardzo krótki zasięg, ograniczony do
jądra atomowego. Jest odpowiedzialne za wiązanie kwarków w protony i neutrony oraz za utrzymywanie protonów i
neutronów w jądrze atomowym. Cząstki pośredniczące w tym oddziaływaniu to gluony. Chromodynamika kwantowa (QCD) jest
teorią opisującą oddziaływanie silne.
""")

    with tab3:
        st.write("""
Oddziaływanie słabe jest odpowiedzialne za procesy takie jak rozpad beta, w którym neutron przekształca się w proton,
elektron i neutrino. Choć jest silniejsze niż grawitacja, jest znacznie słabsze niż elektromagnetyzm i oddziaływanie
silne. Ma krótki zasięg, ograniczony do subatomowych odległości. Oddziaływanie to jest przenoszone przez bozony W i Z.
Oddziaływanie słabe jest jedynym z fundamentalnych oddziaływań, które potrafi zmieniać typy cząstek (np.
przekształcanie kwarków i leptonów).
""")
