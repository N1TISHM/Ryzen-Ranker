import streamlit as st # type: ignore # ➡️ [UI LAYER] Premium layout components
from data_manager import HardwareDatabase  # ➡️ [UI LAYER] Import pure Python backend data
from ai_engine import LocalInferenceEngine  # ➡️ [UI LAYER] Import local AI connection configuration

# ➡️ [UI LAYER] Connect custom backend modules
db = HardwareDatabase()
ai = LocalInferenceEngine(model_name="qwen2.5:0.5b")

# ➡️ [UI LAYER] Page config with custom dark aesthetic styling elements
st.set_page_config(
    page_title="RyzenRanker AI", 
    page_icon="⚡", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Global CSS Styling to inject sleek, professional telemetry card formats ---
st.markdown("""
<style>
    .metric-card {
        background-color: #1e293b;
        border: 1px solid #334155;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .metric-title {
        color: #94a3b8;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 8px;
    }
    .metric-value {
        color: #f97316;
        font-size: 1.6rem;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# ➡️ [UI LAYER] Clean Header Title Layout
st.title("⚡ RyzenRanker AI")  
st.caption("The Advanced Local Intelligence Engine for Silicon Hierarchy & Value Tracking")  
st.write("") # Strategic padding whitespace

# --- UI Controls Area ---
st.markdown("### 🎯 Hardware Priority Constraints")
col1, col2 = st.columns([1.1, 0.9])  # Proportional width splitting

with col1:
    user_gens = st.multiselect(
        "Target Architectures:",
        options=db.get_unique_generations(),  
        default=db.get_unique_generations(),
        help="Check architectures to compute and rank them dynamically."
    )

with col2:
    budget_ceiling = st.slider(
        "Max Price Cap ($):",
        min_value=100, max_value=700, value=700, step=50  
    )

# ➡️ [UI LAYER] Fetch computed native list data metrics
ranked_list = db.filter_and_rank(user_gens, budget_ceiling)
st.divider()

# --- Visual Insights Area ---
if ranked_list:
    # 🧠 [UI LAYER] FIXED: Dynamically isolate highlight products via zero-index elements
    top_value_chip = ranked_list[0]["Processor"]
    
    # Mathematical computation isolating peak performance from the remaining set
    peak_perf_chip = max(ranked_list, key=lambda x: x["Performance"])["Processor"]
    
    # ➡️ [UI LAYER] Render telemetry dashboard panels
    m1, m2 = st.columns(2)
    with m1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🏆 Top Value Pick</div>
            <div class="metric-value">{top_value_chip}</div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">👑 Peak Performance Pick</div>
            <div class="metric-value">{peak_perf_chip}</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("") # Whitespace padding

    st.markdown("### 📊 Value Distribution Analytics")
    st.scatter_chart(  
        data=ranked_list,
        x="Price",
        y="Performance",
        color="Generation",
        size="Demand",
        use_container_width=True
    )
    
    st.markdown("### 📋 Computed Hierarchy Matrix")
    st.dataframe(
        ranked_list, 
        use_container_width=True,
        column_config={
            "Processor": "Processor Model",
            "Generation": "Architecture",
            "Price": st.column_config.NumberColumn("Retail Price", format="$%d"),
            "Performance": st.column_config.ProgressColumn("Perf Index", min_value=0, max_value=100, format="%d Pts"),
            "Demand": st.column_config.NumberColumn("Popularity", format="%d%%"),
            "Value Score": st.column_config.NumberColumn("Value Index")
        }
    )  
else:
    st.warning("No silicon metrics fall within your selected priority constraints.")

st.divider()

# --- Conversational AI Interface ---
st.markdown("### 💬 Explainable AI Engine")
st.caption("Ask RyzenRanker to justify the active rankings or compare specs.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])  

if prompt := st.chat_input("Ex: Why is the top pick better value than the most expensive one?"):
    with st.chat_message("user"):
        st.markdown(prompt)  
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    with st.chat_message("assistant"):
        with st.spinner("Analyzing active matrix properties..."):  
            ai_response = ai.query_explainer(prompt, ranked_list)  
            st.markdown(ai_response)
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})

with st.chat_message("system"):
    st.markdown(
        " tip: you can clear the chat history by clicking the 'clear chat history' button in top right corner of the chat input box "
        
    )
