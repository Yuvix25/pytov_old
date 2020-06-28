if (1 && 1){
                   print("i dont care about indetation");
   if(1==1){
print("except");
}
       }
if (1!=2){
    print("ihihih");
    print({"hi":1}["hi"]);
}

def hi(){
    print("hi");
}

def hello(){
    print("hello");
}


dict = {"hello":1};

/*
this will not be an error
multi line
*/

//this one too



switch("hii", {
    "hello":
        lambda{ print("hello"); },
    "hi":
        lambda{ print("hi"); },
    },
        lambda{ print("default case"); },
);