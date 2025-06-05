from fastmcp import FastMCP

# 建立 Math MCP Server
mcp = FastMCP("Math")

# 工具 1：加法
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    將兩個整數相加並回傳總和。

    Args:
        a (int): 第一個加數
        b (int): 第二個加數

    Returns:
        int: 相加的結果
    """
    return a + b

# 工具 2：乘法
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    將兩個整數相乘並回傳乘積。

    Args:
        a (int): 被乘數
        b (int): 乘數

    Returns:
        int: 相乘的結果
    """
    return a * b

# 啟動 MCP Server，使用 HTTP 模式
if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",  # 明確使用 HTTP 傳輸協定
        host="0.0.0.0",                # 對外開放（或改成 "127.0.0.1" 僅本地）
        port=8000,
        path="/mcp/"                   # 對應 endpoint 如 http://localhost:8000/mcp/
    )
