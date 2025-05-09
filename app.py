import streamlit as st
import os
import time
from blockchain_research import conduct_research
from utils import download_markdown

# Set page configuration
st.set_page_config(
    page_title="Blockchain Research Assistant",
    page_icon="🔍",
    layout="wide"
)

# Main app title
st.title("🔍 Blockchain Research Assistant")
st.markdown("""
This AI-powered assistant conducts comprehensive research on blockchain technologies, protocols, and trends
using OpenAI's Agents SDK and Firecrawl for deep web exploration.
""")

# Sidebar for configuration
st.sidebar.title("Configuration")

# API Key inputs
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
firecrawl_api_key = st.sidebar.text_input("Firecrawl API Key", type="password")

# Topic input with example prompts
st.sidebar.subheader("Research Topic")
example_prompts = [
    "How zkEVMs are reshaping Ethereum scalability",
    "Comparison of Solana and Sui's parallel execution models",
    "Regulatory status of crypto staking in the US and EU",
    "DAO governance attacks and mitigation frameworks",
    "The role of account abstraction in Web3 UX evolution"
]
selected_prompt = st.sidebar.selectbox("Example Topics (select or enter your own below)", 
                                      [""] + example_prompts)
research_topic = st.sidebar.text_area("Enter your research topic", 
                                      value=selected_prompt if selected_prompt else "")

# Research depth and settings
st.sidebar.subheader("Research Settings")
research_depth = st.sidebar.slider("Research Depth", min_value=1, max_value=5, value=3, 
                                  help="Higher values lead to more comprehensive research but take longer")

# Conduct research button
if st.sidebar.button("Start Research", type="primary", disabled=not (openai_api_key and firecrawl_api_key and research_topic)):
    if not openai_api_key or not firecrawl_api_key:
        st.sidebar.error("Please enter both API keys to proceed.")
    elif not research_topic:
        st.sidebar.error("Please enter a research topic.")
    else:
        # Set API keys as environment variables
        os.environ["OPENAI_API_KEY"] = openai_api_key
        os.environ["FIRECRAWL_API_KEY"] = firecrawl_api_key
        
        # Display blockchain technology images in the main panel
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://pixabay.com/get/g378abe9a7e28ab4586b0b6379761bd2b11525058647d539e783fc22f463158ae391ccc3e2333a1089190600ccec79d11fcbb8d25f99a476661590b47407b54e9_1280.jpg", 
                     caption="Blockchain Technology", use_column_width=True)
        with col2:
            st.image("https://pixabay.com/get/gde86c75ed5d083b1ffe8c0594ab284435c2337a85d79b47b370bf89b504d2e70c539bdeb34bdea252c593e12eb2c56316b124e4e47a510ebcb2575dbe640e3b7_1280.jpg", 
                     caption="Distributed Ledger", use_column_width=True)
        
        # Research progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Research phases
        phases = [
            "Initializing research assistant...",
            "Exploring blockchain sources with Firecrawl...",
            "Synthesizing protocol details and metrics...",
            "Elaborating on technical implications...",
            "Generating comprehensive research report..."
        ]
        
        # Simulate research process with progress updates
        for i, phase in enumerate(phases):
            status_text.text(phase)
            progress_bar.progress((i+1) / len(phases))
            if i < len(phases) - 1:  # Don't sleep after the last phase
                time.sleep(2)  # Simulate processing time
        
        try:
            # Actual research function
            research_results = conduct_research(research_topic, research_depth)
            
            # Reset progress indicators
            progress_bar.progress(100)
            status_text.text("Research completed!")
            
            # Display results
            st.subheader("Research Results: " + research_topic)
            
            # Research overview tab
            with st.expander("📊 Research Overview", expanded=True):
                st.markdown(research_results['overview'])
                st.image("https://pixabay.com/get/g99ac5c6150f0c9bd1c6c451a2891c8c6eea30bde5c48035a73f7c5978917c50a08c06cab171797999552c5f554624d8479e93ebc95763c54b2cc62d82710c2a5_1280.jpg", 
                          caption="Cryptocurrency Research", use_column_width=True)
            
            # Technical analysis tab
            with st.expander("🔬 Technical Analysis"):
                st.markdown(research_results['technical_analysis'])
            
            # Market and adoption tab
            with st.expander("📈 Market & Adoption"):
                st.markdown(research_results['market_adoption'])
                st.image("https://pixabay.com/get/g2e2bfdc7f83ef21e9dce6587bf99709225cbf501a48fef1797462867b5b7e2bed677056788685a17d310800ce2dc24c299213ec701b4cbcf5f3f9896c3ecfc61_1280.jpg", 
                         caption="Data Analysis Dashboard", use_column_width=True)
            
            # Regulatory considerations tab
            with st.expander("⚖️ Regulatory Considerations"):
                st.markdown(research_results['regulatory'])
            
            # Future outlook tab
            with st.expander("🔮 Future Outlook"):
                st.markdown(research_results['future_outlook'])
            
            # References tab
            with st.expander("📚 References & Sources"):
                st.markdown(research_results['references'])
            
            # Download button for the report
            full_report = "\n\n".join([
                f"# {research_topic} - Blockchain Research Report\n",
                "## Overview\n" + research_results['overview'],
                "## Technical Analysis\n" + research_results['technical_analysis'],
                "## Market & Adoption\n" + research_results['market_adoption'],
                "## Regulatory Considerations\n" + research_results['regulatory'],
                "## Future Outlook\n" + research_results['future_outlook'],
                "## References & Sources\n" + research_results['references']
            ])
            
            st.download_button(
                label="📥 Download Research Report",
                data=full_report,
                file_name=f"blockchain_research_{research_topic.replace(' ', '_')}.md",
                mime="text/markdown",
            )
            
        except Exception as e:
            st.error(f"Research process encountered an error: {str(e)}")
            st.sidebar.error("Please check your API keys and try again.")

