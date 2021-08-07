from nltk.tokenize import word_tokenize
from collections import defaultdict

class InvertedIndex:

    docs = []
    term_index = []
    num_docs = 0
    common_list = []

    def __init__(self,n) -> None:
        self.num_docs = n
        for i in range(n):
            print("Enter text in doc",i)
            l = input()
            self.docs.append(l)
        self.get_terms()
        print()
        print("The term index is: ")
        print("Terms","Doc Id",sep="\t\t")
        for docs in self.term_index:
            for keys,values in docs.items():
                if len(keys)<=5:
                    print(keys,values,sep="\t\t\t")
                    continue
                print(keys,values,sep="\t\t")
        self.make_common_term_index()
        print()
        print("Sorted term index is: ")
        print("Terms","Doc Id",sep="\t\t")
        for key,value in self.common_list.items():
            for i in range(len(value)):
                if len(key)<=5:
                    print(key,value[i],sep="\t\t\t")
                    continue
                print(key,value[i],sep="\t\t")
        print()
        print("The inverted index is: ")
        self.inverted_index()

    
    def get_terms(self):
        for id,doc in enumerate(self.docs):
            term_list = {}
            for i in word_tokenize(doc):
                if i not in term_list.keys():
                    term_list[i] = id
            self.term_index.append(term_list)
    
    def make_common_term_index(self):
        self.common_list = defaultdict(list)

        for id,doc in enumerate(self.term_index):
            for keys,values in doc.items():
                self.common_list[keys].append(values)

    def inverted_index(self):
        print("Term","Freq","Postings List",sep="\t\t")
        for key in sorted(self.common_list.keys()):
            value = self.common_list[key]
            value = [str(v) for v in value]
            pl = "->".join(value)
            if len(key)<=5:
                    print(key,len(value),pl,sep="\t\t\t")
                    continue
            print(key,len(value),pl,sep="\t\t")

InvertedIndex(4) #enter number of documents as the argument