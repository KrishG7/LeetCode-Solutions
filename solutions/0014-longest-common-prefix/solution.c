char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize==0) return "";
    char* first=strs[0];
    int len=strlen(first);
    for(int i=0;i<len;i++){
        char c=first[i];
        for(int j=1;j<strsSize;j++){
            if (strs[j][i]=='\0' || strs[j][i]!=c){
                first[i]='\0';
                return first;
            }
        }
    }
    return first;
}
