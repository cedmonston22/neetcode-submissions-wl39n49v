class Solution:
    def arrangeCoins(self, n: int) -> int:
        #given number of coins
        #just keep adding stacks of coins i + 1 until you run out
        num_case = 0
        coins_avail = n

        
        while coins_avail - num_case > 0:
            num_case += 1
            coins_avail -= num_case

        return num_case
