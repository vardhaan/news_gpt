import os
import openai
from transformers import GPT2TokenizerFast
from transformers.utils import logging

class GPT:
    def __init__(self):
        openai_api_key = os.environ.get('OPENAI_API_KEY')
        self.tokenizer = GPT2TokenizerFast.from_pretrained('gpt2')
        logging.set_verbosity_error()
        self.model_config = {
            "model_choice": "text-davinci-003",
            "model_temperature": 0.7,
            "max_tokens": 250,
        }
        self.max_allowed_tokens = 4000 #For Davinci. Needs to be updated to work with other models.

    def num_tokens_in_string(self, string_to_count):
        return len(self.tokenizer(string_to_count)['input_ids'])
    
    def get_completion(self, prompt, input_dict, model_config=None, which_input_chunkable=None):
        #TODO: Figure out max_text_token_size. Complete chunk handling.
        completion_length = model_config["max_tokens"]
        prompt_length = self.num_tokens_in_string(prompt)
        input_length = 0
        for key in input_dict:
            input_length += self.num_tokens_in_string(input_dict[key])
            #TODO: need to track which input is chunkable here too. We'll subtract that from input_length, then add that remainder to prompt and completion length.
            #Then 4000 - that value = max_text_token_size
        if (completion_length+prompt_length+input_length <= self.max_allowed_tokens):
            #No need to chunk
            return self.send_completion_request(prompt, input_dict, model_config)
        if (completion_length+prompt_length+input_length > self.max_allowed_tokens):
            if which_input_chunkable == None:
                raise Exception("Input too long for model. Please reduce input length or use a different model.")
            else:
                chunks = self.chunk_text(input_dict[which_input_chunkable], completion_length)
            #need to handle the chunking cases here.
                
    def format_prompt(self, prompt, input_dict):
        #TODO: String formatting usually requires knowing the field names in advance. How do we get around this?
        return

            
    def chunk_text(self, text, max_text_token_size):
        '''
        Find max chunk size for each chunk. We start with number of tokens each chunk can have.
        To split the text into those chunks, we find the character indices of the start of each chunk.
        To do that, we multiply max chunk size (tokens) by 4 to get char size.'''
        max_chunk_chars = max_text_token_size*3 #On avg, 4 chars per token, but doing 3 to reduce chunk size to be safe.
        chunk_indices = [max_chunk_chars*i for i in range(int(len(text)/max_chunk_chars)+1)]
        print(range(int(len(text)/max_chunk_chars)))
        chunk_indices.append(len(text))
        print(chunk_indices)
        chunks = [text[chunk_indices[i]:chunk_indices[i+1]] for i in range(len(chunk_indices)-1)]
        if chunks[-1] == "":
            del chunks[-1]
        return chunks


    def send_completion_request(self, prompt, model_config=None):
        model_choice = model_config["model_choice"]
        model_temperature = model_config["model_temperature"]
        max_tokens = model_config["max_tokens"]

        openai.api_key = os.environ.get('OPENAI_API_KEY')
        response = openai.Completion.create(
            model=model_choice,
            prompt=prompt,
            temperature=model_temperature,
            max_tokens=max_tokens
        )
        return response['choices'][0]['text']

'''
#tests
gpt = GPT()
text = "abcdefghi"
print(gpt.chunk_text(text, 1))
'''