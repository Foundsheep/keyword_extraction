import traceback
from ..models import kosim_tokenizer, kosim_model
from ..utils.util_context_similarity import calculate_similarity_based_on_embedding


def run(text_source, text_targets):
    score = []
    if len(text_source) != 1:
        print(f"text source should have one element, {len(text_source) = }")
        return score
    
    try:
        text_source.extend(text_targets)
        sentences = text_source
        inputs = kosim_tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
        embeddings, _ = kosim_model(**inputs, return_dict=False)

        # calculate the score one by one from the beginning
        for i in range(1, len(sentences)):
            score.append(calculate_similarity_based_on_embedding(embeddings[0], embeddings[i]))
    except Exception as e:
        print(e)
        traceback.print_exc()
    return score

