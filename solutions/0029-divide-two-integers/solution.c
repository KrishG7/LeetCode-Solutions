int divide(int dividend, int divisor) {
    if (dividend == -2147483648 && divisor == -1)
        return 2147483647;

    long dvd = labs(dividend);
    long dvs = labs(divisor);
    long quotient = 0;

    int sign = ((dividend < 0) ^ (divisor < 0)) ? -1 : 1;

    while (dvd >= dvs) {
        long temp = dvs, multiple = 1;
        while (dvd >= (temp << 1)) {
            temp <<= 1;
            multiple <<= 1;
        }
        dvd -= temp;
        quotient += multiple;
    }

    return (int)(sign * quotient);
}
