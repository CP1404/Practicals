def main():
    text = str(input("Text: "))
    count = dict_count(text)
    word_list = sorted(count.items(),key=lambda d:d[0])
    #print(word_list)
    for key, value in word_list:
        print(f"{key} : {value}".format(key= key,value= value))


# count appearance of each word and save as dict
def dict_count(sentence):
    text_dict = {}
    for i in sentence.split(" "):
        text_dict[i] = text_dict.get(i,0)+1

    return text_dict
main()

