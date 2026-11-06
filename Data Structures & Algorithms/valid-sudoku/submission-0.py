class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # tao set chua
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]

        # duyet qua matrix
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                # tinh thu tu box
                box_idx = (r//3) * 3 + (c//3)

                # kiem tra xem co trong set moi tao chua
                if val in row[r] or val in col[c] or val in box[box_idx]:
                    return False

                # neu chua xuat hien thi them vao
                row[r].add(val)
                col[c].add(val)
                box[box_idx].add(val)
        return True
