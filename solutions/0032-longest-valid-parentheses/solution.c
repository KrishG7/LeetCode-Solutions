int longestValidParentheses(char* s) {
    int n = strlen(s);
    int max_len=0;

    int stack[n+1];
    int top=-1;

    stack[++top]=-1;

    for(int i=0;i<n;i++){
        if(s[i]=='('){
            stack[++top]=i;
        }
        else{
            top--;
            if (top==-1){
                stack[++top]=i;
            }
            else{
                int current_len=i-stack[top];
                if (current_len>max_len){
                    max_len=current_len;
                }
            }
        }
    }
    return max_len;
}
