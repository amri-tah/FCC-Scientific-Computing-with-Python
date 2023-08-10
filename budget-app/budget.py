class Category:

  def __str__(self):
    output = ""
    output += "*" * ((30 - len(self.categ)) // 2) + self.categ + "*" * (
      (30 - len(self.categ)) // 2) + "\n"
    for item in self.ledger:
      output += item["description"][0:23].ljust(23) + str(
        format(float(item["amount"]), '.2f')).rjust(7) + "\n"
    output += "Total: " + str(format(float(self.balance), '.2f'))
    return output

  def __init__(self, c):
    self.expense = 0
    self.categ = c
    self.ledger = []
    self.balance = 0

  def deposit(self, amt, desc=""):
    self.ledger.append({"amount": amt, "description": desc})
    self.balance += amt

  def withdraw(self, amt, desc=""):
    if self.check_funds(amt):
      self.ledger.append({"amount": -amt, "description": desc})
      self.balance -= amt
      self.expense += amt
      return True
    return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.categ}")
      category.deposit(amount, f"Transfer from " + self.categ)
      return True
    return False

  def check_funds(self, amt):
    if amt > self.balance: return False
    return True


def create_spend_chart(categs):
  percent = []
  exp = []
  len_labels = 0
  labels = []
  for cat in categs:
    exp.append(cat.expense)
    if len(cat.categ) > len_labels:
      len_labels = len(cat.categ)
    labels.append(cat.categ)
  for amt in exp:
    per = math.floor((amt / sum(exp)) * 100)
    percent.append(per)

  out = "Percentage spent by category\n"
  for i in range(100, -1, -10):
    out += (str(i) + "|").rjust(4)
    for per in percent:
      if int(per) >= i:
        out += " o "
      else:
        out += " " * 3
    out += " \n"

  out += " " * 4 + "-" * (3 * len(categs) + 1) + "\n"

  labels = [label.ljust(len_labels, " ") for label in labels]
  for i in range(len_labels):
    out += "    "
    for label in labels:
      out += " " + label[i] + " "
    if i == len_labels - 1:
      out += " "
    else:
      out += " \n"

  return out