# Footer info
st.sidebar.markdown("---")
st.sidebar.caption("Powered by OpenAI Agents SDK & Firecrawl")
st.sidebar.caption("© 2023 Blockchain Research Assistant")

# When no research is being conducted, show some information about the tool
if 'research_results' not in locals():
    st.subheader("How the Blockchain Research Assistant Works")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://pixabay.com/get/gc2f9a73b7a68deb438a63489bcb6e158dea999b063c7ea9c776ca4b7a5077ba0a7af0b40fe62a522fb986018f2e24c67bff49ce73f0c5b374bb3ced58a0e5652_1280.jpg", 
                 caption="Blockchain Technology", use_column_width=True)
    with col2:
        st.image("https://pixabay.com/get/gbea16d4da049780da4dfe10feab50035188c6c0f1a2ee40c019ba50b84f7e2257b35d061a009a7448ff6e5c7a135afabd1cebc682673614d906289eb88e7b825_1280.jpg", 
                 caption="Cryptocurrency Research", use_column_width=True)
    
    st.markdown("""
    ### ⚙️ How It Works
    
    #### Input Phase
    Enter a blockchain-related research topic and your API credentials (OpenAI + Firecrawl).
    
    #### Exploration Phase
    Firecrawl scours blockchain-specific domains like GitHub repos, crypto blogs, whitepapers, and technical documentation.
    
    #### Synthesis Phase
    A Research Agent generates an initial analysis of the findings — covering technical specs, adoption metrics, tokenomics, and roadmap milestones.
    
    #### Elaboration Phase
    A secondary Elaboration Agent enhances the report by explaining mechanisms, offering case studies, and identifying potential regulatory, security, or scaling implications.
    
    #### Delivery Phase
    The full research dossier is presented in-app and downloadable as a markdown file.
    """)
    
    st.markdown("### 🧪 Example Blockchain Research Prompts")
    for prompt in example_prompts:
        st.markdown(f"- {prompt}")
