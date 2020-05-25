import random

def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #print(len(quotes))

#  for z in range(len(quotes)):
#    print(str(z+1)+": " + quotes[z])

  last = len(quotes)-1
  rnd = random.randint(0,last)

  print(quotes[rnd])

if __name__== "__main__":
  main()

