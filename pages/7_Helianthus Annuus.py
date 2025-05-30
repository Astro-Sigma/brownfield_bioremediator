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

st.title("Helianthus Annuus, aka the Common Sunflower")

st.image("https://upload.wikimedia.org/wikipedia/commons/4/40/Sunflower_sky_backdrop.jpg", width=200)

st.text("""Helianthus annuus, commonly referred to as the sunflower, is a widely cultivated annual plant belonging to the family Asteraceae. Native to North America, this species is distinguished by its tall stature, broad leaves, and striking composite flower heads, which exhibit heliotropic behavior (i.e., orientation in response to the sun). Beyond its agricultural and ornamental value, H. annuus possesses notable phytoremediative properties, making it an attractive candidate for sustainable environmental management. With a fast growth rate, high biomass yield, and extensive fibrous root system, the sunflower can interact with a broad range of contaminants in the soil and water. Its adaptability to diverse climatic and edaphic conditions further enhances its potential for field-scale application in phytoremediation—the use of plants to extract, stabilize, transform, or degrade environmental pollutants.

In the field of bioremediation, Helianthus annuus exhibits multiple advantages that underscore its utility in phytoremediation, particularly for the remediation of heavy metals and certain organic compounds. One of its most well-documented strengths is its ability to accumulate heavy metals such as lead (Pb), arsenic (As), cadmium (Cd), zinc (Zn), and uranium (U) in its aerial tissues, a process known as phytoextraction. Studies have shown that the species can tolerate and sequester significant concentrations of these metals without exhibiting acute phytotoxicity, especially when grown in mildly to moderately contaminated soils. Furthermore, the sunflower's large root surface area facilitates the uptake and stabilization of pollutants, contributing to phytostabilization in areas prone to erosion or leaching. Additionally, H. annuus produces secondary metabolites and root exudates that can stimulate microbial activity in the rhizosphere, promoting synergistic interactions with rhizobacteria that enhance organic pollutant degradation. However, certain limitations must be acknowledged. The species is generally more effective at remediating shallow soil contaminants and is less suitable for deep-rooted pollution or groundwater remediation. Its metal uptake capacity is finite and may plateau in highly contaminated environments unless aided by soil amendments such as chelating agents (e.g., EDTA). Moreover, the accumulation of toxic metals in the biomass raises concerns about safe disposal or reuse of harvested plant material, especially when large-scale remediation is undertaken. Seasonal growth patterns also limit its application to certain climates, and drought or nutrient-deficient soils can suppress both growth and remediation efficacy.

Despite these constraints, Helianthus annuus remains an exceptionally promising candidate for environmentally conscious remediation strategies due to its multifaceted utility. Beyond pollutant removal, it contributes to soil restoration, biodiversity enhancement, and carbon sequestration. Furthermore, its cultivation is economically viable, as the harvested biomass can be potentially used for biofuel production—though only if contaminants are appropriately managed. Research is ongoing into genetically modified sunflower strains with enhanced metal uptake or broader pollutant specificity, as well as the use of microbial inoculants to amplify phytoremediation capacity. The inclusion of H. annuus in integrated phytoremediation systems, such as vegetative buffer zones and constructed wetlands, exemplifies its role not only as a remediator but also as a catalyst for ecosystem services and sustainable land use. In sum, Helianthus annuus provides a harmonious blend of agronomic utility and ecological functionality, making it a pivotal species in the advancement of plant-based environmental detoxification technologies.""")
