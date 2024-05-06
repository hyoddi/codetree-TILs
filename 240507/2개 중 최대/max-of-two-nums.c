#include <stdio.h>

int main() {
    int a, b, ans;
    scanf("%d %d", &a, &b);

    ans = a > b ? a : b;
    printf("%d", ans);
    
    return 0;
}