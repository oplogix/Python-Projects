# 🎲 CLI Poker Game (Python)

A simple **command-line Texas Hold’em Poker** game written in Python.  
Players can bet, check, raise, fold, peek at their hand or the board, and even exit the game mid-round.  
The game automatically detects if only one player is left and declares them the winner.  

---

## 🚀 Features
- Standard **52-card deck** with shuffle
- Supports **2–6 players**
- Deal **hole cards + flop + turn + river**
- Betting system with:
  - ✅ Check  
  - ✅ Call  
  - ✅ Raise  
  - ✅ Fold  
  - ✅ Hand check (`hand`)  
  - ✅ Board check (`board`)  
  - ✅ Exit game (`exit`)  
- Automatic win if only one player remains  

---

## 📦 Requirements
- Python **3.8+**
- No external libraries needed (uses only `random`)

---

## ▶️ How to Play
1. Clone the repo or download `play.py`
2. Run in terminal:
   ```bash
   python play.py
3. Enter the number of players (2-6)
4. Each player takes turns with options:
- hand → show your hole cards
- board → show community cards revealed so far
- check → pass the action if no bets are placed
- call → match the current bet
- raise → increase the current bet
- fold → drop out of the hand
- exit → leave the game entirely

## HAVE FUN!
