import asyncio
import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from rich import print_json

# 設定 Gemini API 金鑰
os.environ["GOOGLE_API_KEY"] = "AIzaSyDYg89d93zs_UpbNuaSb45o8xEzFrhosPI"

def serialize_messages(messages):
    """將 LangChain 訊息物件轉換為可序列化格式"""
    result = []
    for msg in messages:
        item = {
            "role": type(msg).__name__,
            "content": getattr(msg, "content", ""),
        }
        if hasattr(msg, "name"):
            item["name"] = msg.name
        if hasattr(msg, "tool_call_id"):
            item["tool_call_id"] = msg.tool_call_id
        result.append(item)
    return result

async def main():
    # 建立 MCP 客戶端
    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "streamable_http",
                "url": "http://localhost:8001/mcp/",
            },
            "weather": {
                "transport": "streamable_http",
                "url": "http://localhost:8002/mcp/",
            }
        }
    )

    # 取得工具並建立 agent
    tools = await client.get_tools()
    agent = create_react_agent(
        ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7),
        tools
    )

    user_input = input("Input : ")
    # 執行對話
    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": user_input}]}
    )

    # 美化輸出
    print_json(data={"messages": serialize_messages(response["messages"])})

if __name__ == "__main__":
    asyncio.run(main())
