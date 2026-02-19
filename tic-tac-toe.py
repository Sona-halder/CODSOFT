def print_board(board):
    """Display clean X/O board - no numbers"""
    for i in range(3):
        row = f" {board[i*3] or ' '} | {board[i*3+1] or ' '} | {board[i*3+2] or ' '} "
        print(row)
        if i < 2:
            print("-----------")

def is_winner(board, player):
    """Check if player has won"""
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def is_full(board):
    """Check if board is full (draw)"""
    return " " not in board

def available_moves(board):
    """Get list of empty positions"""
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(board, player, original_player):
    """Minimax algorithm - unbeatable AI"""
    if is_winner(board, original_player):  # AI wins
        return 10
    if is_winner(board, "O"):              # Human wins
        return -10
    if is_full(board):                     # Draw
        return 0
    
    if player == "X":  # AI maximizing
        best_score = -float('inf')
        for move in available_moves(board):
            board[move] = "X"
            score = minimax(board, "O", original_player)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:  # Human minimizing
        best_score = float('inf')
        for move in available_moves(board):
            board[move] = "O"
            score = minimax(board, "X", original_player)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    """AI finds perfect move"""
    best_score = -float('inf')
    move = None
    original_player = "X"
    
    for m in available_moves(board):
        board[m] = "X"
        score = minimax(board, "O", original_player)
        board[m] = " "
        if score > best_score:
            best_score = score
            move = m
    return move

def play_game():
    """Main game loop - clean display"""
    board = [" "] * 9
    print("🎮 Tic-Tac-Toe vs Unbeatable AI (X)")
    print("📍 Enter moves 1-9:")
    print("1|2|3")
    print("4|5|6")
    print("7|8|9\n")
    
    current_player = "O"  # You start as O
    
    while True:
        print_board(board)
        print()
        
        if current_player == "O":  # Your turn
            try:
                move = int(input("Your move (1-9): ")) - 1
                if move not in available_moves(board):
                    print("❌ Invalid! Pick empty spot 1-9.")
                    continue
                board[move] = "O"
            except:
                print("❌ Enter number 1-9 only!")
                continue
        else:  # AI turn
            move = best_move(board)
            board[move] = "X"
            print(f"🤖 AI plays at {move+1}")
        
        # Check win conditions
        if is_winner(board, "O"):
            print_board(board)
            print("🎉 YOU WIN! (Rare against perfect AI!)")
            break
        elif is_winner(board, "X"):
            print_board(board)
            print("🤖 AI WINS! Perfect minimax play.")
            break
        elif is_full(board):
            print_board(board)
            print("🤝 DRAW! Perfect game from both sides.")
            break
            
        current_player = "X" if current_player == "O" else "O"

if __name__ == "__main__":
    play_game()
