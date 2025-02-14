import os
from dotenv import load_dotenv

load_dotenv()

PROVIDERS = [
    {
        "name": "DS-R1-Q4-K-M AmpereOne",
        "api_key": "AmpereOne_API_KEY",
        "base_url": "http://192.168.1.106:1025/v1",
        "model": "deepseek-ai/deepseek-r1"
    },
    {
        "name": "DS-R1-7B-Q8_0 AmpereOne",
        "api_key": "AmpereOne_API_KEY",
        "base_url": "http://192.168.1.106:1026/v1",
        "model": "deepseek-ai/deepseek-r1"
    },
]

TEST_MESSAGES = [
    {
        'role': 'user',
        'content': "给我写一首七言绝句，赞叹人生苦短，应当及时泡妞行乐"
    }
]
