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

st.title("Bacillus Subtilis, an endospore-forming bacterium")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Bacillus_subtilis.jpg/1200px-Bacillus_subtilis.jpg", width=200)

st.text("""Bacillus subtilis is a Gram-positive, rod-shaped, endospore-forming bacterium that belongs to the genus Bacillus within the phylum Firmicutes. It is a ubiquitous soil microorganism, widely recognized for its robustness, metabolic versatility, and resilience to environmental stressors such as heat, desiccation, and ultraviolet radiation, largely due to its ability to form dormant, highly resistant spores. This facultative anaerobe thrives in diverse environments ranging from agricultural soils to compost heaps and industrial settings. As a model organism in microbiology and biotechnology, B. subtilis has been extensively studied for its capacity to produce a variety of extracellular enzymes, antimicrobial compounds, and bioactive metabolites. These traits underpin its growing application in environmental biotechnology, particularly in bioremediation, where it contributes to the detoxification and transformation of pollutants through enzymatic degradation, biosurfactant production, and biofilm formation.

From a bioremediation perspective, Bacillus subtilis presents several strengths that make it a valuable agent in the breakdown and stabilization of environmental contaminants. It synthesizes a broad spectrum of hydrolytic enzymes—such as proteases, lipases, cellulases, and amylases—that enable the degradation of complex organic pollutants including hydrocarbons, pesticides, and industrial dyes. Its ability to produce biosurfactants, such as surfactin, enhances the bioavailability of hydrophobic contaminants by reducing surface tension and emulsifying hydrocarbons, thus facilitating their microbial degradation. Additionally, B. subtilis is known for forming resilient biofilms that can colonize contaminated surfaces and sustain microbial consortia, improving pollutant degradation efficiency through synergistic interactions. The bacterium can also participate in the bioprecipitation and biosorption of heavy metals, contributing to the immobilization of metals such as cadmium (Cd), lead (Pb), and chromium (Cr) in polluted soils and wastewater. However, certain limitations affect its practical application. B. subtilis is primarily aerobic, thus its bioremediation activity diminishes under strict anaerobic or heavily reduced conditions commonly found in some polluted environments. Moreover, although it produces a range of degradative enzymes, its effectiveness may be limited when pollutants occur in complex mixtures or at very high concentrations. The scalability of B. subtilis-based treatments also requires optimization, as environmental factors such as pH, temperature, and nutrient availability critically influence its bioremediation performance.

Despite these challenges, Bacillus subtilis remains a promising candidate for incorporation into integrated bioremediation systems and sustainable environmental management strategies. Its non-pathogenic status and Generally Recognized As Safe (GRAS) designation facilitate regulatory approval for use in agricultural and industrial applications. Advances in genetic engineering and synthetic biology have enabled the development of B. subtilis strains with enhanced catabolic pathways tailored for specific pollutants, improving degradation rates and substrate specificity. Furthermore, its use in bioaugmentation—where microbial inoculants are introduced to contaminated sites—has shown positive results in the treatment of soils contaminated by petroleum hydrocarbons, chlorinated solvents, and heavy metals. Combined with phytoremediation or fungal bioremediation, B. subtilis can form part of synergistic consortia that amplify the overall efficiency of pollutant removal. As the global imperative for environmentally benign and cost-effective remediation technologies intensifies, Bacillus subtilis exemplifies the intersection of microbiological robustness and biotechnological innovation, contributing significantly to the restoration of polluted ecosystems and the protection of human health.""")
