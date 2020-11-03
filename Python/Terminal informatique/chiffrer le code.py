cle_cesar=int(input("veuillez saisir le code : "))
nouvelle_chaine = ""

fichier = open('message.txt','r') ##j'ouvre le fichier message.txt qui continet la phrase a chiffrer
chaine= fichier.read()##je mets dans une liste le contenu du fichier
fichier.close()##je ferme le fichier

def chiffrage(caractere,cle_cesar):
    code = ord(caractere) - 65
    code = (code + cle_cesar) % 26
    code = code + 65
    return chr(code)


def cesar(chaine, cle_cesar):
    nouvelle_chaine = ""
    for caractere in chaine:
        nouvelle_chaine = nouvelle_chaine + chiffrage(caractere, cle_cesar)
    return nouvelle_chaine


fichier = open("message_coder.txt","w")## je crée un fichier message_coder.txt
fichier.write(cesar(chaine, cle_cesar))##j'ecrit le message coder dans le fichier
fichier.close()##je ferme le fichier
print('le message chiffré est:' +cesar(chaine,cle_cesar)) ##j'affiche la variable.


