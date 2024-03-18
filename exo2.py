print("entrez votres age") 
age=1
while True:
   # age=int(input("votre age",))
    try:
        age=int(input("votre age :"))
        if age > 0 :
            if age < 0 :
                print("impossible d avoir age negatif")
            elif age >= 18:
                print("vous ete Majeur")
            elif age < 18 :
                print("nous etes munieur")
            break
    except ValueError :
        print("impossible de faire cette operation")
        
        
    
      #  if age < 0 :
        #    print("impossible d avoir age negatif")
        #elif age >= 18:
          #   print("vous ete Majeur")
        #elif age < 18 :
         #   print("nous etes munieur") 
       #      break
  #  except valueError:
       #       print("une erreur ce produit")