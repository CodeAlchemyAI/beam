import torch
from torch import cuda, bfloat16
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, StoppingCriteria, StoppingCriteriaList
from langchain.chains import ConversationChain
from langchain.llms import HuggingFacePipeline
from langchain.memory import ConversationBufferMemory

# Setting up device and cache path
device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu'
cache_path = "./models"

# Setting up the model
model = AutoModelForCausalLM.from_pretrained(
    'mosaicml/mpt-7b-chat',
    trust_remote_code=True,
    torch_dtype=bfloat16,
    cache_dir=cache_path,
    max_seq_len=2048
)
model.eval()
model.to(device)

# Setting up the tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")

stop_token_ids = tokenizer.convert_tokens_to_ids([""])

# Custom stopping criteria


class StopOnTokens(StoppingCriteria):
    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor, **kwargs) -> bool:
        return any(input_ids[0][-1] == stop_id for stop_id in stop_token_ids)


stopping_criteria = StoppingCriteriaList([StopOnTokens()])

# Setting up the text generation pipeline
generate_text = pipeline(
    model=model, tokenizer=tokenizer,
    return_full_text=True,
    task='text-generation',
    device=device,
    stopping_criteria=stopping_criteria,
    temperature=0.1,
    top_p=0.15,
    top_k=0,
    max_new_tokens=64,
    repetition_penalty=1.1
)

# Function to start the conversation


def start_conversation(**inputs):
    query = inputs["query"]

    llm = HuggingFacePipeline(pipeline=generate_text)

    conversation = ConversationChain(
        llm=llm,
        verbose=True,
        memory=ConversationBufferMemory()
    )

    res = conversation.predict(input=query)

    return {"pred": res}


if __name__ == "__main__":
    # You can customize this query however you want:
    query = "What are some use cases I can use this product for?"
    start_conversation(query=query)