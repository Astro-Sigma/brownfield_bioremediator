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

st.title("Phanerochaete Chrysosporium, a white-rot fungus")

st.image("https://botit.botany.wisc.edu/toms_fungi/images/pcrassa2.jpg")

st.text("""Phanerochaete chrysosporium is a species of white-rot fungus renowned for its remarkable ligninolytic capabilities. Belonging to the phylum Basidiomycota, this saprophytic organism is primarily found in decaying hardwood forests, where it plays a critical ecological role in the decomposition of lignin, a complex and recalcitrant biopolymer found in plant cell walls. Distinguished by its cottony white mycelium and rapid growth under aerobic conditions, P. chrysosporium has garnered considerable scientific attention for its exceptional enzymatic machinery—particularly its production of lignin peroxidases (LiPs) and manganese peroxidases (MnPs). These extracellular enzymes have the unique ability to degrade not only lignin but also a broad array of structurally complex and environmentally persistent organic pollutants, including polycyclic aromatic hydrocarbons (PAHs), dyes, pesticides, dioxins, and various industrial solvents.

In the realm of bioremediation, Phanerochaete chrysosporium possesses several significant strengths that distinguish it from other microbial agents. Its most prominent advantage lies in its non-specific oxidative enzymatic system, which enables it to mineralize a wide variety of xenobiotic compounds that are otherwise resistant to bacterial degradation. The organism thrives in lignocellulosic substrates, making it well-suited for applications involving plant-based waste materials as bioremediation platforms. Moreover, it operates under aerobic conditions and can be cultivated relatively easily in controlled bioreactors, facilitating its implementation in ex situ remediation strategies. However, there are notable limitations. P. chrysosporium is highly sensitive to environmental conditions such as pH, temperature, and moisture levels, often requiring narrow operating ranges (typically around 37°C and pH 4.5–5.5) for optimal enzyme activity. Additionally, its effectiveness in in situ soil remediation is somewhat constrained by limited mycelial mobility and slower degradation rates in highly contaminated or compacted soils. Furthermore, while effective against organic pollutants, P. chrysosporium is generally ineffective for the removal of inorganic contaminants such as heavy metals, thus necessitating its use in combination with other remediation strategies for mixed-contaminant sites.

Despite these limitations, the potential of Phanerochaete chrysosporium in environmental biotechnology remains vast and largely untapped. Current research efforts are focused on enhancing its robustness and efficacy through genetic engineering, co-cultivation with other microorganisms, and the use of carrier materials such as biochar or immobilized matrices to stabilize its enzymatic systems. Additionally, advances in bioreactor design and process optimization have improved its scalability for industrial applications. The use of this fungus in wastewater treatment, pulp and paper effluent detoxification, and soil remediation demonstrates how nature’s own decomposers can be leveraged to address anthropogenic pollution. In the context of sustainable and eco-friendly remediation technologies, P. chrysosporium exemplifies the power of fungal biodegradation in transforming harmful compounds into benign or less toxic byproducts, thus contributing to the long-term goal of environmental restoration.""")
