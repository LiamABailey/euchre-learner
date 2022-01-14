from abc import ABC
from typing import List, Tuple

from .card import Card
from .hand import Hand
from .trick import Trick


class Player(ABC):
    """
    The basic player definition
    """

    def __init__(self, id: int):
        """
        Parameters
        ----------
            id : int
                The player's ID
        """
        self.player_id = id
        self.seat = None
        self.cards_held = []

    def assign_seat(self, seat_ix:int):
        """
        Assign the seat postion to the player
        """
        self.seat = seat_ix


    def receive_cards(self, cards: List[Card]):
        """
        receive a 'hand' of five cards

        Paramters
        ---------
            cards: the 5 cards for the player for the hand

        Returns
        -------
            None
        """
        if len(cards) !=5
            raise ValueError("Must receive five cards")
        self.cards_held = cards

    @abstractmethod
    def exchange_with_kitty(self, kitty_card: Card) -> None:
        """
        Method controlling dealer's adding of kitty_card to the hand,
        and discarding of a card

        Parameters
        ----------
            kitty_card : card.Card
                The face-up card in the kitty added to hand

        Returns
        -------
            None
        """
        raise NotImplementedError

    @abstractmethod
    def play_card(self, active_hand: Hand, active_trick: Trick, dealer_seat: int, lead_seat: int):
        """
        Given the known information about the game:
            - played tricks
            - the trick currently being played
            - the kitty card (and if it was passed)
            - the face-up card in the dealer's hand
            - the dealer's seat
            - the seat of the player who starts the trick
            - the player's current hand
         selects a card to play, removing it from the player's hand and
         returning it

        Parameters
        ----------
            active_hand : Hand.hand
                The hand currently being played

            active_trick : Trick.trick
                The trick currently being played

            dealer_seat : int
                The seat of the dealer player, 0-3

            lead_seat : int
                The seat of the player who started the trick

        Returns
        -------
            Card.card : The card played by the player (popped from 'cards_held')

        """
        raise NotImplementedError

    @abstractmethod
    def select_kitty_pickup(self, kitty_card : Card, is_dealer: bool,
                            dealer_is_team_member: bool) -> bool:
        """
        Evaluates the face-up card in the kitty, and
        provides a decision as to if the dealer should pick up the card

        Parameters
        ----------
            kitty_card : card.Card
                The face-up card in the kitty

            is_dealer : bool
                If the player is in the dealer's seat

            is_team_member : bool
                If the dealer is the player's team member

        Returns
        -------
            bool : True if the card is to be picked up, false otherwise
        """
        raise NotImplementedError

    @abstractmethod
    def select_trump(self, passed_suit: string, is_dealer: bool) -> Tuple[str, bool]:
        """
        The player evaluates the hand for the best suit to play. If
        not the dealer, may pass. Will not select the suit that was
        passed during the face-up kitty round.

        Parameters
        ----------
            passed_suit : string
                The suit-string passed in the kitty round (turned down)

            is_dealer : bool
                If the player is in the dealer's seat (is stuck)

        Returns
        -------
            str : The selected suit, if any
            bool : True if suit selected, false otherwise.
        """
        raise NotImplementedError