# your code goes here!
import re 

class EmailAddressParser:
    def __init__(self, email_addresses):
        if isinstance(email_addresses, str):
            self.email_addresses = email_addresses
        else:
            raise ValueError("Email_addresses must be of str class.")

    def parse(self):
        email_finding_pattern = re.compile(r"\s*[, ]\s*")
        email_addresses = email_finding_pattern.split(self.email_addresses)
        valid_email_addresses = [address for address in email_addresses if re.match(r"[^@]+@[^@]+\.[^@]+", address)]
        return sorted(valid_email_addresses)