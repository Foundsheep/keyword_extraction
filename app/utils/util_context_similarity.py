import torch

def calculate_similarity_based_on_embedding(embed_1, embed_2):

    embed_1 = embed_1.flatten()
    embed_2 = embed_2.flatten()

    embed_1_norm = embed_1 / torch.linalg.vector_norm(embed_1)
    embed_2_norm = embed_2 / torch.linalg.vector_norm(embed_2)

    score = torch.matmul(embed_1_norm, embed_2_norm)
    score = score.item()
    return score