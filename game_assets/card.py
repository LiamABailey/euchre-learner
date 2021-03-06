from dataclasses import dataclass

from .euchre import CARD_FACES, SUIT_DESCRIPTOR, FACE_DESCRIPTOR, JACK, LEFT_SUIT

@dataclass
class Card:
    """
    Class for storing card information
    """
    suit: int
    face: int

    def __str__(self):
        return (f"{FACE_DESCRIPTOR[self.face].capitalize()} of "
                f"{SUIT_DESCRIPTOR[self.suit].capitalize()}s")

    def __eq__(self, other):
        """
        Equality implementation
        """
        if isinstance(other, Card):
                return (self.suit == other.suit) and\
                        (self.face == other.face)
        return False

    def _is_left_bar(self, trump: int) -> bool:
        """
        Evaluate if the card is specifically the left bar of a given
        trump suit

        Parameters
        ----------
            trump : int
                The trump suit, from euchre.SUITS

        Returns
        -------
            bool : True if is left bar, false otherwise
        """
        if self.face == JACK and self.suit == LEFT_SUIT[trump]:
            return True

    def is_trump(self, trump: int) -> bool:
        """
        Evaluate if the card is in the trump suit

        Parameters
        ----------
            trump : int
                The trump suit, from euchre.SUITS

        Returns
        -------
            bool : True if member, false otherwise
        """
        if self.suit == trump or self._is_left_bar(trump):
            return True
        return False

    def lt_card(self, other: 'Card', trump: int, lead: int) -> bool:
        """
        Check if this card is of lower value than another card, given
        the trump suit and leading suit

        Parameters
        ----------
            other : Card
                The card compared

            trump : int
                The trump suit, from euchre.SUITS

            trump : int
                The  suit that started the trick, from euchre.SUITS

        Returns
        -------
            bool : True if self < other, False otherwise
        """
        lt = True
        # this card is trump, other isn't
        if self.is_trump(trump) and not other.is_trump(trump):
            return False
        # this card isn't trump, other is
        elif not self.is_trump(trump) and other.is_trump(trump):
            return True
        #either both aren't, or are trump
        else:
            if self.is_trump(trump):
                # if either is a jack, special befahvoir
                if self.face == JACK and other.face != JACK:
                    return False
                elif self.face != JACK and other.face == JACK:
                    return True
                elif self.face == JACK and other.face == JACK:
                    if self._is_left_bar(trump):
                        return True
                    return False
                else:
                    return CARD_FACES.index(self.face) < CARD_FACES.index(other.face)
            else:
                if self.suit == lead and other.suit != lead:
                    return False
                # this card isn't lead, other is
                elif self.suit != lead and other.suit == lead:
                    return True
                else:
                    # this is the rare case where neither card lead, or is
                    # in the trump suit. Neither of these cards can wind the
                    # trick, so we don't care about the evaluation.
                    return CARD_FACES.index(self.face) < CARD_FACES.index(other.face)
