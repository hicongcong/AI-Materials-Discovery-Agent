import streamlit as st
from agent import run_agent

st.set_page_config(
    page_title="AI Materials Discovery Agent",
    page_icon="🧪"
)

st.title("🧪 AI Materials Discovery Agent")

query = st.text_input(
    "请输入材料研发需求",
    placeholder="例如：寻找下一代功率电子器件材料"
)

if st.button("生成研究报告"):

    with st.spinner("AI正在分析..."):

        result = run_agent(query)

    st.subheader("推荐候选材料")

    for mat in result["candidates"]:
        st.write(f"• {mat}")

    st.subheader("材料数据库结果")

    st.json(result["materials"])

    st.subheader("AI分析报告")

    st.write(result["report"])