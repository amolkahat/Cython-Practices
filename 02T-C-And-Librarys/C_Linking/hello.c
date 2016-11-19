int HELLO_X = 10;

int * arange(int a){
    int i = 0;
    int ar[a];
    for(;i<a;i++){
        ar[i] = i;
    }
    return &ar;
}

void main(){
    int s = arange(19);
    int i;
//    for(i=0;i<19;i++){
        printf("%s", s);
  //  }
}
