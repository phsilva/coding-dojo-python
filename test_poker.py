
def testCard():
    c = Card("4D")
    assert c.num == 4
    assert c.kind == Card.DIAMONDS

def testHand():
    cards = [Card('3D'), Card('4H')]
    hand = Hand(cards)

    assert hand.cards[0].num == 3
    assert hand.cards[0].kind == Card.DIAMONDS

    assert hand.cards[1].num == 4
    assert hand.cards[1].kind == Card.HEARTS

class Card:
    DIAMONDS = 3
    HEARTS = 2

    def __init__(self, c):
        self.num = to_num(c[0])
        self.kind = to_naipe(c[1])

class Hand:

    def __init__(self, cards):
        self.cards = []
        for card in cards:
            self.cards.append(card)

def testePoker():
   hand1 = Hand([Card('3D'), Card('2H')])
   hand2 = Hand([Card('2D'), Card('8D')])
   poker = Poker()
   assert poker.play(hand1,hand2) == hand1

class Poker:

    def play(self,hand1,hand2):
        card1 = hand1.cards[0]
        card2 = hand2.cards[0]

        if card1.num > card2.num:
            return hand1
        else:
            return hand2





# def test_poker():
#     assert poker('2D', 'AC') == 2
#     assert poker('TD','8D') == 1
#     assert poker('3D','3S') == 1
#     assert hand(['3D', '3S'], ['TD', '8D']) == 1


maos = {
    'par': 1
}

def hand(hand1, hand2):
    c1 = combination(hand1)
    c2 = combination(hand2)


    return

def combination(hand):
    num1, num2 = to_num(hand[0]), to_num(hand[1])
    if num1 == num2:
        return ('par', num1)

    return ('alta', )

def poker(carta1, carta2):
    num1, naipe1 = carta1[0], carta1[1]
    num2, naipe2 = carta2[0], carta2[1]

    if to_num(num1) > to_num(num2):
        return 1
    elif to_num(num1) == to_num(num2):
        if to_naipe(naipe1) > to_naipe(naipe2):
            return 1
    return 2

def to_num(num):
    if num == 'T':
        return 10
    if num == 'J':
        return 11
    elif num == 'Q':
        return 12
    elif num == 'K':
        return 13
    elif num == 'A':
        return 14
    else:
        return int(num)

def to_naipe(naipe):
    ordem = 'CSHD'
    return ordem.index(naipe)
