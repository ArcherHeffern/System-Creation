#define _GNU_SOURCE
#include <limits.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/times.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <signal.h>
#include <string.h>
#include <sched.h>
#include <unistd.h>



#define ARR_SIZE 10 // To show slowdown
#define ARR_SIZE 10000000 // To show speedup
#define TASKS 2
#define ELEMENTS_PER_TASK ARR_SIZE / TASKS

int arr[ARR_SIZE];
int mins[TASKS];
int single_theaded_min = INT_MAX;
int multi_threaded_min = INT_MAX;

// Program to split up finding the min value by delegating half of the array to parent, and other half to the thread

static int child_func(int *arg);
int min(int *arr, int start, int stop);
int get_us(struct timeval *start, struct timeval *stop);

int main(int argc, char** argv) {
    // Allocate stack for child task.
    const int STACK_SIZE = 65536;
    char* stack = malloc(STACK_SIZE);
    if (!stack) {
        perror("malloc");
        exit(1);
    }

    // Initialize array with random data
    for (int i = 0; i < ARR_SIZE; i++) {
        arr[i] = rand() % 10;
    }

    // Single threaded solution
    struct timeval stop, start;
    int time_elapsed;
    gettimeofday(&start, NULL);

    single_theaded_min = min(arr, 0, ARR_SIZE);

    gettimeofday(&stop, NULL);
    time_elapsed = get_us(&start, &stop);
    printf("Min value with a single task was calcuated in %d seconds and was %d\n", time_elapsed, single_theaded_min);


    // Multithreaded solution 
    gettimeofday(&start, NULL);

    int i = 0;
    for (; i < TASKS - 1; i++) {
        int args[3] = {i, i * ELEMENTS_PER_TASK, (i+ELEMENTS_PER_TASK)};
        if (clone(child_func, stack + STACK_SIZE, CLONE_VM | SIGCHLD, args) == -1) {
            perror("clone");
            exit(1);
        }
    }
    mins[TASKS - 1] = min(arr, i * ELEMENTS_PER_TASK, (i+1) * ELEMENTS_PER_TASK);
    int status;
    if (wait(&status) == -1) {
        perror("wait");
        exit(1);
    }
    multi_threaded_min = min(mins, 0, TASKS);

    gettimeofday(&stop, NULL);
    time_elapsed = get_us(&start, &stop);
    printf("Min value with %d tasks was calcuated in %d seconds and was %d\n", TASKS, time_elapsed, multi_threaded_min);
    return 0;
}

int min(int *arr, int start, int stop) {
    int min = INT_MAX;
    for (int i = start; i < stop; i++) {
        min = arr[i] < min ? arr[i] : min;
    }
    return min;
}

static int child_func(int *arg) {
    mins[arg[0]] = min(arr, arg[1], arg[2]);
    return 0;
}

int get_us(struct timeval *start, struct timeval *stop) {
    return (stop->tv_sec - start->tv_sec) * 1000000 + stop->tv_usec - start->tv_usec;
}