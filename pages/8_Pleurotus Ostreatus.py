import streamlit as st

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

st.title("Pleurotus Ostreatus, aka Oyster Mushroom")

st.image("https://upload.wikimedia.org/wikipedia/commons/f/f6/Pleurotus_ostreatus_JPG7.jpg", width=200)

st.text("""Pleurotus ostreatus, commonly referred to as the oyster mushroom, is a saprophytic basidiomycete fungus belonging to the family Pleurotaceae. Native to temperate and subtropical forests, it is one of the most widely cultivated edible mushrooms globally due to its high nutritional value, ease of cultivation, and rapid growth on lignocellulosic waste substrates. Beyond its culinary and economic significance, P. ostreatus has garnered considerable attention for its potent bioremediation capabilities. As a white-rot fungus, it decomposes complex organic matter such as lignin, cellulose, and hemicellulose using an enzymatic arsenal that includes laccases, manganese peroxidases (MnPs), and versatile peroxidases (VPs). These enzymes confer upon P. ostreatus a unique ability to degrade a wide range of persistent environmental pollutants, including hydrocarbons, synthetic dyes, pesticides, and even certain heavy metals through biosorption and chelation mechanisms.

In the realm of bioremediation, Pleurotus ostreatus exhibits numerous strengths that position it as one of the most effective fungi for mycoremediation—the use of fungi to degrade or sequester contaminants in the environment. Its enzymatic system is particularly adept at breaking down high-molecular-weight aromatic hydrocarbons such as polycyclic aromatic hydrocarbons (PAHs), polychlorinated biphenyls (PCBs), and petroleum-based compounds, many of which are recalcitrant to bacterial degradation. This is possible due to its extracellular ligninolytic enzymes, which are non-specific oxidizers capable of attacking a broad spectrum of pollutants. Furthermore, P. ostreatus can be cultivated on agricultural waste substrates (e.g., straw, sawdust, corn cobs), making its application cost-effective and sustainable. It also plays a beneficial role in biosorption of heavy metals like cadmium (Cd), lead (Pb), and mercury (Hg), binding these elements to its mycelial biomass. However, there are critical limitations to consider. The fungus requires aerobic conditions for optimal enzymatic activity, which restricts its use in anoxic or waterlogged environments. It also prefers mildly acidic to neutral pH and stable temperatures, limiting its effectiveness in extreme environmental conditions. Moreover, although it can immobilize or transform certain heavy metals, it does not degrade them, raising concerns about how to manage the metal-laden fungal biomass post-remediation. Its slower growth compared to bacterial agents can also pose a temporal challenge, especially for emergency or high-volume cleanups.

Despite these constraints, Pleurotus ostreatus remains one of the most ecologically and economically viable organisms for use in large-scale bioremediation efforts. Its deployment has been demonstrated in field and laboratory settings for the detoxification of soils contaminated by petroleum spills, industrial effluents, synthetic dyes, and pharmaceutical residues. Innovations in fungal biotechnology have led to the development of immobilized enzyme systems, genetically enhanced strains, and co-cultivation strategies with bacteria or plants to augment its remediation capacity. Additionally, because P. ostreatus is non-pathogenic and produces edible fruiting bodies under appropriate conditions, its application in agroecological settings provides an added benefit of food or biomass production alongside pollutant degradation. In integrated systems, such as mycofiltration—where fungal mycelium is used to filter water and soil pollutants—P. ostreatus plays a central role due to its dense mycelial network and enzymatic strength. As mycoremediation continues to evolve as a key component of sustainable environmental engineering, Pleurotus ostreatus exemplifies the potential of fungal biology to remediate human-induced ecological damage while contributing to circular bioeconomies.""")
