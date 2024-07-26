class Box:
    def __init__(self,matrix,box_num):
        '''
        box is a 3x3 matrix 
        empty is the number of empty cells in the box
        '''
        self.box = matrix
        self.empty = self.num_empty()
        self.box_num = box_num
    
    #check_box function for 3x3 box
    def is_safe(self,ele):
        '''
        This checks whether we can place
        an element/number(1-9) in a box
        It does not allow duplicates 
        within a box
        '''
        for row in self.box:
            if ele in row:
                return False
        return True

    def num_empty(self):
        '''
        Counts the number of empty cells
        in the box
        '''
        count = 0
        for i in self.box:
            for j in i:
                if j==0:
                    count+=1
        return count