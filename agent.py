from llm import (
    recommend_materials,
    generate_report
)

from mp_tool import fetch_materials


def run_agent(query):

    candidates = recommend_materials(
        query
    )

    materials_data = fetch_materials(
        candidates
    )

    report = generate_report(
        query,
        materials_data
    )

    return {
        "candidates": candidates,
        "materials": materials_data,
        "report": report
    }