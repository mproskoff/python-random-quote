def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #print(len(quotes))

#  for z in range(len(quotes)):
#    print(str(z+1)+": " + quotes[z])

  for num, qt in enumerate(quotes, start=1):
    print("Quote# {}: {}".format(num, qt))


  #print(quotes[len(quotes)-1])

if __name__== "__main__":
  main()

