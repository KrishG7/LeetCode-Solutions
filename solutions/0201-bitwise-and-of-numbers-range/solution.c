int rangeBitwiseAnd(int left, int right) {
    int shift = 0;
    while (left < right) {
        //  keep shifting both numbers to the right
        left >>= 1;
        right >>= 1;
        //  keep track of how many bits you shifted
        shift += 1;
    }

    //  Once left and right are equal, you have found the common prefix, shift result by those no of shifts to get number back in place
    return left << shift;
}
