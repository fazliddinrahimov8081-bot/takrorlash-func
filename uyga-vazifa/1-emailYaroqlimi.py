def email_yaroqlimi(e):
    return (
        e.count("@") == 1 and
        e.split("@")[0] !="" and
        "." in e.split("@")[1] and
        all(ch.isalnum() or ch in "._@" for ch in e)
    )
print(email_yaroqlimi("john@gmail.com"))   
print(email_yaroqlimi("@jon.gmail.ru"))    
print(email_yaroqlimi("ali.hotmail.ru")) 