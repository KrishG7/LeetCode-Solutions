int largestRectangleArea(int* heights, int heightsSize) {

    int* stack = (int*)malloc((heightsSize + 1) * sizeof(int));
    int top = -1;
    int max_area = 0;

    for (int i = 0; i <= heightsSize; i++) {
        int current_height = (i == heightsSize) ? 0 : heights[i];

        while (top != -1 && heights[stack[top]] > current_height) {
            int h = heights[stack[top--]];
            int w = (top == -1) ? i : (i - stack[top] - 1);
            int area = h * w;
            if (area > max_area)
                max_area = area;
        }
        stack[++top] = i;
    }
    free(stack);
    return max_area;
}
