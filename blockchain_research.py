import time
from firecrawl_client import FirecrawlClient
from openai_agent import ResearchAgent, ElaborationAgent

def conduct_research(topic, depth=3):
    """
    Conduct comprehensive blockchain research on a given topic
    
    Args:
        topic (str): The blockchain research topic
        depth (int): Research depth level (1-5)
        
    Returns:
        dict: Structured research results with different sections
    """
    
    # Initialize the clients
    firecrawl = FirecrawlClient()
    research_agent = ResearchAgent()
    elaboration_agent = ElaborationAgent()
    
    # Step 1: Gather raw data using Firecrawl
    raw_data = firecrawl.explore_blockchain_topic(topic, depth=depth)
    
    # Step 2: Initial synthesis with Research Agent
    initial_analysis = research_agent.analyze(
        topic=topic,
        raw_data=raw_data,
        depth=depth
    )
    
    # Step 3: Elaborate on findings with Elaboration Agent
    elaborate_results = elaboration_agent.elaborate(
        topic=topic, 
        initial_analysis=initial_analysis,
        depth=depth
    )
    
    # Step 4: Organize into structured sections
    research_results = {
        'overview': elaborate_results['overview'],
        'technical_analysis': elaborate_results['technical_analysis'],
        'market_adoption': elaborate_results['market_adoption'],
        'regulatory': elaborate_results['regulatory'],
        'future_outlook': elaborate_results['future_outlook'],
        'references': elaborate_results['references']
    }
    
    return research_results
