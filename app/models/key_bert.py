from transformers import BertModel, AutoTokenizer, AutoModelForCausalLM
from keybert import KeyBERT


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

# TODO: Get the model from local
def get_keybert():
    model = BertModel.from_pretrained('skt/kobert-base-v1')
    kw_model = KeyBERT(model)
    return kw_model