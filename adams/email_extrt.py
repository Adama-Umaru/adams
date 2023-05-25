import re
import requests

def extract_phone_numbers(text):
    phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
    phone_numbers = re.findall(phone_regex, text)
    return phone_numbers

def extract_email_addresses(text):
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    email_addresses = re.findall(email_regex, text)
    return email_addresses

def extract_links(text):
    link_regex = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    links = re.findall(link_regex, text)
    return links

def save_emails_to_file(emails):
    with open("extracted_emails.txt", "w") as file:
        file.write("\n".join(emails))

def main():
    url = input("Enter the website URL: ")
    response = requests.get(url)
    text = response.text

    phone_numbers = extract_phone_numbers(text)
    email_addresses = extract_email_addresses(text)
    links = extract_links(text)

    print("Phone Numbers:")
    for phone_number in phone_numbers:
        print(phone_number)

    print("Email Addresses:")
    for email_address in email_addresses:
        print(email_address)

    print("Links:")
    for link in links:
        print(link)

    save_emails_to_file(email_addresses)
    print("Extracted email addresses saved to 'extracted_emails.txt'.")

if __name__ == "__main__":
    main()




