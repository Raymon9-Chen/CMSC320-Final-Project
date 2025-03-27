from pokemontcgsdk import RestClient
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

RestClient.configure('9a6c471e-5ccd-4def-9199-9ddf68c00d7c')


cards = Card.find('xy1-1')

print(cards.tcgplayer)