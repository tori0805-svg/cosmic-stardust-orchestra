import streamlit as st
from crewai import Agent, Task, Crew
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Cosmic Stardust Orchestra", layout="wide")

# COSMIC THEME
st.markdown("""
<style>
.stApp {
    background: linear-gradient(140deg, #00FFFF 8%, #E6E6FA 30%, #C0C0C0 70%),
                url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=1920&q=90') center/cover no-repeat fixed;
    color: white;
}
.stButton>button {
    background: #FF1493; color: white; border-radius: 12px; padding: 0.8rem 1.5rem; font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("🌌 Cosmic Stardust Orchestra")
st.caption("Your complete AI Orchestra Builder & Trainer – 100% cloud, zero install")

# Your agents from the blueprint
data_fetcher = Agent(
    role="Data Fetcher",
    goal="Get and clean any data",
    backstory="Expert at perfect data retrieval",
    allow_delegation=False,
    verbose=True
)

analyst = Agent(
    role="Insight Analyst",
    goal="Turn data into brilliant insights",
    backstory="Master pattern hunter and summarizer",
    allow_delegation=False,
    verbose=True
)

if st.button("🎼 Run Full Orchestra Pipeline", type="primary"):
    with st.spinner("Conducting the orchestra…"):
        task1 = Task(description="Fetch and clean sample data", expected_output="Clean dataset", agent=data_fetcher)
        task2 = Task(description="Deep analysis and beautiful summary", expected_output="Insight report", agent=analyst)

        crew = Crew(agents=[data_fetcher, analyst], tasks=[task1, task2], verbose=2)
        result = crew.kickoff()

    st.success("Performance complete!")
    st.markdown("### Final Report")
    st.write(result)

st.info("Ready for your 32 bonus tools, Supabase, custom models, etc. Just add more .py files – auto-reloads!")
