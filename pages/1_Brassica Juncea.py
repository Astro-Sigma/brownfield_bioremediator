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

st.text("""Brassica juncea, commonly known as Indian mustard, is a vigorous annual plant in the Brassicaceae family, widely cultivated for its culinary, agricultural, and industrial significance. Originating from the Indian subcontinent, it thrives in a variety of climates and soil types, displaying remarkable adaptability. Morphologically, the plant is characterized by deeply lobed green leaves, tall erect stems, bright yellow flowers, and seed pods containing pungent mustard seeds, which are frequently processed into edible oils, condiments, and traditional medicines. Due to its rapid growth rate, high biomass yield, and deep root system, B. juncea has also gained recognition as a promising candidate in the field of phytoremediation, particularly for sites contaminated with heavy metals and other toxic elements.

In terms of bioremediation capabilities, Brassica juncea exhibits several pronounced strengths. Foremost among these is its high capacity for phytoextraction, especially of heavy metals such as lead (Pb), cadmium (Cd), chromium (Cr), nickel (Ni), and arsenic (As). The plant's ability to translocate these metals from the rhizosphere into its aerial tissues—without significant inhibition of growth—makes it suitable for repeated harvest and removal cycles. Its short life cycle and ease of cultivation allow for multiple remediation cycles within a single growing season, enhancing its overall effectiveness. Additionally, its extensive root system interacts with rhizospheric microorganisms that can enhance metal solubility and uptake. However, B. juncea is not without limitations. It tends to be less effective in removing organic pollutants such as petroleum hydrocarbons and certain pesticides, which require degradation rather than accumulation. Moreover, while tolerant to moderate levels of contamination, its performance deteriorates in environments with extremely high concentrations of heavy metals, where toxicity can stunt growth and reduce biomass, thereby limiting its remediation potential. Another notable weakness is the requirement for proper post-harvest biomass management, as the metal-laden tissues can become secondary pollutants if not handled correctly.

Nonetheless, Brassica juncea remains a powerful and economically viable tool in sustainable environmental restoration. Advances in genetic engineering and agronomic practices have further enhanced its phytoremediation potential by improving metal tolerance, root exudate composition, and overall biomass production. The integration of this species into remediation strategies not only offers a cost-effective alternative to traditional physicochemical methods but also contributes to the ecological revitalization of degraded lands. In addition, the plant’s compatibility with microbial consortia and soil amendments such as chelators or biochar can further amplify its remediation efficiency. As global attention increasingly shifts toward green technologies and sustainable development, the role of Brassica juncea in phytoremediation stands as a compelling example of how biological systems can be harnessed to mitigate the adverse effects of industrial pollution on ecosystems.""")

st.image("https://upload.wikimedia.org/wikipedia/commons/4/42/Brassica_juncea_-_K%C3%B6hler%E2%80%93s_Medizinal-Pflanzen-168.jpg")
