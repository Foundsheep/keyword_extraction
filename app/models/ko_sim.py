from transformers import AutoModel, AutoTokenizer
import os

def get_ko_sim_models():
    model_dir = os.path.join(os.path.dirname(__file__), 'BM-K/KoSimCSE-roberta')
    model = AutoModel.from_pretrained(model_dir, local_files_only=True)
    tokenizer = AutoTokenizer.from_pretrained('BM-K/KoSimCSE-roberta')

    return tokenizer, model

