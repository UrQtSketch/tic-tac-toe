# import numpy as np

# board = np.zeros((3,3) ,dtype = int)
# print(board)

# def print_board(b):
#     symbols  = {0 : " ", 1: "X" , -1: "o"}
#     for r in range(3):
#         row = " | ".join(symbols[val] for val in b [r])
#         print(" "+ row)

#         if r <2:
#             print("---+----+---")

# def check_winner(b):
#     if 3 in np.sum(b, axis = 1) or 3 in np.sum(b, axis = 0):
#         return "X"
#     if -3 in np.sum(b, axis = 1) or -3 in np.sum(b, axis = 0):
#         return "O"
#     if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
#         return "X"
#     if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
#             return "O"
    

#     if not 0 in b:
#      return "draw"
#     return None


# current = 1

# print("=" * 50)
# print("welcome to our tic tac toe game: -")
# print("=" * 50)


# print_board(board)

# while True:

#  if current == 1:
#     player = "X"
#  else:
#     player = "O"

#  try:

#     row = int(input(f'{player} enter your row(0,1,2):'))
#     col = int(input(f'{player} enter your column(0,1,2):'))

#  except ValueError:
#      print("please enter only numbers:")
#      continue 
 
#  if row < 0 or row > 2 or col < 0 or col > 2:
#        print(" pls provide row and col between 0 to 2: -")

#  if board(row,col) != 0:
#        print("cell is already taken")    

#  board[row,col] = current 
#  print_board(board)

#  result = check_winner(board)

#  if result is not None:
#        if result =="draw":
#         print("game draw hogya hai")
#        else:
#           print(result, "wins")

#        break  


# if current == 1:
#        current = -1

# else:
#       current = 1

# print_board(board)







import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Tic-Tac-Toe",
    page_icon="🎮",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #101827;
    color: white;
}
h1, h2, p {
    text-align: center;
}
div.stButton > button {
    min-height: 75px;
    font-size: 25px;
    font-weight: bold;
    border-radius: 12px;
    border: 1px solid #334155;
    background: #1e293b;
    color: white;
}
div.stButton > button:hover {
    border-color: #38bdf8;
    color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1

def check_winner(b):
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return "X"

    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return "O"

    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"

    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"

    if not np.any(b == 0):
        return "Draw"

    return None

st.title("🎮 TIC-TAC-TOE")
st.caption("NUMPY EDITION • TWO PLAYERS")

board = st.session_state.board
current = st.session_state.current
result = check_winner(board)

if result == "X" or result == "O":
    st.success(f"🏆 Player {result} wins!")
elif result == "Draw":
    st.info("🤝 It's a draw!")
else:
    player = "X" if current == 1 else "O"
    st.subheader(f"Player {player}'s turn")

# Clickable 3 × 3 board
for r in range(3):
    cols = st.columns(3, gap="small")

    for c in range(3):
        value = board[r, c]
        symbol = "X" if value == 1 else "O" if value == -1 else "·"

        if cols[c].button(
            symbol,
            key=f"cell_{r}_{c}",
            use_container_width=True,
            disabled=(value != 0 or result is not None)
        ):
            new_board = board.copy()
            new_board[r, c] = current
            st.session_state.board = new_board

            new_result = check_winner(new_board)

            if new_result is None:
                st.session_state.current = -current

            st.rerun()

st.divider()

if st.button("🔄 New Game", use_container_width=True):
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.rerun()


