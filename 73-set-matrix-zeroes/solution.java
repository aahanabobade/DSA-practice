// Set Matrix Zeroes
// Difficulty: Medium
// Runtime: 1 ms
// Memory: 45.6 MB
// https://leetcode.com/problems/set-matrix-zeroes/

class Solution {
    public void setZeroes(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return;

        int m = matrix.length;
        int n = matrix[0].length;
        boolean rowZero = false; // Flag for the first row
        boolean colZero = false; // Flag for the first column

        // Check if the first row needs to be zero
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                rowZero = true;
                break;
            }
        }

        // Check if the first column needs to be zero
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                colZero = true;
                break;
            }
        }

        // Use the first row and column to mark zeroes for the rest of the matrix
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0; // Mark the start of the row
                    matrix[0][j] = 0; // Mark the start of the column
                }
            }
        }

        // Set matrix cells to zero based on the markers
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        // Finally, set the first row to zero if needed
        if (rowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }

        // Finally, set the first column to zero if needed
        if (colZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
