from transformers import BertModel, AutoTokenizer, AutoModelForCausalLM
from keybert import KeyBERT
import os


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def get_keybert():
    model_dir = os.path.join(os.path.dirname(__file__), "skt/kobert-base-v1")
    model = BertModel.from_pretrained(model_dir, local_files_only=True)
    kw_model = KeyBERT(model)
    return kw_model