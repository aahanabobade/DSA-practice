# Zigzag Conversion
# Difficulty: Medium
# Runtime: 3 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/zigzag-conversion/

        current_row =0
        going_down = False

        for i in s:
        rows= ['']*numRows
        
            return s
            rows[current_row]+=i

            if current_row == 0 or current_row ==numRows-1:
                going_down = not going_down
            
            current_row += 1 if going_down else -1
        
        return ''. join(rows)
                
