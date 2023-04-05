from transformers import AutoTokenizer, AutoModelForCausalLM

DEFAULT_GENERATION_SETTINGS = {
    # The maximum length of the sequence to be generated. With a lower value, the model will be less likely to generate long complete texts, but will be faster to generate texts.
    "max_new_tokens": 150,
    # The number of beams to use for beam search. Beam search is an algorithm that finds the most likely sequence of words.
    "num_beams": 5,
    # Make sure the model doesn't output the same text twice, by allowing it to stop generating the text early after it has repeated the same text.
    "no_repeat_ngram_size": 2,
    "early_stopping": True
}

# gpt2 is the predecessor of gpt3 and is a smaller model.
# This particular version is the smallest version of the model, conatining only 124M parameters.
model_name = "gpt2"
# The tokenizer is used to convert the input text into a format that the model can understand, and to convert the model's output back into text.
tokenizer = AutoTokenizer.from_pretrained(model_name)
# The model is the actual neural network that will be used to generate the text.
model = AutoModelForCausalLM.from_pretrained(model_name)


def query(message):

    # Create a sequence of numbers representing the message.
    encoded_input = tokenizer(message, return_tensors='pt')

    # Ask the model to generate a response, getting a list of lists (encoded_output) in return.
    generation_args = {
        # The sequence of numbers representing the message.
        "input_ids": encoded_input["input_ids"],
        # The attention mask is used to tell the model which tokens are real and which are padding.
        "attention_mask": encoded_input["attention_mask"],
        **DEFAULT_GENERATION_SETTINGS
    }
    encoded_output = model.generate(**generation_args)
    # Get the decoded text from the model's output.
    output = tokenizer.decode(encoded_output[0], skip_special_tokens=True)
    # The tokenizer returns both the user input and the bot response in the same string as diffrent lines,
    # so we split the string into two vars that we later pack into a dictionary.
    user_input, bot_response = output.split('\n\n')

    return {
        "user_input": user_input,
        "bot_response": bot_response
    }
