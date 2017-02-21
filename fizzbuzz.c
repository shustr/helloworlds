#include <stdio.h>

int main(int argc, const char * argv[]) {
int num;

for (num = 0; num <= 100; num++)
	if (num % 3 == 0) {
		printf("Fizz %d", num);
	}
	
	else if (num % 5 == 0) {
		printf("Buzz %d", num);
	}

	else if (num % 3 == 0 && num % 5 == 0) {
		printf("FizzBuzz %d", num);
	}

	else {
		printf("%d", num);
	}
return 0;
}
