


print("enter the plain text:")
p=list(input())
print("enter key which should be an integer:")
key=int(input())
def encryption():
    s=[]
    i=0
    while(i<len(p)):
        s.insert(i,int(int(ord(p[i])+key)%97))
        i=i+1       
    return s 

def decryption():
    c=encryption()
    print("the received cipher text is")
    i=0
    s=""
    while(i<len(c)):
        s=s+chr(c[i]+97) 
        i=i+1   
    l=[]
    i=0
    while(i<len(c)):
        l.insert(i,chr(c[i]+97-key))
        i=i+1
    print("the retrived plaintext is:")
    print(l)    
    
    
def shift():
    encryption()
    decryption()
    
    
shift()    

