// N-Queens II
// Difficulty: Hard
// Runtime: 0 ms
// Memory: 40.5 MB
// https://leetcode.com/problems/n-queens-ii/

class Solution {
    private int count = 0;

    public int totalNQueens(int n) {
        boolean[] cols = new boolean[n];         // Columns
        boolean[] d1 = new boolean[2 * n - 1];    // Main diagonals
        boolean[] d2 = new boolean[2 * n - 1];    // Anti-diagonals

        backtrack(0, n, cols, d1, d2);
        return count;
    }

    private void backtrack(int row, int n, boolean[] cols, boolean[] d1, boolean[] d2) {
        if (row == n) {
            count++;
            return;
        }

        for (int col = 0; col < n; col++) {
            int id1 = col - row + n - 1;
            int id2 = col + row;
            if (cols[col] || d1[id1] || d2[id2]) continue;

            cols[col] = d1[id1] = d2[id2] = true;
            backtrack(row + 1, n, cols, d1, d2);
            cols[col] = d1[id1] = d2[id2] = false;
        }
    }
}
