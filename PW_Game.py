import random

class Card:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.name)

class Deck:
    def __init__(self, kittens=4, regulars=16, yt=4, nmp=6, rtp=4, factory=4, atk=4, skp=4, shfle=4, clr=5):
        self.regulars = regulars
        self.yt = yt
        self.nmp = nmp
        self.rtp = rtp
        self.factory = factory
        self.atk = atk
        self.skp = skp
        self.shfle = shfle
        self.clr = clr

        #NOT SURE HOW TO ADD THE NEW CARDS INTO "self.types" without making the line too long
        self.types = ['Grace Davidson Factory']*self.factory + ['Regular']*self.regulars + ['Yeet']*self.yt
        self.actual_cards = [Card(i) for i in self.types]

    def shuffle(self):
        random.shuffle(self.actual_cards)

    def get_top_card(self):
        card_to_be_returned = self.actual_cards.pop(0)
        return card_to_be_returned

    def get_four_cards(self): #for dealing the initial hand to each player
        four_cards = []
        for i in range(4):
            card_name_list = []
            for j in range(len(self.actual_cards)):
                card_name_list.append(self.actual_cards[j].name)
            regular_card_index = card_name_list.index('Regular')
            regular_card = self.actual_cards.pop(regular_card_index)
            four_cards.append(regular_card)
        return four_cards

class Player:
    def __init__(self, ID, hand):
        self.player_ID = ID
        self.hand = hand
        self.alive = True

    def __str__(self):
        return self.player_ID

    def __repr__(self):
        return str(self.player_ID)

class ExplodingKittens():
    def __init__(self,num_players):
        self.num_players = num_players
        self.player_list = []

    def start_game(self): #set up game for first round of card draws
        self.deck_of_cards = Deck(self.num_players - 1, 53 - self.num_players)
        for player_ID in range(1, self.num_players + 1): #start w Player 1
            cards_for_player = self.deck_of_cards.get_four_cards() #Deal card to player
            player_ID = "Player " + str(player_ID)
            new_player = Player(player_ID, cards_for_player) #Save player ID and card
            self.player_list.append(new_player)
        self.deck_of_cards.shuffle()

    def play_round(self):
        for i in range(len(self.player_list)):
            top_card = self.deck_of_cards.get_top_card()
            print('{} drew {}'.format(self.player_list[i], top_card))
            if str(top_card) == 'Grace Davidson Factory':
                print('{} is dead!'.format(self.player_list[i]))
                self.player_list[i].alive = False
            alive = [self.player_list[j].alive for j in range(len(self.player_list))]
            if sum(alive) == 1:
                winner_index = alive.index(True)
                return '{} won the game!'.format(self.player_list[winner_index])

        player_list = [] #update player_list with only living players
        for i in range(len(self.player_list)):
            if self.player_list[i].alive:
                player_list.append(self.player_list[i])
        self.player_list = player_list

    def decide_winner(self):
        while len(self.player_list) > 1:
            outcome = self.play_round()
            if outcome is not None:
                print(outcome)
                break

if __name__=="__main__":
    """run this code when executing module as a program 
    and not when importing its classes"""
    game = ExplodingKittens(5)
    game.start_game()
    print(game.player_list)
    game.decide_winner()

""""" This is for the screen and visuals of the game
import pygame

#Initialize the pygame
pygame.init()

#Create the screen
scree = pygame.display.set_mode((1500, 800))

#Tittle and Icon
pygame.display.set_caption("Pollution Who")
icon = pygame.image.load('biohazard.png')
pygame.display.set_icon(icon)

#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB - Red, Green, Blue

"""""
