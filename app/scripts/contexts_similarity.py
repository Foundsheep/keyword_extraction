from ..models import kosim_tokenizer, kosim_model
from ..utils.util_context_similarity import calculate_similarity_based_on_embedding


def run(sentence_1, sentence_2):
    score = None
    try:
        sentences = [sentence_1, sentence_2]

        inputs = kosim_tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
        embeddings, _ = kosim_model(**inputs, return_dict=False)

        score = calculate_similarity_based_on_embedding(embeddings[0], embeddings[1])
    except Exception as e:
        print(e)
    return score

