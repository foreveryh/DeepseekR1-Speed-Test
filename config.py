import os
from dotenv import load_dotenv

load_dotenv()

PROVIDERS = [
    {
        "name": "火山引擎",
        "api_key": os.getenv("VOLCENGINE_API_KEY", ""),
        "base_url": "https://ark.cn-beijing.volces.com/api/v3",
        "model": os.getenv("VOLCENGINE_MODEL", "ep-20250213205153-qdfsd")
    },
    {
        "name": "DeepSeek 官方",
        "api_key": os.getenv("DEEPSEEK_API_KEY", ""),
        "base_url": "https://api.deepseek.com",
        "model": "deepseek-reasoner"
    },
    {
        "name": "阿里云/百炼",
        "api_key": os.getenv("ALIBABA_API_KEY", ""),
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "deepseek-r1"
    },
    {
        "name": "腾讯云",
        "api_key": os.getenv("TENCENT_API_KEY"),
        "base_url": "https://api.lkeap.cloud.tencent.com/v1",
        "model": "deepseek-r1"
    },
    {
        "name": "PPInfra",
        "api_key": os.getenv("PPINFRA_API_KEY"),
        "base_url": "https://api.ppinfra.com/v3/openai",
        "model": "deepseek/deepseek-r1/community"
    },
    {
        "name": "Nvida NIM",
        "api_key": os.getenv("NVIDIA_API_KEY"),
        "base_url": "https://integrate.api.nvidia.com/v1",
        "model": "deepseek-ai/deepseek-r1"
    },
]

TEST_MESSAGES = [
    {
        'role': 'user',
        'content': "给我写一首七言绝句，赞叹人生苦短，应当及时泡妞行乐"
    }
]