class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.__min_length = min_length
        self.__mails = mails
        self.__domains = domains
    
    def __validate_name(self, name):
        return len(name) >= self.__min_length
    
    def __validate_mail(self, mail):
        return mail in self.__mails
    
    def __validate_domain(self, domain):
        return domain in self.__domains
    
    def validate(self, email):
        try:
            username, domain_part = email.split('@')
            mail, domain = domain_part.split('.')
        except ValueError:
            return False
        
        is_name_valid = self.__validate_name(username)
        is_mail_valid = self.__validate_mail(mail)
        is_domain_valid = self.__validate_domain(domain)
        
        return is_name_valid and is_mail_valid and is_domain_valid

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.com"))  
print(email_validator.validate("georgios@gmail.net"))  
print(email_validator.validate("stamatito@abv.net"))  
print(email_validator.validate("abv@softuni.bg")) 