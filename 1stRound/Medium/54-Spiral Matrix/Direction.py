class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # edge case in case it's of length one, otherwise goes out of boundaries
        if (len(matrix) == 1 or len(matrix[0]) == 1):
            vals = []
            for l in matrix:
                vals += l
            return vals

        NUM_CELLS = len(matrix[0])*len(matrix)
        hor, ver = 0, 0
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        vals = []
        direction = 'r'  # 'r', 'd','l','u'

        while (len(vals) < NUM_CELLS):
            vals.append(matrix[ver][hor])

            if (direction == 'r'):
                hor += 1
                if (hor == right):
                    top += 1
                    direction = 'd'
            elif (direction == 'l'):
                hor -= 1
                if (hor == left):
                    bottom -= 1
                    direction = 'u'
            elif (direction == 'u'):
                ver -= 1
                if (ver == top):
                    left += 1
                    direction = 'r'
            elif (direction == 'd'):
                ver += 1
                if (ver == bottom):
                    right -= 1
                    direction = 'l'

        return vals
