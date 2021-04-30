import timeit
from collections import Counter


def count_words(text):
    text = text.lower()
    puncs = [",", "?", ".", ";", ":", "'", '"']
    for punc in puncs:
        text = text.replace(punc, "")
    word_count = {}
    for word in text.split(" "):
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def count_words_fast(text):
    text = text.lower()
    puncs = [",", "?", ".", ";", ":", "'", '"']
    for punc in puncs:
        text = text.replace(punc, "")
    word_count = Counter(text.split(" "))
    return word_count


def dictionary_time():
    SETUP_CODE = """ 
from __main__ import count_words
from collections import Counter
text = "There were little things that she simply could not stand. The sound of someone tapping their nails on the table. A person chewing with their mouth open. Another human imposing themselves into her space. She couldn't stand any of these things, but none of them compared to the number one thing she couldn't stand which topped all of them combined."
"""

    TEST_CODE = """ 
count_words(text)"""

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=100000)

    # priniting minimum exec. time
    print("Dictionary count {}".format(min(times)))


def counter_time():
    SETUP_CODE = """ 
from __main__ import count_words_fast 
from collections import Counter
text = "There were little things that she simply could not stand. The sound of someone tapping their nails on the table. A person chewing with their mouth open. Another human imposing themselves into her space. She couldn't stand any of these things, but none of them compared to the number one thing she couldn't stand which topped all of them combined."
"""

    TEST_CODE = """count_words_fast(text)"""

    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE, stmt=TEST_CODE, repeat=3, number=100000)

    # priniting minimum exec. time
    print("Counter count {}".format(min(times)))


texts = "There were little things that she simply could not stand. The sound of someone tapping their nails on the table. A person chewing with their mouth open. Another human imposing themselves into her space. She couldn't stand any of these things, but none of them compared to the number one thing she couldn't stand which topped all of them combined."
print(count_words_fast(texts) is count_words(texts))