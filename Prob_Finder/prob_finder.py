#!/usr/bin/python3
#@author: Github.com/syedalizain033  
from pypdf import PdfReader #download via pip3 install pypdf

def prob_finder(dist,total):
    dist_percentage = {char: round((count / total) * 100) for char, count in dist.items()}
    dist_percentage=dict(sorted(dist_percentage.items(), key=lambda x: x[1], reverse=True))
    return dist_percentage
    # counter=0
    # # for i,j in dist_percentage.items():
    # #     counter+=j
    # # print(counter)

def dist_gen(text):
    dist={}
    for i in text:
        if i in dist:
            dist[i]=dist[i]+1
        else:
            dist[i]=1
    return dist

def wordcounter(pdf,text=""):
    content=PdfReader(pdf)
    for i in range(len(content.pages)):
        data=content.pages[i]
        text=text+data.extract_text()
    text=text.lower().replace(" ","").replace("\n","").replace("'","").replace("'","").replace("/","").replace("-","").replace(",","").replace("!","").replace(".","").replace("`","").replace("’","").replace("‘","").replace(":","")
    # print(text)
    dist=dist_gen(text)
    # print(dist)
    return prob_finder(dist,len(text))
    

def crack(dist, cipher):
    decrypted_text = ''
    enc_dist=prob_finder(dist_gen(cipher),len(cipher))
    enc_dist=dict(sorted(enc_dist.items(), key=lambda x: x[1], reverse=True))

    c=0
    x=[x for x,y in enc_dist.items()]
    i=[i for i,y in dist.items()]
    print(cipher)
    for j in range(len(x)):
        try:
            if x[c]==' ':
                continue
            cipher=cipher.replace(x[c],i[c])
            print(cipher)
            c+=1
        except: break
        
    print(cipher)

def main():
    pdf="file.pdf"
    dist=wordcounter(pdf)
    # print(dist)
    cipher="ybklypdyg byy"
    crack(dist,cipher)

main()