## 🃏 Problem Statement: Blackjack Game

Design and implement a simple **Blackjack game** using Python.

Blackjack is a card game where the goal is to get a hand value as close to **21** as possible without exceeding it.

---

### 🎯 Game Rules

1. Cards have the following values:
   - **Number cards (2–10):** Face value  
   - **Face cards (Jack, Queen, King):** Value of 10  
   - **Ace:** Value of 11 or 1 (whichever is more beneficial)

2. The game is played between **one player** and the **computer (dealer)**.

3. Both player and dealer are initially dealt **two cards**.

4. The player can choose to:
   - **Hit** → draw another card  
   - **Stand** → keep current hand

5. The dealer must:
   - Keep drawing cards until the hand value is **17 or higher**

6. The game ends when:
   - A player’s hand value exceeds **21** (**Bust**)
   - Both player and dealer stand

---

### 🏆 Winning Conditions

- Player wins if:
  - Player’s score is **closer to 21** than the dealer’s without exceeding it
  - Dealer busts

- Dealer wins if:
  - Dealer’s score is **closer to 21** than the player’s without exceeding it

- If both have the same score:
  - The game is a **Draw**

---

In a standard Blackjack game, 52 cards are shuffled.

🃏 Details

4 suits: Hearts, Diamonds, Clubs, Spades

Each suit has 13 cards:
- Numbers 2–10 (9 cards)
- Jack, Queen, King (3 face cards)
- Ace (1 card)