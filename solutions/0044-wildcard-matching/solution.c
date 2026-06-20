bool isMatch(char* s, char* p) {
    int s_idx = 0;
    int p_idx = 0;
    int star_idx = -1;
    int match_idx = 0;

    while (s[s_idx] != '\0') {
        if (p[p_idx] == '?' || p[p_idx] == s[s_idx]) {
            p_idx++;
            s_idx++;
        }

        else if (p[p_idx] == '*') {
            star_idx = p_idx;
            match_idx = s_idx;
            p_idx++;
        }

        else if (star_idx != -1) {
            p_idx = star_idx + 1;
            s_idx = ++match_idx;
        } else
            return false;
    }
    while (p[p_idx] == '*')
        p_idx++;

    return p[p_idx] == '\0';
}
