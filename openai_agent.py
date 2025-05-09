import os
import json
from openai import OpenAI

class ResearchAgent:
    """
    Agent that uses OpenAI to synthesize raw blockchain research data
    """
    
    def __init__(self):
        """Initialize the ResearchAgent with OpenAI API"""
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.client = OpenAI(api_key=self.api_key)
        # The newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # Do not change this unless explicitly requested by the user
        self.model = "gpt-4o"
    
    def analyze(self, topic, raw_data, depth=3):
        """
        Analyze raw blockchain data to create initial research synthesis
        
        Args:
            topic (str): The blockchain research topic
            raw_data (dict): Raw data from Firecrawl
            depth (int): Research depth (1-5)
            
        Returns:
            dict: Initial analysis of the blockchain topic
        """
        if not self.api_key:
            raise ValueError("OpenAI API key is required")
        
        # Extract content from raw data
        content_list = []
        if "raw_data" in raw_data and isinstance(raw_data["raw_data"], list):
            for item in raw_data["raw_data"]:
                if "content" in item:
                    content_list.append(item["content"])
        
        # Join content with source information
        research_content = "\n\n".join(content_list)
        
        # Create system message for the research agent
        system_message = """
        You are a specialized blockchain research agent with expertise in cryptocurrency, 
        distributed ledger technology, smart contracts, DeFi, and Web3 ecosystems.
        
        Analyze the provided blockchain research data and synthesize it into a comprehensive 
        initial analysis with the following components:
        
        1. Technical specifications and architecture
        2. Adoption metrics and market position
        3. Tokenomics (if applicable)
        4. Development roadmap and milestones
        5. Key stakeholders and contributors
        
        Provide factual, technically accurate information based solely on the data provided.
        If certain information is missing, acknowledge the gaps rather than making assumptions.
        Structure your response as JSON with the following sections: 
        {
            "technical_specs": "...",
            "adoption_metrics": "...",
            "tokenomics": "...",
            "roadmap": "...",
            "stakeholders": "...",
            "key_findings": "..."
        }
        """
        
        # Create the prompt for analysis
        analysis_prompt = f"""
        Research Topic: {topic}
        
        Research Depth: {depth}/5
        
        Raw Research Data:
        {research_content[:15000]}  # Limit content to avoid token limits
        
        Based on this data, provide a detailed initial analysis following the structure specified.
        """
        
        try:
            # Call OpenAI API for analysis
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": analysis_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.1
            )
            
            # Parse the response
            analysis_text = response.choices[0].message.content
            analysis_json = json.loads(analysis_text)
            
            return analysis_json
            
        except Exception as e:
            raise Exception(f"Error analyzing blockchain data: {str(e)}")


class ElaborationAgent:
    """
    Agent that elaborates on initial blockchain research findings
    """
    
    def __init__(self):
        """Initialize the ElaborationAgent with OpenAI API"""
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.client = OpenAI(api_key=self.api_key)
        # The newest OpenAI model is "gpt-4o" which was released May 13, 2024.
        # Do not change this unless explicitly requested by the user
        self.model = "gpt-4o"
    
    def elaborate(self, topic, initial_analysis, depth=3):
        """
        Elaborate on initial findings to create comprehensive research report
        
        Args:
            topic (str): The blockchain research topic
            initial_analysis (dict): Initial analysis from ResearchAgent
            depth (int): Research depth (1-5)
            
        Returns:
            dict: Elaborated research results with different sections
        """
        if not self.api_key:
            raise ValueError("OpenAI API key is required")
        
        # Convert initial analysis to string format for the prompt
        initial_analysis_str = json.dumps(initial_analysis, indent=2)
        
        # Create system message for the elaboration agent
        system_message = """
        You are a specialized blockchain elaboration agent with expertise in explaining complex
        blockchain concepts, mechanisms, and implications. Your task is to take an initial blockchain
        research analysis and elaborate it into a comprehensive, well-structured report with depth
        and nuance.
        
        Your elaboration should:
        1. Explain technical mechanisms in clear, accessible terms
        2. Provide relevant case studies or comparisons
        3. Identify regulatory, security, or scaling implications
        4. Analyze economic and market impacts
        5. Discuss future potential and development paths
        
        Structure your response as JSON with the following sections:
        {
            "overview": "Executive summary of the research findings",
            "technical_analysis": "Detailed explanation of technical aspects",
            "market_adoption": "Analysis of market position, adoption metrics, and economic implications",
            "regulatory": "Regulatory considerations and compliance frameworks",
            "future_outlook": "Future potential and development paths",
            "references": "Key sources and references (formatted as markdown links)"
        }
        
        Each section should be comprehensive and formatted in markdown for readability.
        """
        
        # Create the prompt for elaboration
        elaboration_prompt = f"""
        Research Topic: {topic}
        
        Research Depth: {depth}/5
        
        Initial Analysis:
        {initial_analysis_str}
        
        Please elaborate on this initial analysis to create a comprehensive blockchain research report
        following the structure specified. Focus on depth, clarity, and actionable insights.
        """
        
        try:
            # Call OpenAI API for elaboration
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": elaboration_prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.2
            )
            
            # Parse the response
            elaboration_text = response.choices[0].message.content
            elaboration_json = json.loads(elaboration_text)
            
            return elaboration_json
            
        except Exception as e:
            raise Exception(f"Error elaborating on blockchain research: {str(e)}")
