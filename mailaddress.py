def mailsplit():
    mail = input("Please write your E-mail address:").strip()
    #print(type(mail))
    split = mail.split("@")
    print("Your E-mail username is %s,and your domain name is %s" % (split[0],split[1]))
def mailindex():
    mail = input("Please write your E-mail address:").strip()
    UserName = mail[0:mail.index("@")]
    DomainName = mail[mail.index("@")+1:]
    print("Your E-mail username is %s,and your domain name is %s" % (UserName, DomainName))

if __name__ == "__main__":
    mailsplit()
    mailindex()