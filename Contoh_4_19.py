#Contoh_4_19
def kos(paparan):
    print(paparan)
    h=float(input())
    return h
def main():
    h1=kos("Masukkan harga kos RM:")
    h2=kos("Masukkan harga jualan RM:")
    if h1==h2:
        print("Tiada keuntungan.")
    elif h2 > h1:
        print("Peratus keuntungan:",((h2-h1)/h1)*100,"%")
    else:
        print("Peratus kerugian:",((h1-h2)/h1)*100,"%")
if __name__=="__main__":
  main()
