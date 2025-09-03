from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate


class AINewsNode:
    def __init__(self, llm):
        """
        Initialize the AINewsNode with API keys for Tavily and GROQ
        """
        self.tavily = TavilyClient()
        self.llm = llm
        
        # This is used to capture the various steps in this file so that later can be use for steps shown
        self.state = {}
    
    def fetch_news(self, state: dict) -> dict:
        """
        Fetch AI news based ont he specified frequency.
        
        Args:
            state (dict): The state dictionary containing 'frequency'.
        
        Returns:
            dict: Updated state with 'news_data' key containing fetched news
        """
        
        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {
            'daily': 'd',
            'weekly': 'w',
            'monthly': 'm',
            'year': 'y'
        }
        
        days_map = {
            'daily': 1,
            'weekly': 7,
            'monthly': 30,
            'year': 366
        }
        
        response = self.tavily.search(
            query = "Top AI technology news Pakistan and globally.",
            topic = 'news',
            time_range=time_range_map[frequency],
            include_answer='advanced',
            max_results=20,
            days=days_map[frequency]
        )
        
        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        
        return state