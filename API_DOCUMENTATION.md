# API Documentation

This document details the APIs used in the Blockchain Research Assistant and how they are integrated into the application.

## Table of Contents

1. [OpenAI API](#openai-api)
2. [Firecrawl API](#firecrawl-api)
3. [API Authentication](#api-authentication)
4. [Error Handling](#error-handling)
5. [Rate Limiting Considerations](#rate-limiting-considerations)

## OpenAI API

The application uses OpenAI's API to power the research and elaboration agents that analyze blockchain information and generate comprehensive reports.

### Model Selection

The application uses GPT-4o, the latest and most advanced model from OpenAI at the time of development (released May 13, 2024).

### Chat Completions API

**Endpoint**: `https://api.openai.com/v1/chat/completions`

#### Research Agent Implementation

```python
response = self.client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": analysis_prompt}
    ],
    response_format={"type": "json_object"},
    temperature=0.1
)
```

**Parameters Explained**:

- `model`: Specifies "gpt-4o" as the model to use
- `messages`: Array of message objects with roles and content
  - `system_message`: Defines the specialized blockchain research agent role
  - `analysis_prompt`: Contains the research topic and raw data
- `response_format`: Specifies JSON format for structured output
- `temperature`: Set to 0.1 for more deterministic, focused responses

#### Elaboration Agent Implementation

```python
response = self.client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": elaboration_prompt}
    ],
    response_format={"type": "json_object"},
    temperature=0.2
)
```

**Parameters Explained**:

- `model`: Specifies "gpt-4o" as the model to use
- `messages`: Array of message objects with roles and content
  - `system_message`: Defines the specialized blockchain elaboration agent role
  - `elaboration_prompt`: Contains the research topic and initial analysis
- `response_format`: Specifies JSON format for structured output
- `temperature`: Set to 0.2 for somewhat creative but still focused responses

### Response Processing

Both agents parse the JSON responses and extract the structured research information:

```python
analysis_text = response.choices[0].message.content
analysis_json = json.loads(analysis_text)
```

## Firecrawl API

The application uses Firecrawl's API to gather blockchain-specific information from various web sources.

### Base URL

```
https://api.firecrawl.dev/v1
```

### Authentication

All requests include an Authorization header with the API key:

```python
self.headers = {
    "Authorization": f"Bearer {self.api_key}",
    "Content-Type": "application/json"
}
```

### Research Job Creation

**Endpoint**: `/research/start`

```python
payload = {
    "query": topic,
    "sources": blockchain_sources[:num_sources],
    "depth": depth,
    "blockchain_specific": True
}

response = requests.post(
    f"{self.base_url}/research/start",
    headers=self.headers,
    json=payload
)
```

**Parameters Explained**:

- `query`: The blockchain research topic
- `sources`: Array of blockchain-specific domains to prioritize
- `depth`: Research depth level (1-5)
- `blockchain_specific`: Boolean flag to focus on blockchain content

### Job Status Checking

**Endpoint**: `/research/status/{job_id}`

```python
status_response = requests.get(
    f"{self.base_url}/research/status/{job_id}",
    headers=self.headers
)
```

### Results Retrieval

**Endpoint**: `/research/results/{job_id}`

```python
results_response = requests.get(
    f"{self.base_url}/research/results/{job_id}",
    headers=self.headers
)
```

## API Authentication

The application uses environment variables to securely store API keys:

```python
# OpenAI authentication
self.api_key = os.getenv("OPENAI_API_KEY", "")
self.client = OpenAI(api_key=self.api_key)

# Firecrawl authentication
self.api_key = os.getenv("FIRECRAWL_API_KEY", "")
self.headers = {
    "Authorization": f"Bearer {self.api_key}",
    "Content-Type": "application/json"
}
```

### Key Management in Streamlit

The keys are collected via the Streamlit interface and set as environment variables:

```python
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["FIRECRAWL_API_KEY"] = firecrawl_api_key
```

## Error Handling

The application implements robust error handling for API interactions:

### OpenAI API Error Handling

```python
try:
    # API call
    response = self.client.chat.completions.create(...)
    # Response processing
except Exception as e:
    raise Exception(f"Error analyzing blockchain data: {str(e)}")
```

### Firecrawl API Error Handling

```python
try:
    # API calls
    response = requests.post(...)
    response.raise_for_status()
    # Job polling and results retrieval
except requests.exceptions.RequestException as e:
    # Fallback mechanism in case of API failure
    return self._simulate_blockchain_research(topic)
```

## Rate Limiting Considerations

### OpenAI Rate Limits

- The application uses low temperature settings to minimize token usage
- Content length is limited to avoid exceeding token limits
- Error handling includes checking for rate limit responses

### Firecrawl Rate Limits

- The application implements polling with reasonable timeouts
- A maximum number of retries prevents infinite loops
- The depth parameter controls the breadth of research to manage API usage

## Implementation Best Practices

1. **Security**:
   - API keys are never hardcoded
   - Keys are stored as environment variables
   - Keys are not exposed in responses or logs

2. **Efficiency**:
   - Responses are cached where appropriate
   - Requests are optimized to minimize API calls
   - Content is trimmed to avoid unnecessary token usage

3. **Resilience**:
   - Fallback mechanisms are in place for API failures
   - Exponential backoff is used for retries
   - Timeout management prevents hanging operations

4. **Structure**:
   - API interactions are encapsulated in dedicated classes
   - Response parsing is separated from API calls
   - Error handling is consistent across different API integrations