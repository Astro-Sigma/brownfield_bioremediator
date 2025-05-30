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

st.title("Typha Latifolia, aka Bulrush")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Typha_latifolia_02_bgiu.jpg/500px-Typha_latifolia_02_bgiu.jpg", width=200)

st.text("""Typha latifolia, commonly known as the broadleaf cattail, is a perennial aquatic macrophyte belonging to the family Typhaceae. Native to temperate and subtropical regions across North America, Europe, Asia, and parts of Africa, it is predominantly found in freshwater marshes, wetlands, lakeshores, and ditches. Recognized for its tall, erect stature—often exceeding two meters—and its distinctive cylindrical brown flowering spikes, T. latifolia is a keystone species in wetland ecosystems. It contributes significantly to sediment stabilization, nutrient cycling, and wildlife habitat provisioning. More importantly, T. latifolia has garnered considerable scientific and environmental interest for its role in phytoremediation, particularly within constructed wetlands and natural wastewater treatment systems. Through a combination of physiological and biochemical mechanisms, this species can absorb, accumulate, or transform a wide spectrum of environmental pollutants, making it an essential component in nature-based remediation strategies.

In the context of bioremediation, Typha latifolia presents several compelling strengths. First, its extensive fibrous root and rhizome system enhances rhizofiltration and rhizodegradation, facilitating both the uptake and microbial degradation of contaminants within the rhizosphere. It is particularly adept at removing nutrients such as nitrogen (in the forms of ammonium and nitrate) and phosphorus, thereby mitigating eutrophication risks. Moreover, it can tolerate and accumulate heavy metals including lead (Pb), cadmium (Cd), zinc (Zn), copper (Cu), and chromium (Cr), often sequestering them in roots and rhizomes to reduce translocation into aerial parts. Its role in promoting microbial communities—especially aerobic and facultative bacteria—in the root zone also enhances the degradation of organic pollutants such as polycyclic aromatic hydrocarbons (PAHs), phenols, and certain pesticides. However, T. latifolia is not without limitations. One major constraint is its dependency on aquatic or semi-aquatic conditions; it is ineffective in arid or upland terrestrial environments. Its metal accumulation ability, while notable, is generally lower compared to hyperaccumulators like Brassica juncea. Furthermore, excessive proliferation can lead to monodominance in wetland ecosystems, displacing native plant diversity and altering hydrological balances. Additionally, the accumulation of pollutants in biomass poses a disposal challenge, particularly in metal-contaminated sites, as incineration or composting can reintroduce contaminants into the environment if not properly managed.

Despite these limitations, Typha latifolia remains a cornerstone species in constructed wetland systems and green infrastructure aimed at pollution control and ecosystem restoration. Its ease of propagation, adaptability to diverse freshwater conditions, and multifunctional ecological roles make it an ideal candidate for low-cost, low-maintenance remediation technologies. It is frequently used in horizontal and vertical flow constructed wetlands for the treatment of municipal, agricultural, and industrial effluents. Recent studies have explored the use of T. latifolia in conjunction with other wetland plants and bioaugmentation strategies to enhance the remediation of emerging contaminants such as pharmaceuticals, endocrine disruptors, and microplastics. Its biomass, if uncontaminated, can also be valorized for bioenergy production, paper manufacturing, or thatching—thus contributing to circular bioeconomy frameworks. As global attention shifts toward sustainable, nature-based solutions for pollution mitigation, Typha latifolia offers a model of how native ecological engineering can support environmental recovery and public health.""")
