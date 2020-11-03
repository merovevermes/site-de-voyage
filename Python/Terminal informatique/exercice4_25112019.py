message=input("quels est le message : ")##le programme demender quels est le message a traduire
fichier = open('message.txt','w')#créé ou ouvre un fichier pour ecrire a l'interieur
fichier.write(message)##j'ecris le contenu de la variable dans le fichier
fichier.close()

clé=12 ##on crée une variable avec le pas du code césar
lettres = []##je crée une liste pour l'alphabet
for i in range (65,91): ##je répete l'action 26 fois
    lettres.append(chr(i))## je transforme le nombre i en caracter ascii correspondant

## je ne sais pas comment le decaller dans le sens inverse et tester tout les possibilité.
## et je ne sais pas comment utiliser le nouvelle alpabet pour ecrire le message decoder.

fichier = open ("message_decoder.txt","W")##je crée un fichier et je me preapre a ecrire dedans
fichier.write(message_decoder) ##j'ecris le message decoder a l'interieur
print('le message décoder est : ' +message_decoder)##j'affiche le message decoder
fichier.close##je ferme le fichier
