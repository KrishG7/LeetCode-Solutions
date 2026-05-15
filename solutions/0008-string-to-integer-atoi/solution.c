int myAtoi(char* s) {
    int i=0;
    int sign=1;
    int res=0;
    while(s[i]==' ') i++;
    if (s[i]=='-' || s[i]=='+'){
        if(s[i]=='-') sign=-1;
        i++;
    }
    while(s[i]!='\0' && isdigit(s[i])){
        int digit=s[i]-'0';
        if (res > INT_MAX / 10 || (res == INT_MAX / 10 && digit > 7)) {
            return (sign == 1) ? INT_MAX : INT_MIN;
        }

        res = res * 10 + digit;
        i++;
    }

    return res * sign;
}
