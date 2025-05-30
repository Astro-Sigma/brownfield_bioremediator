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

st.title("Pseudomonas Putida, a flagellated bacterium")

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc5OZ9EJVVHasjvemZxNMk15s_nHTkM7i0Lw&s", width=200)

st.text("""Pseudomonas putida is a Gram-negative, rod-shaped, flagellated bacterium belonging to the class Gammaproteobacteria and the family Pseudomonadaceae. It is commonly found in soil, water, and rhizosphere environments and is well-known for its metabolic versatility, robust growth in diverse ecological conditions, and relatively fast reproduction rates. Unlike many bacteria with more narrow ecological functions, P. putida has been extensively studied for its ability to metabolize a wide range of organic substrates, including xenobiotic compounds that are otherwise recalcitrant to biodegradation. It serves as a model organism for systems biology and environmental microbiology, particularly in the fields of metabolic engineering, synthetic biology, and bioremediation. Owing to its non-pathogenicity and generally regarded as safe (GRAS) status, P. putida is also a preferred chassis for biotechnological applications, including bioaugmentation and wastewater treatment.

In terms of bioremediation, Pseudomonas putida is renowned for its formidable arsenal of degradative enzymes and catabolic pathways, which enable it to break down a wide variety of environmental pollutants. These include hydrocarbons such as toluene, benzene, xylene, naphthalene, phenol, and even complex solvents like trichloroethylene. One of its key strengths is the possession of plasmid-encoded metabolic operons, such as the TOL plasmid, which encodes enzymes for the oxidative catabolism of aromatic hydrocarbons. Moreover, P. putida demonstrates high tolerance to oxidative stress and toxic compounds, which allows it to function in environments where many other microbes may perish. Its ability to form biofilms and colonize contaminated surfaces further enhances its effectiveness in both in situ and ex situ applications. However, certain weaknesses are associated with its use in bioremediation. Although it can tolerate many stressors, extreme pH levels, heavy metal toxicity, or anoxic conditions can inhibit its growth and metabolic functions. Furthermore, the presence of competing microbial species in natural environments may reduce its efficiency unless supported by nutrient amendments or introduced as part of a microbial consortium. In addition, while it is adept at degrading many organic pollutants, it has limited capabilities for directly removing inorganic contaminants such as heavy metals, unless genetically engineered or paired with metal-chelating strategies.

Despite these limitations, Pseudomonas putida remains one of the most promising and versatile microbial agents for sustainable environmental remediation. Its genetic malleability makes it an ideal candidate for synthetic biology approaches aimed at expanding its catabolic range or enhancing its environmental resilience. For instance, engineered strains of P. putida have been developed to remediate mixed-waste sites containing both organic pollutants and heavy metals by introducing genes for metal-binding proteins or enhanced transporter systems. In addition, its compatibility with rhizosphere environments allows it to be used in tandem with phytoremediation strategies, whereby the bacterium colonizes plant roots and aids in the degradation of soil pollutants. As biotechnological tools continue to evolve, the deployment of Pseudomonas putida in bioreactors, biopurification systems, and soil bioaugmentation programs is expected to expand, offering a powerful and environmentally friendly alternative to chemical and mechanical remediation techniques.""")
