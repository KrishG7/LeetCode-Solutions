/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 
char** letterCombinations(char* digits, int* returnSize) {
    *returnSize = 0;
    int len = strlen(digits);
    if (len == 0) return NULL;

    char* phoneMap[]={"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};

    int total = 1;
    for (int i = 0; i < len; i++) {
        total *= (digits[i] == '7' || digits[i] == '9') ? 4 : 3;
    }

    char ** result=(char **)malloc(total * (sizeof(char*)));
    for(int i=0;i<total;i++){
        result[i] = (char*)malloc((len + 1) * sizeof(char));
        result[i][len] = '\0';
    }

    int groups = total;
    for (int i = 0; i < len; i++) {
        char* letters = phoneMap[digits[i] - '2'];
        int letterCount = strlen(letters);

        groups /= letterCount;
        for (int j = 0; j < total; j++) {
            result[j][i] = letters[(j / groups) % letterCount];
        }
    }

    *returnSize = total;
    return result;

}

