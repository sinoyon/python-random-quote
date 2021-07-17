def main():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes[10] = f.readlines()
  f.close()

  print(quotes[0])


