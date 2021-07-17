def main():

  f = open("quotes.txt")
  quotes[0] = f.readlines()
  f.close()

  print(quotes[0])


