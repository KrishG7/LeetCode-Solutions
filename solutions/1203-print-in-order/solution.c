typedef struct {
    // User defined data may be declared here.
    sem_t sem_second;
    sem_t sem_third;
    
} Foo;

// Function Declaration, do not remove
void printFirst();
void printSecond();
void printThird();

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    
    // Initialize user defined data here.
    sem_init(&obj->sem_second, 0, 0);
    sem_init(&obj->sem_third, 0, 0);
    return obj;
}

void first(Foo* obj) {
    
    // printFirst() outputs "first". Do not change or remove this line.
    printFirst();
    sem_post(&obj->sem_second);
}

void second(Foo* obj) {
    
    // printSecond() outputs "second". Do not change or remove this line.
    sem_wait(&obj->sem_second);
    printSecond();
    sem_post(&obj->sem_third);
}

void third(Foo* obj) {
    
    // printThird() outputs "third". Do not change or remove this line.
    sem_wait(&obj->sem_third);
    printThird();
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.
    sem_destroy(&obj->sem_second);
    sem_destroy(&obj->sem_third);
    free(obj);
}
