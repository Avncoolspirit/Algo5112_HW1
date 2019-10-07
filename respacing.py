# TODO: Avnish Kumar, ak2626
# TODO: Rishabh Jain, 

# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to #print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)"%(str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) == bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):
    #TODO: YOUR CODE HERE
    #print "checking: " , string[i:j+1], "i ,j ", i,"", j 
    if is_word(string[i:j+1]):
        return RespaceTableCell(True, len(string[i:j+1])-1)   #check if word is true
    else:
        for split in range(0,j-i):               #loop to check if the substring when split corresponds to 2 words 
            if (T.get(i,i+split).value & T.get(i+split+1,j).value) :
                return RespaceTableCell(True, split)   
    return RespaceTableCell(False, None)

            
     


    
                  
# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):
    order = []
    for i in range(0,N):   # checking the diagonal which represents the single characters first and then moving up a diagonal
        for j in range(0,N-i):
            order.append((j,j+i))
    return order

# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
    string =s
    check =table.get(0,len(s)-1)         
    index = 0
    if check.value ==False:
        return None
    s_respaced=""
    while check.value :
        index += check.index+1
        word = string[0:check.index+1]  # cutting word from the split position
        string = string[check.index+1:len(s)] #Rest of the string
        
        s_respaced+= word    # add word to the output string 
        
        if index < len(s):
            s_respaced+=" "     # adding spaces after each word
            check =table.get(index,len(s)-1)  #move to the next element in the table
        else:
            break
    return s_respaced

if __name__ == "__main__":
    # Example usage.
    from dynamic_programming import DynamicProgramTable
    s = "glenndialtruckglennglen"
    wordlist = ["menu","turbo","york","cork","glen","haven","glenn","warm","dial","truck"]
    #print cell_ordering(len(s))
    D = DynamicProgramTable(len(s) , len(s) , cell_ordering(len(s)), fill_cell)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    print respace_from_table(s, D)
    
