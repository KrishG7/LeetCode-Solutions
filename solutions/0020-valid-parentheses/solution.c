bool isValid(char* s) {
    char stack[10000];
    int top = -1;
    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            top++;
            stack[top] = s[i];
        } else {
            if (top == -1)
                return false;
            char topChar = stack[top];
            if ((s[i] == ')' && topChar == '(') ||
                (s[i] == '}' && topChar == '{') ||
                (s[i] == ']' && topChar == '[')) {
                top--;
            } else {
                return false;
            }
        }
    }
    return top == -1;
}
