class Contact:
    def __init__(self,fn,ln,ph,addr,city,zipcode):
        self.fn=fn
        self.ln=ln
        self.ph=ph
        self.addr=addr
        self.city=city
        self.zipcode=zipcode
    
    def __lt__(self,other):
        if self.ln.strip().lower()==other.ln.strip().lower():
            return self.fn.strip().lower() < other.fn.strip().lower()
        return self.ln.strip().lower() < other.ln.strip().lower()
    
    def __str__(self):
        return f"{self.fn.capitalize()} {self.ln.capitalize()}\n {self.ph}\n {self.addr}\n {self.city} {self.zipcode}"
    
    def __repr__(self):
        return f"{self.fn.capitalize()},{self.ln.capitalize()},{self.ph},{self.addr},{self.city},{self.zipcode}"
