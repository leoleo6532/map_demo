import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

# 設定 LM Studio 為本地 OpenAI server
os.environ["OPENAI_API_BASE"] = "http://localhost:1234/v1"
os.environ["OPENAI_API_KEY"] = "lm-studio"

async def main():
    # 建立 MCP 客戶端，連接到本地的 Math MCP 伺服器
    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "http",
                "url": "http://localhost:8000/mcp",  # MCP server endpoint
            }
        }
    )

    tools = await client.get_tools()

    # 使用 LM Studio 模型
    agent = create_react_agent(
        ChatOpenAI(model="TheBloke/Mistral-7B-Instruct-v0.2-GGUF"),  # 請換成你有載的模型
        tools
    )

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "請計算 (3 + 5) x 12"}]}
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
