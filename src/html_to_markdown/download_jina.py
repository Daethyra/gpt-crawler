import torch
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained(
    "jinaai/jina-embeddings-v2-small-en", trust_remote_code=True
)
model = AutoModel.from_pretrained("jinaai/jina-embeddings-v2-small-en")