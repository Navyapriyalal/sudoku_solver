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

def find_zeros(boxes):
    for i in range(len(boxes)):
        for j in range(3):
            for k in range(3):
                if boxes[i].box[j][k] == 0:
                    return(i+1,j+1,k+1)
    return None

def is_safe(boxes,box_num,row,col,ele):
    return boxes[box_num-1].is_safe(ele) and check_row(boxes,box_num,row,ele) and check_col(boxes,box_num,col,ele)
        
def solve(boxes):
    zero_pos = find_zeros(boxes)
    if zero_pos == None:
        return True
    box_num, row, col = zero_pos

    for num in range(1,10):
        if is_safe(boxes, box_num, row, col, num):
            boxes[box_num-1].box[row-1][col-1] = num
            if solve(boxes):
                return True
            boxes[box_num-1].box[row-1][col-1] = 0


def print_soln(boxes):
    for box in boxes:
        print(box.box)

box1 = Box([[0,7,0],[0,5,9],[3,4,0]],1)
box2 = Box([[5,8,3],[2,0,0],[0,0,6]],2)
box3 = Box([[0,2,0],[3,0,0],[5,0,7]],3)
box4 = Box([[7,9,5],[0,0,3],[6,8,0]],4)
box5 = Box([[0,0,0],[6,9,7],[0,0,2]],5)
box6 = Box([[6,3,2],[1,0,0],[7,0,0]],6)
box7 = Box([[9,1,4],[0,3,0],[5,6,7]],7)
box8 = Box([[8,3,5],[7,0,1],[4,2,9]],8)
box9 = Box([[0,7,6],[4,9,5],[0,1,3]],9)

boxes = [box1,box2,box3,box4,box5,box6,box7,box8,box9]

# print(box1.is_safe(1))
# print(check_row(boxes,2,2,2))
# print(check_col(boxes,2,2,3))
# print(box1.empty)
if solve(boxes):
    print_soln(boxes)
