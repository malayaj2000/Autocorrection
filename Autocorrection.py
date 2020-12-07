def find_persons(text):
    nlp=spacy.load("en_core_web_sm")
    doc2 = nlp(text)
    persons = [ent.text for ent in doc2.ents if ent.label_ == 'PERSON']

    return persons


def spell_checker(text):
    name=find_persons(text)
    name_word=[i.split(" ") for i in name]
    y=[j for sub in name_word for j in sub]
    y=set(y)
    c=[]
    for i in text.split() :
        if i not in y:
            t=TextBlob(i)
            c_text = t.correct()
            z=list(enumerate(Word(str(t)).spellcheck()))
            if (str(c_text)!=str(t))and len(z)!=1:
                print(f'{t} is probably incorrectly spelled')
                print("possible suggestions are")
                for k in z:
                    print(f'{k[0]}:{k[1][0]}')
                print("or choose '-1' if it is correct")
                option=int(input())
                if option!=-1:
                    c.append(str(z[option][1][0]))
                else:
                    c.append(str(t))
            else:
                c.append(str(c_text))
        else:
            c.append(str(i))
    x=" ".join(c)
    return x


def main():
    text = input()
    c_text=spell_checker(text)
    print(c_text)


if __name__=="__main__":
    from textblob import TextBlob,Word
    import spacy
    main()