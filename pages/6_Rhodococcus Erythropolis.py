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

st.title("Rhodococcus Erythropolis, an aerobic actinobacterium")

st.image("https://cdn.dsmz.de/images/strain/10853/DSM_743.jpg", width=200)

st.text("""Rhodococcus erythropolis is a Gram-positive, non-sporulating, non-motile, aerobic actinobacterium belonging to the genus Rhodococcus within the family Nocardiaceae. It is characterized by its robust, coccoid to rod-shaped morphology and a high G+C content in its genomic DNA, typically around 60–70%. R. erythropolis is commonly found in soil, marine sediments, and contaminated industrial sites due to its extraordinary metabolic versatility. The cell wall contains mycolic acids, a feature that contributes to its resilience against harsh chemical environments. Of particular interest to environmental microbiologists and biotechnologists is R. erythropolis’s extensive catabolic potential, enabling it to degrade a wide array of hydrocarbons and xenobiotic compounds. Because of its broad enzymatic toolkit—including oxygenases, hydrolases, and dehalogenases—this bacterium is increasingly recognized as a cornerstone species in the microbial remediation of complex organic pollutants.

In the context of bioremediation, Rhodococcus erythropolis possesses several critical strengths that make it uniquely valuable. One of its foremost advantages is its unparalleled ability to degrade hydrophobic and structurally complex organic pollutants, including petroleum hydrocarbons, chlorinated solvents, polycyclic aromatic hydrocarbons (PAHs), polychlorinated biphenyls (PCBs), nitriles, and various synthetic detergents. This capacity is largely attributed to the production of biosurfactants, which enhance the solubility and bioavailability of hydrophobic compounds, as well as the presence of multiple oxygenase systems that initiate degradation. Additionally, R. erythropolis exhibits high resistance to toxic compounds and environmental stressors such as desiccation, UV radiation, and osmotic pressure—factors that often inhibit the survival of less hardy bacteria in contaminated sites. Its genomic plasticity and ability to host plasmids also support horizontal gene transfer, enabling the acquisition and optimization of catabolic traits. However, the species is not without weaknesses. It tends to grow more slowly than many Gram-negative bioremediators (e.g., Pseudomonas putida), potentially delaying the overall remediation timeline. Moreover, its effectiveness may decline in anaerobic environments, as it primarily functions under aerobic conditions. Another constraint is the limited commercial availability of well-characterized and standardized R. erythropolis strains for field-scale deployment, which may hinder its widespread application outside of research and pilot projects.

Despite these challenges, Rhodococcus erythropolis remains a highly promising candidate for advanced and sustainable environmental remediation strategies. Modern biotechnological approaches, including metabolic engineering, synthetic biology, and immobilization techniques, are being employed to enhance its degradation kinetics and adaptability. Co-cultivation with other microbial species or consortia can further amplify its remediation potential by creating synergistic metabolic networks. For instance, pairing R. erythropolis with metal-tolerant strains can be effective in treating co-contaminated sites with both organic pollutants and heavy metals. Additionally, its integration into bioreactor systems, biofilters, and biobarriers has proven useful for industrial wastewater treatment and soil decontamination. As the global imperative for green and cost-effective remediation intensifies, Rhodococcus erythropolis exemplifies how microbial ingenuity can be mobilized to mitigate the enduring impacts of industrial pollution while contributing to ecological restoration and public health protection.""")
