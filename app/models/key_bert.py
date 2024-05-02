from transformers import BertModel, AutoTokenizer, AutoModelForCausalLM
from keybert import KeyBERT

def get_dummy_model():
    polyglot_repo_id = "EleutherAI/polyglot-ko-1.3b"
    repo_id = "rycont/KoQuestionBART"
    tokenizer = AutoTokenizer.from_pretrained(repo_id)
    tokenizer_2 = AutoTokenizer.from_pretrained(polyglot_repo_id)
    model = AutoModelForCausalLM.from_pretrained(repo_id)
    model_2 = AutoModelForCausalLM.from_pretrained(polyglot_repo_id)
    return model

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def get_keybert():
    model = BertModel.from_pretrained('skt/kobert-base-v1')
    kw_model = KeyBERT(model)
    return kw_model