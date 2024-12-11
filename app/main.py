from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI()

# Define the input model
class NodeInput(BaseModel):
    node_id: int
    properties: dict

class GNNInput(BaseModel):
    nodes: List[NodeInput]

# Define the output model
class NodeEmbedding(BaseModel):
    node_id: int
    embedding: List[float]

class GNNOutput(BaseModel):
    embeddings: List[NodeEmbedding]

# Dummy GNN logic
def generate_dummy_embedding(properties: dict) -> List[float]:
    # Generate embeddings based on properties or randomly
    feature_vector = np.array(list(properties.values()))
    embedding_size = 8  # Fixed size for the dummy embeddings
    if len(feature_vector) == 0:
        return np.random.rand(embedding_size).tolist()
    embedding = np.tanh(np.dot(feature_vector, np.random.rand(len(feature_vector), embedding_size)))
    return embedding.tolist()

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

# Run using: uvicorn dummy_gnn:app --reload
