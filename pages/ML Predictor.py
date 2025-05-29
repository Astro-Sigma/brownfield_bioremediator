import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import json
import streamlit.components.v1 as components

# -------- Define lists --------
toxic_compounds = [
    "TPH", "Gasoline", "Diesel", "Jet Fuel", "Motor Oil", "Heating Oil",
    "Lubricants", "PAHs", "Benzo[a]pyrene", "Naphthalene", "Anthracene",
    "Phenanthrene", "Fluoranthene", "Pyrene", "Chrysene", "VOCs",
    "TCE", "PCE", "Benzene", "Toluene", "Ethylbenzene", "BTEX",
    "Vinyl Chloride", "Methylene Chloride", "Chloroform", "SVOCs",
    "Phenols", "Anilines", "Phthalates", "PCBs", "DDT", "Atrazine",
    "Alachlor", "Lindane", "Chlordane", "Parathion", "2,4-D", "2,4,5-T",
    "Glyphosate", "Cresols", "Quinoline", "Lead", "Cadmium", "Chromium",
    "Arsenic", "Mercury", "Nickel", "Zinc", "Copper", "Selenium", "Manganese",
    "Barium", "Uranium", "Cesium-137", "Strontium-90", "Radon", "Plutonium",
    "Antibiotics", "Hormones", "Antidepressants", "Analgesics", "PFOS", "PFOA",
    "BPA", "PBDEs"
]

soil_types = [
    "sandy_loam", "loamy", "clay_loam", "well-drained", "sandy", "clay",
    "silty", "peaty", "chalky"
]

soil_moisture = [
    "low", "medium", "high"
]


# -------- Load or Train Model --------
@st.cache_resource
def train_or_load_model():
    # Simulated training data
    data_pd = pd.DataFrame(json.load(open(r"C:\Users\gianh\PycharmProjects\ScienceFairProject"
                                          r"\balanced_brownfield_dataset.json", 'r')))

    # Fill in missing compound columns (simulate full list)
    for comp in toxic_compounds:
        if comp not in data_pd.columns:
            data_pd[comp] = 0

    data_pd['pH'] = data_pd.get('pH', 6.5)  # default if missing
    data_pd['max_spend'] = data_pd.get('cost_per_cubic_yard', 50.0)
    # data.rename(columns={"cost_per_cubic_yard": "max_spend"}, inplace=True)
    data_pd.drop(columns=['cost_per_cubic_yard'], inplace=True, errors='ignore')
    data_encoded = pd.get_dummies(data_pd, columns=["soil_type", "moisture"])
    # data_encoded = data_encoded.rename(columns={"cost_per_cubic_yard": "max_spend"})
    x = data_encoded.drop("bioremediator", axis=1)
    y = data_encoded["bioremediator"]
    model_pd = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model_pd.fit(x, y)
    return model_pd, x.columns, y.value_counts()


model, feature_columns, label_distribution = train_or_load_model()

# -------- Streamlit UI --------
st.title("🧪 Bioremediator Recommender for Brownfields 🧪")

st.markdown("Please input all known environmental and ecological data below:")

st.markdown( """<style>@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap'); 

html, body, [class*="css"] {
    font-family: 'Roboto', sans-serif; 
    font-size: 12px;
    font-weight: 500;
    color: #091747;
}</style>""", unsafe_allow_html= True)

# Toxic compound checklist
selected_compounds = st.multiselect(
    "Toxic Compounds Detected",
    options=toxic_compounds,
    default=[]
)

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

# Other site properties
pH = st.slider("Soil pH", min_value=3.5, max_value=10.0, value=6.5, step=0.01)
soil_type = st.selectbox("Soil Type", soil_types)
moisture = st.selectbox("Soil Moisture", soil_moisture)
max_spend = st.slider("Cost Per Cubic Yard", min_value=0.0, max_value=150.0, value=100.0, step=0.1)

if st.button("Recommend Bioremediator"):
    # Convert selected compounds into binary features
    compound_dict = {comp: (1 if comp in selected_compounds else 0) for comp in toxic_compounds}

    # Add other features
    input_dict = {
        **compound_dict,
        "pH": pH,
        "soil_type": soil_type,
        "moisture": moisture,
        "max_spend": max_spend
    }

    input_df = pd.DataFrame([input_dict])

    # One-hot encode only soil_type and moisture columns
    input_encoded = input_df.copy()

    # Apply get_dummies only on categorical columns
    categorical_cols = ["soil_type", "moisture"]
    input_encoded = pd.concat([
        input_encoded.drop(columns=categorical_cols),
        pd.get_dummies(input_encoded[categorical_cols])
    ], axis=1)

    # Reindex columns to match training feature columns
    input_encoded = input_encoded.reindex(columns=feature_columns, fill_value=0)

    # Predict
    prediction = model.predict(input_encoded)[0]
    st.success(f"🌱 Recommended bioremediator: **{prediction}**")

    import eli5
    from eli5.sklearn import PermutationImportance

    # Show prediction explanation
    st.subheader("🧬 Feature Contribution Explanation (via ELI5)")

    # Use ELI5 to explain prediction
    from eli5 import format_as_dataframe

    explanation = eli5.explain_prediction_sklearn(model,
    input_encoded.iloc[0],
    feature_names=input_encoded.columns.tolist())

    #explanation_df = format_as_dataframe(explanation)

    # Clean output DataFrame
    #top_explanations = explanation_df[["feature", "weight"]].copy()
    #top_explanations = top_explanations[top_explanations["weight"] != 0].sort_values(by="weight", ascending=False)

    # Display in Streamlit
    #st.dataframe(top_explanations.head(20).reset_index(drop=True))

    # Optional: horizontal bar plot
    #fig, ax = plt.subplots(figsize=(10, 6))
    #ax.barh(top_explanations["feature"][::-1], top_explanations["weight"][::-1], color='cornflowerblue')
    #ax.set_title("Top Features Influencing Prediction")
    #ax.set_xlabel("Contribution (positive or negative)")
    #st.pyplot(fig)

    html_explanation = eli5.format_as_html(explanation)
    html_with_style = f"""
    <style>
        body, .eli5, .eli5 * {{
            color: white !important;
            background-color: transparent !important;  /* Optional: keep transparent background */
        }}
    </style>
    {html_explanation}
    """
    components.html(html_explanation, height=600, scrolling=True)
