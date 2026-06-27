char* simplifyPath(char* path) {
    char** stack = malloc((strlen(path) + 1) * sizeof(char*));
    int top = 0;

    char* token = strtok(path, "/");
    while (token != NULL) {
        if (strcmp(token, ".") == 0 || strlen(token) == 0) {
            // ignore
        } else if (strcmp(token, "..") == 0) {
            if (top > 0)
                top--;
        } else {
            // FIX: strdup the token to save a permanent copy
            stack[top++] = strdup(token);
        }
        token = strtok(NULL, "/");
    }

    char* result = malloc(strlen(path)*3000 + 2); // Standard size is enough
    int pos = 0;

    if (top == 0) {
        result[pos++] = '/';
    } else {
        for (int i = 0; i < top; i++) {
            result[pos++] = '/';
            for (int j = 0; stack[i][j] != '\0'; j++) {
                result[pos++] = stack[i][j];
            }
        }
    }
    result[pos] = '\0';

    free(stack);
    return result;
}
