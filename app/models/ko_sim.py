from transformers import AutoModel, AutoTokenizer

def get_ko_sim_models():

    model = AutoModel.from_pretrained('BM-K/KoSimCSE-roberta')
    tokenizer = AutoTokenizer.from_pretrained('BM-K/KoSimCSE-roberta')

    return tokenizer, model

