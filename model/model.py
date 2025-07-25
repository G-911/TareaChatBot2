from langchain_mistralai.chat_models import ChatMistralAI
from config.config import MISTRAL_API_KEY

model = ChatMistralAI(api_key = MISTRAL_API_KEY)