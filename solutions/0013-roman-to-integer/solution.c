int getVal(char c) {
    switch (c) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
    }
}

int romanToInt(char* s) {
    int res=0;
    int n=strlen(s);

    for(int i=0;i<n;i++){
        int v1=getVal(s[i]);

        if(i+1<n){
            int v2=getVal(s[i+1]);
            if(v1<v2){
                res-=v1;
            }else{
                res+=v1;
            }
        }else{
            res+=v1;
        }
    }
    return res;
}

