def dechiffrage(caractere, cle_cesar):
    code = ord(caractere) - 65
    code = (code - cle_cesar) % 26
    code = code + 65
    return chr (code)


def cesar(chaine,cle_cesar):
    nouvelle_chaine = ""
    for caractere in chaine:
        nouvelle_chaine = nouvelle_chaine + dechiffrage ( caractere, cle_cesar )
    return nouvelle_chaine


cle_cesar=int(input("veuillez saisir le code : "))
chaine=input("quels est la phrase a déchiffrer ?")

fichier = open("message_decoder.txt","w")## je crée un fichier message_coder.txt
fichier.write(cesar(chaine,cle_cesar))##j'ecrit le message coder dans le fichier
fichier.close()##je ferme le fichier
print('le message chiffré est:' +cesar(chaine,cle_cesar)) ##j'affiche la variable.

