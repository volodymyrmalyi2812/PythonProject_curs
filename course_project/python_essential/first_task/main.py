import random
import sys
from abc import ABC, abstractmethod
from enum import Enum


class Suit(Enum):
    HEARTS = "♥"
    DIAMONDS = "♦"
    CLUBS = "♣"
    SPADES = "♠"


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit.value}"

    def points(self):
        if self.rank in ("J", "Q", "K"):
            return 10
        if self.rank == "A":
            return 11
        return int(self.rank)


class Deck:
    def __init__(self):
        ranks = [str(number) for number in range(2, 11)] + ["J", "Q", "K", "A"]
        self.cards = [Card(rank, suit) for suit in Suit for rank in ranks]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Participant(ABC):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def take_card(self, deck):
        self.cards.append(deck.draw())

    def score(self):
        total = sum(card.points() for card in self.cards)
        aces = sum(card.rank == "A" for card in self.cards)
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total

    def show_cards(self):
        return " ".join(str(card) for card in self.cards)

    @abstractmethod
    def turn(self, deck):
        pass


class Player(Participant):
    def turn(self, deck):
        while self.score() < 21:
            print(f"\nВаші карти: {self.show_cards()} (очки: {self.score()})")
            answer = input("1 - Взяти карту, 2 - Зупинитися: ").strip()
            if answer == "1":
                self.take_card(deck)
            elif answer == "2":
                break
            else:
                print("Введіть 1 або 2.")


class Dealer(Participant):
    def turn(self, deck):
        while self.score() < 17:
            self.take_card(deck)


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Гравець")
        self.dealer = Dealer("Дилер")

    def result(self):
        player_score = self.player.score()
        dealer_score = self.dealer.score()
        print(f"\nВаші карти: {self.player.show_cards()} (очки: {player_score})")
        print(f"Карти дилера: {self.dealer.show_cards()} (очки: {dealer_score})")

        if player_score > 21:
            print("Перебір! Ви програли.")
        elif dealer_score > 21:
            print("У дилера перебір. Ви виграли!")
        elif player_score > dealer_score:
            print("Вітаємо! Ви виграли!")
        elif player_score < dealer_score:
            print("Дилер виграв.")
        else:
            print("Нічия!")

    def play(self):
        for _ in range(2):
            self.player.take_card(self.deck)
            self.dealer.take_card(self.deck)

        print("\n=== BLACKJACK ===")
        print(f"Карти дилера: {self.dealer.cards[0]} [?]")
        print(f"Ваші карти: {self.player.show_cards()} (очки: {self.player.score()})")

        if self.player.score() == 21 or self.dealer.score() == 21:
            self.result()
            return

        self.player.turn(self.deck)
        if self.player.score() <= 21:
            self.dealer.turn(self.deck)
        self.result()


def run_tests():
    deck = Deck()
    assert len(deck.cards) == 52
    assert len({str(card) for card in deck.cards}) == 52

    player = Player("Тест")
    player.cards = [Card("A", Suit.HEARTS), Card("9", Suit.SPADES)]
    assert player.score() == 20
    player.cards.append(Card("5", Suit.CLUBS))
    assert player.score() == 15
    player.cards = [Card("A", Suit.HEARTS), Card("A", Suit.SPADES), Card("9", Suit.CLUBS)]
    assert player.score() == 21
    player.cards = [Card("K", Suit.HEARTS), Card("Q", Suit.SPADES), Card("5", Suit.CLUBS)]
    assert player.score() == 25

    dealer = Dealer("Дилер")
    dealer.cards = [Card("10", Suit.HEARTS), Card("7", Suit.SPADES)]
    cards_before = len(deck.cards)
    dealer.turn(deck)
    assert dealer.score() == 17
    assert len(deck.cards) == cards_before

    print("Усі тести пройдено!")


def main():
    while True:
        print("\n1 - Грати в BlackJack")
        print("2 - Правила")
        print("0 - Вихід")
        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            Game().play()
        elif choice == "2":
            print("Мета - набрати більше очок, ніж дилер, але не більше 21.")
            print("Карти від 2 до 10 мають свою вартість, J, Q, K - 10 очок.")
            print("Туз дає 11 або 1 очко. Дилер бере карти до 17 очок.")
        elif choice == "0":
            print("До зустрічі!")
            break
        else:
            print("Оберіть 1, 2 або 0.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        run_tests()
    else:
        main()
