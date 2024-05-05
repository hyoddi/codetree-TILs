#include <stdio.h>

int main() {
    int a, b, ans;

    scanf("%d %d", &a, &b);

    if (a > b){
        ans = a - b;
    }
    else{
        ans = b - a;
    }

    printf("%d", ans);
    return 0;
}