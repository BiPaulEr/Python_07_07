import logging
import random

livres_logger = logging.getLogger("livres")
transaction_logger = logging.getLogger("transactions")

livres_logger.setLevel(logging.WARNING)
transaction_logger.setLevel(logging.WARNING)

stream_handler = logging.StreamHandler()
livres_logger.addHandler(stream_handler)
transaction_logger.addHandler(stream_handler)

bibliotheque = {}

def add_book(title):
    rand_int = random.randint(0, 100)
    if rand_int < 90:
        bibliotheque[title] = True
        livres_logger.info(f"Nouveau livre {title} ajoute a la biliotheque")
    else:
        livres_logger.warning(f"Echec ajout livre {title}")

def process_transaction(user_id, book_id):
    is_present = bibliotheque.get(book_id, None)
    if not is_present:
        transaction_logger.warning(f" Utilisateur {user_id} can't buy {book_id} not present in bibliotheque")
        return
    if not isinstance(is_present, bool):
        transaction_logger.warning(f" Utilisateur {user_id} can't buy {book_id} already buy by {is_present}")
        return
    
    bibliotheque[book_id] = user_id
    transaction_logger.info(f" Utilisateur {user_id} buy {book_id}")

livres = ["Livre_"+str(i).zfill(2) for i in range(1, 20)]
users = ["User_"+str(i) for i in range(1, 10)]

for livre in livres:
    add_book(livre)

for user in users:
    process_transaction(user, livres[random.randint(0, len(livres) -1)])