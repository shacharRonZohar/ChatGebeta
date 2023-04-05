from transformers import AutoModelForCausalLM, AutoTokenizer

# gpt2 is the predecessor of gpt3 and is a smaller model.
model_name = "gpt2"
# The tokenizer is used to convert the input text into a format that the model can understand, and to convert the model's output back into text.
tokenizer = AutoTokenizer.from_pretrained(model_name)
# The model is the actual neural network that will be used to generate the text.
model = AutoModelForCausalLM.from_pretrained(model_name)


def get_response(message):

    # Create a sequence of integers representing the message.
    input_ids = tokenizer.encode(message, return_tensors="pt")
    # Ask the model to generate a response, getting a list of lists in return.
    output_ids = model.generate(
        input_ids,
        max_length=50,
        # The number of beams to use for beam search. Beam search is an algorithm that finds the most likely sequence of words.
        num_beams=5,
        #
        no_repeat_ngram_size=2,
        # Make sure the model doesn't output the same text twice.
        early_stopping=True
    )
    # Get the decoded text from the model's output.
    output = tokenizer.decode(
        output_ids[0], skip_special_tokens=True)
    # The tokenizer returns both the user input and the bot response in the same string as diffrent lines.
    user_input, bot_response = output.split('\n\n')
    return {
        "user_input": user_input,
        "bot_response": bot_response
    }


get_response("Hello, how are you?")
