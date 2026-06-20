char* multiply(char* num1, char* num2) {
    if (strcmp(num1, "0") == 0 || strcmp(num2, "0") == 0)
        return "0";

    int len1 = strlen(num1);
    int len2 = strlen(num2);

    int* res = (int*)calloc(len1 + len2 + 1, sizeof(int));

    for (int i = len1 - 1; i >= 0; i--) {
        for (int j = len2 - 1; j >= 0; j--) {
            int mul = (num1[i] - '0') * (num2[j] - '0');
            int p1 = i + j;
            int p2 = i + j + 1;

            int sum = mul + res[p2];

            res[p2] = sum % 10;
            res[p1] += sum / 10;
        }
    }

    char* result = (char*)malloc((len1 + len2 + 1)* sizeof(char));
    int start = 0;
    while (start < len1 + len2 && res[start] == 0) {
        start++;
    }

    int k = 0;
    for (int i = start; i < len1 + len2; i++) {
        result[k++] = res[i] + '0';
    }

    result[k] = '\0';

    free(res);
    return result;
}
