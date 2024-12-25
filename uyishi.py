class a:
    def pp(self,v:str,g:str):
        c=3
        d=3
        if v=="steal":
            pass
        elif v=="share":
            c-=1
            d+=3
        
        if g=="share":
            d-=1
            c+=3
        
        return[c,d]

b=a()
print(b.pp("share","share"))