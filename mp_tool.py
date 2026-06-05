from mp_api.client import MPRester
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_materials(material_list):

    api_key = os.getenv("MP_API_KEY")

    results = []

    with MPRester(api_key) as mpr:

        for mat in material_list:

            docs = mpr.materials.summary.search(
                formula=mat,
                fields=[
                    "material_id",
                    "formula_pretty",
                    "band_gap",
                    "density"
                ]
            )

            if docs:
                results.append({
                    "name": docs[0].formula_pretty,
                    "band_gap": docs[0].band_gap,
                    "density": docs[0].density
                })

    return results