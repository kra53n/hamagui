text = b'  version    : 2.1.0.203\n  pid        : 26696\n  status     : offline\n  client id  : 254-901-802\n  address    : 25.103.11.92    2620:9b::1967:b5c\n  nickname   : krakaka\n  lmi account: \n\n'

def get_from_text(text, word):
    """
    From `text` function catch word and return information
    that situated after this word.

    For example: from `status: offline` it will return offline
    """
    text = text.decode("utf-8")
    len_text = len(text)
    len_word = len(word)
    # from what place begin reading
    begin = 0
    catch = None
    # catg information of the word parameter
    while (len_text - begin) >= len_word:
        if text[begin:begin+len_word] == word:
            end = begin+len_word
            while text[end] != "\n":
                end += 1
            catch = text[begin+len_word:end]
        begin += 1
    # remove `:` and spaces
    catch = catch.replace(":", "")
    catch = catch.replace(" ", "")
    return catch

print(get_from_text(text, "status"))
