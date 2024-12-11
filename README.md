# didactic-winner
Dummy API service emulating a graph neural network

```bash
docker build -t dummy-gnn-api .
```

```bash
docker run -d -p 8000:8000 --name dummy-gnn-container dummy-gnn-api
```

The API will be accessible at ```http://127.0.0.1:8000```


To test, use Postman or 
```bash
curl -X POST "http://127.0.0.1:8000/gnn/embeddings" -H "Content-Type: application/json" -d '{
   "nodes": [
       {"node_id": 1, "properties": {"feature1": 0.5, "feature2": 1.0}},
       {"node_id": 2, "properties": {"feature1": 0.2, "feature2": 0.8}}
   ]
}'
```
