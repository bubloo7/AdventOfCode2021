class board:

    # Constructor, expects 2D array representing bingo board 
    # O(n^2)   
    def __init__(self, arrArr):
        self.debug = []

        self.n = len(arrArr)
        self.bingo_ = False

        for i in range(self.n):
            for j in range(self.n):
                self.debug.append([arrArr[i][j], False])
        self.nums = {}
        self.rows = [0, 0, 0, 0, 0]
        self.cols = [0, 0, 0, 0, 0]
        for i in range(self.n):
            for j in range(self.n):
                self.nums[arrArr[i][j]] = i*self.n + j

    # Debugging method 
    # O(n^2)
    def __str__(self):
        ans = ""
        red = '\033[1m' + '\033[91m'
        bad = f'\033[0m'
        for i in range(self.n):
            for j in range(self.n):
                if self.debug[i*self.n + j][1]:
                    ans += red + str(self.debug[i*self.n + j][0]) + bad + " "
                else: 
                    ans += str(self.debug[i*self.n + j][0]) + " "
            ans += '\n'


        ans += "rows: " + str(self.rows) + '\n'
        ans += "cols: " + str(self.cols) + '\n'
        if(self.bingo()):
            ans += "Bingo!!!"
        else:
            ans += "No bingo ):"
        

        
        return ans

    # Checks if the board has bingo
    # O(1)
    def bingo(self):
        return self.bingo_
    
    # Adds number to board
    # O(1)
    def num(self, num):
        if num in self.nums:
            ind = self.nums[num]
            col = ind % self.n
            row = int(ind / self.n)

            self.debug[ind][1] = True

            self.cols[col]  += 1
            self.rows[row]  += 1
            self.nums.pop(num)
            if self.cols[col] == self.n or self.rows[row] == self.n:
                self.bingo_ = True

