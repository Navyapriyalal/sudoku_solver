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

def check_row(boxes,box_num,row,ele):
    row_ind = (row-1)%3
    if box_num == 1 or box_num == 2 or box_num == 3:
        for i in range(0,3):
            if ele in boxes[i].box[row_ind]:
                return False
    elif box_num == 4 or box_num == 5 or box_num == 6:
        for i in range(3,6):
            if ele in boxes[i].box[row_ind]:
                return False
    elif box_num == 7 or box_num == 8 or box_num == 9:
        for i in range(6,9):
            if ele in boxes[i].box[row_ind]:
                return False
    else:
        print('Not Valid Box number')
        return
    return True

def check_col(boxes,box_num,col,ele):
    col_ind = (col-1)%3
    if box_num == 1 or box_num == 4 or box_num == 7:
        for i in range(0,7,3):
            for j in range(3):
                if boxes[i].box[j][col_ind] == ele:
                    return False
    elif box_num == 2 or box_num == 5 or box_num == 8:
        for i in range(1,8,3):
            for j in range(3):
                if boxes[i].box[j][col_ind] == ele:
                    return False
    elif box_num == 3 or box_num == 6 or box_num == 9:
        for i in range(2,9,3):
            for j in range(3):
                if boxes[i].box[j][col_ind] == ele:
                    return False
    else:
        print('Not Valid Box number')
        return
    return True

