words = ['data', 'cam', 'camp', 'lack']

def word_present(word: str, start: str, i: int) -> bool:
    length = len(word)-i
    if length == 0:
        if start == "":
            return True 
        else:
            return False
    
    start += word[i]
    i += 1
    if start in words:
        is_present = word_present(word, start, i)
        # other is to fresh start
        is_present2 = word_present(word, "", i)
        return is_present or is_present2
    else:
        is_present = word_present(word, start, i)
        return is_present
        

print(word_present("dataca", start="", i=0))