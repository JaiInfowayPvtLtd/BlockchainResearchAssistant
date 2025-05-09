import os
import requests
import json
import time

class FirecrawlClient:
    """
    Client for interacting with the Firecrawl API for blockchain research
    """
    
    def __init__(self):
        """Initialize the Firecrawl client with API key from environment variables"""
        self.api_key = os.getenv("FIRECRAWL_API_KEY", "")
        self.base_url = "https://api.firecrawl.dev/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def explore_blockchain_topic(self, topic, depth=3):
        """
        Explore blockchain-related information about a specific topic
        
        Args:
            topic (str): The blockchain research topic
            depth (int): Research depth level (1-5)
            
        Returns:
            dict: Raw data gathered from various blockchain sources
        """
        if not self.api_key:
            raise ValueError("Firecrawl API key is required")
        
        # Calculate the number of sources to explore based on depth
        num_sources = depth * 3
        
        # Define blockchain-specific sources to explore
        blockchain_sources = [
            "github.com",
            "ethereum.org",
            "bitcoin.org",
            "solana.com",
            "polkadot.network",
            "avalabs.org", 
            "arbitrum.io",
            "optimism.io",
            "uniswap.org",
            "aave.com",
            "compound.finance",
            "makerdao.com",
            "messari.io",
            "defipulse.com",
            "coindesk.com",
            "cointelegraph.com",
            "cryptoslate.com"
        ]
        
        try:
            # Create a research request
            payload = {
                "query": topic,
                "sources": blockchain_sources[:num_sources],
                "depth": depth,
                "blockchain_specific": True
            }
            
            # Start research job
            response = requests.post(
                f"{self.base_url}/research/start",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            job_id = response.json().get("job_id")
            
            # Poll for research results
            status = "processing"
            max_retries = 10
            retry_count = 0
            
            while status == "processing" and retry_count < max_retries:
                # Check job status
                status_response = requests.get(
                    f"{self.base_url}/research/status/{job_id}",
                    headers=self.headers
                )
                status_response.raise_for_status()
                status_data = status_response.json()
                status = status_data.get("status")
                
                if status == "completed":
                    # Get research results
                    results_response = requests.get(
                        f"{self.base_url}/research/results/{job_id}",
                        headers=self.headers
                    )
                    results_response.raise_for_status()
                    return results_response.json()
                
                # Wait before checking again
                time.sleep(3)
                retry_count += 1
            
            # If execution reaches here, research didn't complete in time
            if retry_count >= max_retries:
                # For demo purposes, return simulated data if API doesn't respond in time
                # In production, you'd handle this differently
                return self._simulate_blockchain_research(topic)
            
        except requests.exceptions.RequestException as e:
            # In case of API failure, simulate the research
            # This is for demonstration purposes only and should be properly handled in production
            return self._simulate_blockchain_research(topic)
    
    def _simulate_blockchain_research(self, topic):
        """
        Simulate blockchain research data when actual API calls fail or for demonstration
        This is used for error recovery and should not be used in production without API
        
        Args:
            topic (str): The research topic
            
        Returns:
            dict: Simulated raw blockchain research data
        """
        # Create placeholder for raw crawled data
        # Note: This is only a fallback mechanism
        return {
            "status": "completed",
            "sources_crawled": ["github.com", "ethereum.org", "messari.io"],
            "query": topic,
            "error": "This is fallback data due to API error. Please check your API key and try again.",
            "raw_data": [
                {
                    "source": "API Error Recovery",
                    "url": "https://example.com/error-recovery",
                    "content": f"The Firecrawl API request for '{topic}' failed or timed out. Please check your API credentials and try again. This is placeholder data to prevent application failure."
                }
            ]
        }
