# Blockchain Research Assistant

A powerful AI-powered blockchain research assistant built with OpenAI's Agents SDK and Firecrawl, designed to perform deep, structured research across decentralized ecosystems, protocols, trends, and compliance frameworks.

![Blockchain Research](https://pixabay.com/get/gc2f9a73b7a68deb438a63489bcb6e158dea999b063c7ea9c776ca4b7a5077ba0a7af0b40fe62a522fb986018f2e24c67bff49ce73f0c5b374bb3ced58a0e5652_1280.jpg)

## 🧠 Features

- **Protocol-Level Research**: Automatically explores L1/L2 networks, smart contract platforms, DeFi protocols, NFTs, DAOs, and blockchain-specific whitepapers.
- **Firecrawl + OpenAI**: Combines Firecrawl's web scraping and research automation with OpenAI's Agents SDK for layered understanding and commentary.
- **Streamlined UI**: Simple and elegant Streamlit interface tailored for blockchain professionals.
- **Exportable Reports**: Download markdown reports with links, summaries, and elaborated context for easy sharing.

## ⚙️ How It Works

### Input Phase
Enter a blockchain-related research topic and your API credentials (OpenAI + Firecrawl).

### Exploration Phase
Firecrawl scours blockchain-specific domains like GitHub repos, crypto blogs, whitepapers, and technical documentation.

### Synthesis Phase
A Research Agent generates an initial analysis of the findings — covering technical specs, adoption metrics, tokenomics, and roadmap milestones.

### Elaboration Phase
A secondary Elaboration Agent enhances the report by explaining mechanisms, offering case studies (e.g., zk-rollups vs optimistic rollups), and identifying potential regulatory, security, or scaling implications.

### Delivery Phase
The full research dossier is presented in-app and downloadable as a markdown file.

## 🛠️ Requirements

- Python 3.8+
- OpenAI API Key
- Firecrawl API Key
- Required packages listed in requirements.txt

## 📋 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/blockchain-research-assistant.git
cd blockchain-research-assistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## 🚀 Usage

1. Enter your API keys in the sidebar fields:
   - OpenAI API Key
   - Firecrawl API Key

2. Select a research topic (use one of the examples or enter your own)

3. Adjust the research depth slider (1-5)

4. Click "Start Research" and wait for the results

5. Explore the different sections of the research report

6. Download the markdown report for sharing or future reference

## 🧪 Example Blockchain Research Prompts

- "How zkEVMs are reshaping Ethereum scalability"
- "Comparison of Solana and Sui's parallel execution models"
- "Regulatory status of crypto staking in the US and EU"
- "DAO governance attacks and mitigation frameworks"
- "The role of account abstraction in Web3 UX evolution"

## 🧬 Technical Architecture

### Project Structure

```
blockchain-research-assistant/
├── app.py                     # Main Streamlit application
├── blockchain_research.py     # Core research orchestration
├── firecrawl_client.py        # Client for Firecrawl API
├── openai_agent.py            # OpenAI agent implementations
├── utils.py                   # Utility functions
└── .streamlit/
    └── config.toml            # Streamlit configuration
```

### Component Overview

- **Firecrawl Client**: Performs iterative web crawling across crypto-specific knowledge sources including GitHub, Mirror, Medium, Whitepapers, Token Docs, and forums like X/Twitter, Reddit, and Stack Exchange.

- **Research Agent**: Synthesizes protocol details, architecture diagrams, TVL trends, dev activity, and funding data.

- **Elaboration Agent**: Adds economic implications, scalability trade-offs, real-world adoption examples, and compliance insights.

## 📈 Research Output Structure

The research results are structured into the following sections:

1. **Overview**: Executive summary of the research findings
2. **Technical Analysis**: Detailed explanation of technical aspects
3. **Market & Adoption**: Analysis of market position, adoption metrics, and economic implications
4. **Regulatory Considerations**: Regulatory status and compliance frameworks
5. **Future Outlook**: Future potential and development paths
6. **References & Sources**: Key sources and references (formatted as markdown links)

## ⚙️ Configuration

The application can be configured through environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `FIRECRAWL_API_KEY`: Your Firecrawl API key

You can also customize the Streamlit interface through the `.streamlit/config.toml` file.

## 🔒 Security Considerations

- API keys are stored as environment variables and are not persisted
- Research data is processed locally and not stored on external servers
- Downloaded reports contain only the processed research results, not raw data

## 📝 License

[MIT License](LICENSE)

## 🙏 Acknowledgements

- OpenAI for the powerful language models
- Firecrawl for web scraping capabilities
- Streamlit for the intuitive web interface