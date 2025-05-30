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

st.title("Sphingomonas Paucimobilis, a gram-negative bacterium")

st.image("https://onlinelibrary.wiley.com/cms/asset/d10417f3-4313-4bc5-bac8-e3a3d5ed8efc/ccr37715-fig-0002-m.jpg")

st.text("""Sphingomonas paucimobilis is a Gram-negative, rod-shaped, non-spore-forming bacterium belonging to the class Alphaproteobacteria and the family Sphingomonadaceae. Unlike many other Gram-negative bacteria, S. paucimobilis is uniquely characterized by the absence of lipopolysaccharides (LPS) in its outer membrane. Instead, it contains glycosphingolipids, which are believed to confer increased resistance to a range of environmental stresses and antimicrobial agents. This microorganism is aerobic and motile via a single polar flagellum, and it can be isolated from a wide variety of ecological niches, including soil, water systems, clinical settings, and industrial wastewater. Its metabolic versatility and ability to degrade complex organic molecules have established S. paucimobilis as a prominent candidate for use in the bioremediation of contaminated environments, particularly those polluted with xenobiotic and recalcitrant compounds.

In the context of bioremediation, Sphingomonas paucimobilis displays several distinctive strengths. Its most significant attribute is its remarkable capacity to degrade a wide spectrum of persistent organic pollutants, including polycyclic aromatic hydrocarbons (PAHs), chlorinated phenols, polychlorinated biphenyls (PCBs), herbicides, and other toxic aromatic compounds. The bacterium achieves this through an array of oxidative enzymes and catabolic pathways, such as monooxygenases and dioxygenases, which facilitate the initial activation and ring-cleavage of stable aromatic compounds. Additionally, its lack of endotoxins (due to the absence of LPS) makes it a safer organism for certain biotechnological applications, especially in sensitive or populated environments. Furthermore, S. paucimobilis exhibits considerable resistance to oxidative stress, desiccation, and variable pH conditions, allowing it to survive in harsh or nutrient-deficient environments where other microbes may fail. However, there are notable weaknesses. The bacterium often shows slow growth kinetics, especially when metabolizing high-molecular-weight or heavily chlorinated compounds, which may limit the speed of remediation. Its biodegradation efficacy can also be compromised by high concentrations of pollutants that exhibit acute toxicity, and in natural or unamended soils, its survival and metabolic activity may decline due to competition from native microbial communities. Additionally, it is largely ineffective against inorganic pollutants such as heavy metals, thus limiting its standalone application for mixed-waste scenarios.

Nevertheless, Sphingomonas paucimobilis remains a promising organism in the field of microbial bioremediation, especially when incorporated into integrated remediation strategies. Current research is exploring the use of bioaugmentation, genetic modification, and consortium-based approaches to overcome its limitations and enhance its pollutant degradation spectrum and kinetics. For instance, co-cultivation with other microbial species—such as Pseudomonas putida or Rhodococcus spp.—has demonstrated synergistic effects in breaking down complex pollutant mixtures more efficiently than monocultures. Its potential role in bioreactor-based systems for wastewater treatment and soil biopurification beds is also being actively investigated. As the demand for environmentally benign remediation technologies continues to rise, Sphingomonas paucimobilis stands out as a microbial workhorse capable of contributing to the detoxification of some of the most persistent and hazardous anthropogenic compounds, thus playing a key role in advancing sustainable environmental stewardship.""")

