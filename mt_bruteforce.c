#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>
#include <openssl/md5.h>

typedef struct _thread_data_t {
    pthread_t tid;
    char *alphablock;
} thread_data_t;

int load_file_to_memory(const char *filename, char **result) {
    int size = 0;
    FILE *f = fopen(filename, "rb");
    if (f == NULL) { 
        *result = NULL;
        return -1; // -1 means file opening fail 
    } 
    fseek(f, 0, SEEK_END);
    size = ftell(f);
    fseek(f, 0, SEEK_SET);
    *result = (char *)malloc(size+1);
    if (size != fread(*result, sizeof(char), size, f)) { 
        free(*result);
        return -2; // -2 means file reading fail 
    } 
    fclose(f);
    (*result)[size] = 0;
    return size;
}

void *find_hashes(thread_data_t *thr_data) {
    char *alph = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@";
    int len1 = strlen(alph);
    int len2 = strlen(thr_data->alphablock);
    int a, b, c, d, e;
    char plaintext[6];
    char *filecontent;
    int size;
    unsigned char myhash[MD5_DIGEST_LENGTH];

    size = load_file_to_memory("CRY_Lab_02_B_hashes.txt", &filecontent);
    if (size < 0) {
        puts("Error loading file.\n");
        exit(1);
    }

    for (a = 0; a < len1; a++) {
        for (b = 0; b < len1; b++) {
            for (c = 0; c < len1; c++) {
                for (d = 0; d < len1; d++) {
                    for (e = 0; e < len2; e++) {
                        plaintext[0] = alph[a];
                        plaintext[1] = alph[b];
                        plaintext[2] = alph[c];
                        plaintext[3] = alph[d];
                        plaintext[4] = thr_data->alphablock[e];
                        plaintext[5] = '\0';
                        MD5(plaintext, 6, myhash);
                        if (strstr(filecontent, myhash) != NULL) {
                            printf("thread %ld found hash for %s\n", thr_data->tid, plaintext);
                        }
                    }
                }
            }
        }
    }
    pthread_exit(NULL);
}

int main(int argc, char **argv) {
    thread_data_t thr_data[4];
    thr_data[0].tid = 0;
    thr_data[0].alphablock = "0123456789abcdefghijkl";
    thr_data[1].tid = 1;
    thr_data[1].alphablock = "mnopqrstuvwxyzABCDEFGH";
    thr_data[2].tid = 2;
    thr_data[2].alphablock = "JKLMNOPQRSTUVWXYZ!\"#$";
    thr_data[3].tid = 3;
    thr_data[3].alphablock = "%&\'()*+,-./:;<=>?@";
    int i;
    pthread_t tid[4] = {0, 1, 2, 3};

    for (i = 0; i < 4; i++) {
       //pthread_create(thr_data[i].tid, NULL, find_hashes, &thr_data[i]);
       pthread_create(&(thr_data[i].tid), NULL, (void*)&find_hashes, &thr_data[i]);
    }
    for (i = 0; i < 4; i++) {
       pthread_join(thr_data[i].tid, NULL);
    }
}
