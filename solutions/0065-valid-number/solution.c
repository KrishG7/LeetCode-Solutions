bool isNumber(char* s) {
    bool seen_digit = false, seen_exp = false, seen_dot = false;
    int n = strlen(s);

    for(int i=0;i<n;i++){
        if(s[i]>='0' && s[i]<='9'){
            seen_digit=true;
        }
        else if(s[i]=='+' || s[i]=='-'){
            if (i>0 && s[i-1]!='e' && s[i-1]!='E') return false;
        }
        else if(s[i]=='e' || s[i]=='E'){
            if(seen_exp || !seen_digit) return false;
            seen_exp=true;
            seen_digit=false;
        }
        else if (s[i]=='.'){
            if(seen_dot || seen_exp) return false;
            seen_dot=true;
        }
        else{
            return false;
        }
    }
    return seen_digit;
}
