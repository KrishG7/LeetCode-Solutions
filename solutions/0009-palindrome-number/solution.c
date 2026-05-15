bool isPalindrome(int x) {
    if (x<0 || x%10==0 && x!=0){
        return false;
    }
    int original=x;
    long reverse=0;
    while(x>0){
        reverse=reverse*10+(x%10);
        x/=10;
    }
    return (original==(int)reverse);
}
