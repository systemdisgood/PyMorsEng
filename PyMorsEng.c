#include <stdio.h>

typedef unsigned phase_t;
phase_t  max_phase_t = -1;

phase_t beep_phase = 0;
unsigned beep_frequency = 641;
unsigned sampling_frequency = 44100;

void phase_step(phase_t* phase, phase_t step)
{
	*phase += step;
}

unsigned infile_name_len = 0;

int main(int argc, char* argv[])
{
	if(argc != 3)
	{
		printf("Must be 2 arguments\n");
		return 0;
	}

	infile_name_len = strlen(argv[1]);

	return 0;
}
