import streamlit as st
import base64

def download_markdown(markdown_content, filename="research_report.md"):
    """
    Generate a download link for markdown content
    
    Args:
        markdown_content (str): The markdown content to download
        filename (str): The filename for the downloaded file
        
    Returns:
        str: HTML for the download link
    """
    b64 = base64.b64encode(markdown_content.encode()).decode()
    href = f'<a href="data:file/markdown;base64,{b64}" download="{filename}">Download Markdown File</a>'
    return href

def format_research_results(results):
    """
    Format research results for display
    
    Args:
        results (dict): The research results dictionary
        
    Returns:
        str: Formatted markdown text
    """
    formatted_text = f"""
    # Research Results
    
    ## Overview
    {results.get('overview', 'No overview available')}
    
    ## Technical Analysis
    {results.get('technical_analysis', 'No technical analysis available')}
    
    ## Market & Adoption
    {results.get('market_adoption', 'No market adoption data available')}
    
    ## Regulatory Considerations
    {results.get('regulatory', 'No regulatory information available')}
    
    ## Future Outlook
    {results.get('future_outlook', 'No future outlook available')}
    
    ## References & Sources
    {results.get('references', 'No references available')}
    """
    
    return formatted_text
