#include <stdio.h>

int main() {
    
    int arr[10];
    int sum_val = 0;
    int cnt = 0;

    for (int i = 0; i < 10; i++){
        scanf("%d", &arr[i]);
        if (arr[i] >= 250) break;
        sum_val+=arr[i];
        cnt += 1;
    }

    float avr_val = (float)sum_val / cnt;
    
    printf("%d %.1f",sum_val, avr_val);


    return 0;
}