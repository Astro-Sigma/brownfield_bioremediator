import streamlit as st

st.title("Welcome to our Bioremediation Science Fair Project Website!")

st.markdown( """<style>@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap'); 

html, body, [class*="css"] {
    font-family: 'Roboto', sans-serif; 
    font-size: 12px;
    font-weight: 500;
    color: #091747;
}</style>""", unsafe_allow_html= True)

st.markdown(
        """
        <style>
        .stApp {
            background-color: #006ee6;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.text("""Our project is aimed to aid in the bioremediation selection process for either commercial or governmental organizations such that upon utilizing our program, the clientele shall be told the best bioremediator for the specific conditions of the brownfield that they have inputted.""")

st.text("""We have collected data on and researched a total of 10 species of bioremediators. They are listed as follows:
   1. Brassica juncea (Brown Mustard)
   2. Phanerochaete chrysosporium (Fungi)
   3. Sphingomonas paucimobilis (Bacteria)
   4. Pseudomonas putida (Bacteria)
   5. Populus deltoides (Eastern Cottonwood)
   6. Rhodococcus erythropolis (Bacteria)
   7. Helianthus annuus (Common Sunflower)
   8. Pleurotus ostreatus (Oyster Mushroom)
   9. Typha latifolia (Bulrush)
   10. Bacillus subtilis (Bacteria) 
""")
