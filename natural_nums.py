def run():
    #dictionary ={i: i**3 for i in range(1,101)}
    #print (dictionary)
   #my_dict = {}
   #for i in range (1,101):
    #   if i % 3 != 0:
    #       my_dict[i] = i**3 
   #print (my_dict)
   #dictionary={i: i**3 for i in range(1,101) if (i % 3 !=0)}
   #print(dictionary)
   dictionary= {i: round(i**0.5,2) for i in range(1,1001)}
   print(dictionary)

if __name__ == "__main__":
    run()