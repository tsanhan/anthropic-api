import json

from anthropic_class import AnthropicClient
from dataset_gen import generate_dataset

client = AnthropicClient()
dataset = generate_dataset(client=client.get_client())

with open("./2. Prompt evaluation/dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)
    

