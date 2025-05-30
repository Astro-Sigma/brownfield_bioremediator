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

st.title("Populus Deltoides, aka Eastern Cottonwood")

st.image("https://newfs.s3.amazonaws.com/taxon-images-1000s1000/Salicaceae/populus-deltoides-fr-atal.jpg", width=200)

st.text("""Populus deltoides, commonly referred to as the Eastern cottonwood, is a fast-growing, deciduous tree species native to North America. It belongs to the family Salicaceae, which also includes willows (Salix spp.), and is one of the most prominent members of the Populus genus. Characterized by its triangular (deltoid) leaves, deeply furrowed bark, and cotton-like seeds, P. deltoides can reach heights of over 30 meters in optimal conditions. This species thrives in riparian zones, floodplains, and moist soils, making it well-adapted to dynamic, water-rich environments. Due to its rapid growth, extensive root system, and high transpiration rates, Populus deltoides has been widely planted for use in bioenergy, afforestation, erosion control, and most notably, phytoremediation—the use of plants to mitigate soil, sediment, and groundwater contamination.

In the context of bioremediation, Populus deltoides offers a robust suite of strengths that make it an ideal candidate for both in situ and ex situ remediation strategies. Most significantly, its deep, fibrous root system enhances access to contaminants located in the vadose zone or shallow groundwater. This species is capable of removing a broad range of pollutants through several mechanisms, including phytoextraction (uptake and sequestration of heavy metals), phytostabilization (reduction of contaminant mobility), and phytodegradation (metabolic breakdown of organic pollutants). It is particularly effective against chlorinated solvents such as trichloroethylene (TCE), as well as nitrates, pesticides, petroleum hydrocarbons, and certain heavy metals like zinc, lead, and cadmium. Furthermore, P. deltoides supports a rhizosphere rich in microbial life, enhancing synergistic interactions that accelerate the degradation of organic contaminants. However, there are also important limitations. The tree’s efficacy is restricted to shallow contamination zones (typically less than 10 feet deep), and its performance declines in arid, saline, or nutrient-poor soils. Additionally, the long lifespan and seasonal dormancy of deciduous trees limit their year-round effectiveness. The accumulation of heavy metals in biomass can also pose challenges for biomass disposal and long-term ecological safety if not properly managed.

Nevertheless, the utility of Populus deltoides in environmental remediation is considerable, particularly when integrated into multi-tiered green remediation systems. Its compatibility with microbial bioaugmentation, mycorrhizal fungi, and engineered rhizosphere amendments make it a valuable component in holistic restoration strategies. Hybrid varieties and transgenic lines have also been developed to enhance metal tolerance, pollutant uptake rates, and enzymatic degradation pathways. Moreover, due to its aesthetic and ecological benefits—such as providing habitat, shade, and carbon sequestration—P. deltoides has been used in phytoremediation projects that double as urban greening and ecosystem rehabilitation initiatives. Its deployment in buffer strips, vegetative filter systems, and constructed wetlands exemplifies how phytoremediation can align ecological restoration with pollutant removal objectives. As concerns over environmental degradation intensify, the role of Populus deltoides as a phytoremediator will likely continue to expand, solidifying its place in sustainable land management and pollution mitigation strategies.""")
