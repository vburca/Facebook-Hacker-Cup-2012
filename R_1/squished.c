#include <stdio.h>

int main() {
	
	FILE *f, *g;
	f = fopen("squished.in", "r");
	

	int n, m, encoded;
	fscanf(f, "%d", &n);
	printf(" n = %d\n", n);

	while (n) {
		fscanf(f, "%d", &m);
		fscanf(f, "%d", &encoded);
		printf("\t m = %d\n", m);
		printf("\t encoded = %d\n", encoded);
		n--;
	}

	return 0;
}
