from app.models.key_bert import get_keybert
from app.models.ko_sim import get_ko_sim_models

kw_model = get_keybert()
kosim_tokenizer, kosim_model = get_ko_sim_models()