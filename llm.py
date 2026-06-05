from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("SILICONFLOW_API_KEY"),
    base_url="https://api.siliconflow.cn/v1"
)


def recommend_materials(query):

    prompt = f"""
你是一位材料科学专家。

用户需求：
{query}

请推荐最适合研究的3种候选材料。

严格要求：

只返回JSON数组

不要Markdown

不要```json

不要解释

只返回化学式。

示例：

["GaN","SiC","Ga2O3"]

不要返回：

Diamond
Graphene
Perovskite
"""

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    try:
        return json.loads(text)
    except:
        return [text]


def generate_report(user_query, materials_data):

    prompt = f"""
你是一位材料研发专家。

用户需求：
{user_query}

候选材料数据：

{materials_data}

请生成：

# 推荐材料

# 性能比较

# 应用场景

# 结论

用中文回答。
"""

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content