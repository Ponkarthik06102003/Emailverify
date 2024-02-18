import re

def is_valid_email(email):
    # check if email address is valid
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True

def is_disposable_email(email):
    # get the domain name from the email
    domain = email.split('@')[-1]

    # check if the domain is a disposable email address provider
    disposable_domains = ['mailinator.com', 'guerrillamail.com', 'temp-mail.org', 'sharklasers.com']
    if domain in disposable_domains:
        return True
    return False


def email_features(email):
    # check if email address is valid
    if not is_valid_email(email):
        return "Invalid email address"

    # get the domain name from the email
    domain = email.split('@')[-1]

    # check if the email is a disposable email address
    is_disposable = is_disposable_email(email)

    # get the username from the email
    username = email.split('@')[0]

    # get the top-level domain from the domain
    tld = domain.split('.')[-1]

    # get the country code TLD from the domain (if available)
    cctld = None
    if len(domain.split('.')) == 2:
        cctld = domain.split('.')[0]

    # check if the email is from a popular free email provider
    is_free = False
    free_email_providers = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
    if domain in free_email_providers:
        is_free = True

    # return a dictionary of features
    features = {
        'email': email,
        'domain': domain,
        'username': username,
        'top_level_domain': tld,
        'country_code_tld': cctld,
        'is_free_email': is_free,
        'is_disposable_email': is_disposable,
        'is_valid_email': True
    }
    return features

# example usage
email = input("Enter email address: ")
print(email_features(email))
