import re
def parse_email(email):
  pattern = r'^[a-zA-Z][\w.-]*@(.+)'
  match = re.match(pattern, email)
  if match:
    username = email.split('@')[0]
    domain = match.group(1)
    return username, domain
  else:
    return None, None
def main():
  email = input("Введите ваш email: ")
  username, domain = parse_email(email)
  if username and domain:
    print(f"Имя пользователя: {username}")
    print(f"Доменное имя: {domain}")
  else:
    print("Некорректный формат email.")
if __name__ == "__main__":
  main()

