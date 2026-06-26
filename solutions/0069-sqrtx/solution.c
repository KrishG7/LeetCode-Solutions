int mySqrt(int x) {
    if(x<2){
        return x;
    }
    int ans=0;
    int low=0;
    int high=x/2;
    while(low<=high){
        int mid=(low+high)/2;
        if ((long)mid*mid<=x){
            ans=mid;
            low=mid+1;
        }
        else{
            high=mid-1;
        }
    }
    return ans;
}
