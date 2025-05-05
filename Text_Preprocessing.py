import string
import re

punctuations = string.punctuation
mention_pattern = re.compile(r'@\w+')

def remove_mentions(x):
    return x.apply(lambda text: mention_pattern.sub('', str(text)))

def remove_punctuations(x):
    return x.apply(lambda text: str(text).translate(str.maketrans('', '', punctuations)))

def lower_case_remove_whitespace(x):
    return x.apply(lambda text: str(text).lower().strip())

def remove_non_ascii(x):
    return x.apply(lambda text: re.sub(r'[^\x00-\x7F]+', '', str(text)))