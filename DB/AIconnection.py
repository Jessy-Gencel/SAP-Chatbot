from ai_core_sdk.ai_core_v2_client import AICoreV2Client
from dotenv import load_dotenv
import os

load_dotenv()

ai_core_client = AICoreV2Client(
    base_url = "https://api.ai.prod.eu-central-1.aws.ml.hana.ondemand.com" + "/v2", # The present SAP AI Core API version is 2
    auth_url=  "https://delaware-ai-1ftkiuy2.authentication.eu10.hana.ondemand.com" + "/oauth/token", # Suffix to add
    client_id = os.getenv("AI_CLIENT_ID"),
    client_secret = os.getenv("AI_CLIENT_SECRET"),
)