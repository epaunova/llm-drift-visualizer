import json
from sentence_transformers import SentenceTransformer, util
import argparse

def compute_drift(data_path):
    with open(data_path) as f:
        data = json.load(f)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    for i, item in enumerate(data):
        emb1 = model.encode(item['output_v1'], convert_to_tensor=True)
        emb2 = model.encode(item['output_v2'], convert_to_tensor=True)
        score = util.cos_sim(emb1, emb2).item()
        print(f"Prompt {i+1}: Drift Score = {1 - score:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True, help="Path to JSON data file")
    args = parser.parse_args()
    compute_drift(args.data)
