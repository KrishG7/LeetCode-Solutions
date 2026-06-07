/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void backtrack(char* current, int open, int close, int n, char ** result, int * returnSize, int len){
    if (len==2 * n){
        current[len] = '\0';
        result[*returnSize]= strdup(current);
        (*returnSize)++;
        return;
    }

    if (open < n) {
        current[len] = '(';
        backtrack(current, open + 1, close, n, result, returnSize, len + 1);
    }
    
    if (close < open) {
        current[len] = ')';
        backtrack(current, open, close + 1, n, result, returnSize, len + 1);
    }
}


char** generateParenthesis(int n, int* returnSize) {
    char** result = (char**)malloc(5000 * sizeof(char*));
    char* current = (char*)malloc((2 * n + 1) * sizeof(char));
    *returnSize = 0;

    backtrack(current, 0, 0, n, result, returnSize, 0);
    
    free(current);
    return result;
}
