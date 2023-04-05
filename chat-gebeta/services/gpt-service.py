from transformers import pipeline, GenerationConfig
# Model instantiation
# gpt-2 is a the predecessor of gpt-3, it is a large transformer-based language model with 1.5 billion parameters, trained on a dataset of 8 million web pages.
model_name = "gpt2"
# generation_config = GenerationConfig(

# )
generator = pipeline(model=model_name,
                     tokenizer=model_name)

# print(generation_config)
input_text = "Hello, how are you today?"

output_text = generator(input_text, max_length=50,
                        num_beams=5,
                        no_repeat_ngram_size=2,
                        early_stopping=True,)
print(output_text[0]["generated_text"])
