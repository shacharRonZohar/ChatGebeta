from transformers import AutoTokenizer, AutoModelForCausalLM

DEFAULT_GENERATION_SETTINGS = {
    # The maximum length of the sequence to be generated. With a lower value, the model will be less likely to generate long complete texts, but will be faster to generate texts.
    "max_new_tokens": 70,
    # The number of beams to use for beam search. Beam search is an algorithm that finds the most likely sequence of words.
    "num_beams": 5,
    # Make sure the model doesn't output the same text twice, by allowing it to stop generating the text early after it has repeated the same text.
    "no_repeat_ngram_size": 2,
    "early_stopping": True,
    # "temperature": 0.7,
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
    # example_output = "Hi, how are you today?\n\n\n\nI'm so happy to be here.\n\n/ I've been working on this project for a while now, and I'm really excited about it. It's been a long time coming, but I feel like it's finally time for me to get back to work on the project. So, thank you so much for taking the time to answer my/,/"
    # output = example_output

    # # The tokenizer sometimes returns the message as part of the start of the output, and it can look wierd if it's a long sequence so we remove it if it's there.
    if output.startswith(f'{message}\n\n'):
        output = output[len(f'{message}\n\n'):]
    # Then, we remove any wierd characters that might have been left over from the slice, or the model might has added to the start and end of the output, like newlines, commas, slashes, etc.
    output = output.strip(',/\n\n')

    return {
        "user_input": message,
        "bot_response": output
    }
