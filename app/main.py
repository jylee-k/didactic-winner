from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI()

# Define the input model
class NodeInput(BaseModel):
    node_id: str
    properties: dict

class GNNInput(BaseModel):
    nodes: List[NodeInput]

# Define the output model
class NodeEmbedding(BaseModel):
    node_id: str
    embedding: List[float]

class GNNOutput(BaseModel):
    embeddings: List[NodeEmbedding]

# Dummy GNN logic
def generate_dummy_embedding(properties: dict) -> List[float]:
    # Generate embeddings based on properties or randomly
    feature_vector = np.array(list(properties.values()))
    embedding_size = 8  # Fixed size for the dummy embeddings
    return np.random.rand(embedding_size).tolist()

# API endpoint
@app.post("/gnn/embeddings", response_model=GNNOutput)
def get_node_embeddings(gnn_input: GNNInput):
    if not gnn_input.nodes:
        raise HTTPException(status_code=400, detail="No nodes provided.")

    embeddings = []
    for node in gnn_input.nodes:
        embedding = generate_dummy_embedding(node.properties)
        embeddings.append(NodeEmbedding(node_id=node.node_id, embedding=embedding))

    return GNNOutput(embeddings=embeddings)

