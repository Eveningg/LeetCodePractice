class Solution:
    def distinctIntegers(self, n: int) -> int:
        
        # Initialize the set to keep track of distinct numbers on the board
        board = {n}
        
        # Continue the loop until a repeated board configuration is found
        while True:
            # Initialize a set to store new numbers that satisfy the condition
            new_nums = {i for x in board for i in range(1, n+1) if x % i == 1}

            # Check if the new numbers are already present on the board
            if new_nums.issubset(board):
                break
            
            # Add the new numbers to the board
            board |= new_nums
        
        # Return the count of distinct integers on the board
        return len(board)