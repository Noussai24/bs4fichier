import requests
from bs4 import BeautifulSoup

# Je veux créer une fonction pour vérifier si une URL est accessible.
# Cela me permettra de savoir si je peux procéder au scraping de la page.
def verifier_url(url):
    # Je veux envoyer une requête HTTP GET à l'URL.
    # Cela simule une visite sur le site web comme le ferait un navigateur.
    response = requests.get(url)
    
    # Je veux vérifier le code de statut de la réponse HTTP pour évaluer le résultat de la requête.
    # Un code de statut de 200 signifie que la requête a été réussie et que la page est accessible.
    if response.status_code == 200:
        print("OK - La page a été chargée avec succès.")
        return True
    else:
        print("URL bloquée ou inaccessible pour une autre raison.")
        return False

# Je veux créer une fonction pour obtenir la liste des noms de films depuis une page Allociné.
# Cette fonction sera utilisée pour extraire et afficher les noms des films.
def liste_films(url):
    # Je veux m'assurer que l'URL est accessible avant de tenter le scraping.
    if not verifier_url(url):
        return []
    
    # Je veux récupérer le contenu HTML de la page pour l'analyse.
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Je veux sélectionner les éléments de la page qui contiennent les images des films.
    # J'ai déterminé que les vignettes des films sur Allociné utilisent la classe 'thumbnail-img'.
    film_elements = soup.select('img.thumbnail-img')
    
    # Je veux extraire les noms des films en utilisant l'attribut 'alt' des balises <img>.
    # Je veux également nettoyer le nom en enlevant la partie 'Bande-annonce VF' si elle est présente.
    film_names = [img['alt'].split(" Bande-annonce")[0] for img in film_elements if " Bande-annonce" in img['alt']]
    
    # Je veux retourner la liste des noms de films.
    return film_names

# Je veux définir l'URL de la page Allociné à partir de laquelle je vais récupérer les noms des films.
url = "https://www.allocine.fr/film/"

# Je veux appeler la fonction 'liste_films' et afficher les noms des films que je récupère.
films = liste_films(url)
for film in films:
    print(film)