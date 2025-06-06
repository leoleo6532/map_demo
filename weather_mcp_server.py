import random
from fastmcp import FastMCP
from typing import Union, List

# 建立模擬氣候資訊的 MCP Server
mcp = FastMCP("MockTaiwanWeather")

cities = [
    "台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市",
    "基隆市", "新竹市", "嘉義市", "宜蘭縣", "花蓮縣", "台東縣",
    "澎湖縣", "金門縣", "連江縣"
]

weather_conditions = [
    "晴時多雲", "短暫陣雨", "多雲時晴", "午後雷陣雨",
    "陰天", "大雨", "小雨", "雷雨", "多雲", "晴天"
]

temperatures = list(range(20, 37))  # 模擬溫度 20～36°C

@mcp.tool()
def get_weather(city: Union[str, List[str]]) -> Union[str, List[str]]:
    """
    模擬查詢台灣城市的氣候資訊，支援單一或多個城市。

    Args:
        city (Union[str, List[str]]): 城市名稱或城市名稱列表（例如："台北市"，或 ["台北市", "高雄市"]）

    Returns:
        Union[str, List[str]]: 模擬氣候資訊
    """
    if isinstance(city, str):
        city_list = [c.strip() for c in city.split(",")]
    else:
        city_list = city

    results = []
    for c in city_list:
        if c not in cities:
            results.append(f"未找到城市：{c}，請輸入台灣有效城市名稱。")
        else:
            condition = random.choice(weather_conditions)
            temp = random.choice(temperatures)
            results.append(f"{c} 現在天氣：{condition}，氣溫約 {temp}°C。")

    return results if len(results) > 1 else results[0]

@mcp.tool()
def list_cities() -> List[str]:
    """
    列出支援查詢氣候資訊的台灣縣市清單。

    Returns:
        List[str]: 支援的縣市名稱列表。
    """
    return cities

# 啟動 MCP Server
if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8001,
        path="/mcp/"
    )
