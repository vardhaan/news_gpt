from datetime import datetime
from transformers import GPT2TokenizerFast
from transformers.utils import logging
import time

# function that converts UTC string into datetime object
def convert_utc_string_to_datetime(utc_string):
    return datetime.strptime(utc_string, '%Y-%m-%dT%H:%M:%SZ')


# function that converts datetime object into UTC string
def convert_datetime_to_utc_string(datetime_obj):
    return datetime_obj.strftime('%Y-%m-%dT%H:%M:%SZ')


def num_tokens_in_string(string_to_count):
    #logging.set_verbosity_error()
    tokenizer = GPT2TokenizerFast.from_pretrained('gpt2')
    return len(tokenizer(string_to_count)['input_ids'])


#Test
x = "Hello world what is up"
start = time.time()
tokenizer = GPT2TokenizerFast.from_pretrained('gpt2')
end_tokenizer = time.time()
y = tokenizer(x)
end_encoding = time.time()
print("Time to load tokenizer: ", (end_tokenizer - start)*1000, "ms")
print("Time to encode: ", (end_encoding - end_tokenizer)*1000, "ms")

