class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial

    def deposer(self, montant):
        self.solde += montant
        print(f"votre depot de : {montant}CFA a ete effectuer avec succes \n. Nouveau solde est : {self.solde}CFA \n")

    def retirer(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print(f"vous avez retirer la somme de :{montant}CFA  dans votre compte.\n Nouveau solde est : {self.solde}CFA \n")
        else:
            print("Solde insuffisant.")

    def verifier_solde(self):
        print(f"Solde actuel : {self.solde}CFA \n")
    

compte = CompteBancaire(25000)  
compte.verifier_solde()      
compte.deposer(50000)            
compte.retirer(30000)           
compte.verifier_solde()       
