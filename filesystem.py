import os

class File():
    def __init__(self,path) -> None:
        self.path = path;
        self.file,self.data = None,None;

    def read_file(self):
        try:
            with open(self.path,"r") as file:
                self.data = file.read();
                if self.data == " ":
                    print("Empty text file");
                else: print(self.data);
        except Exception:
            print(f"Eroor during task {Exception}");
        return self.data;
    
    def write_file(self,value):
        with open(self.path,"w") as f:
            f.write(value);

    def append_file(self,value):
        with open(self.path,"a") as f:
            f.write(value);
    def delete_file(self):
        os.remove(self.path);
        print("File deleted")

    def clear_file(self):
        with open(self.path,"w") as file:
            file.write("");
        
        print("File cleared");
        return self.path;
    def copyFile(self,path):
        res = self.read_file();
        if os.path.exists(path):
            print("This file already exist.\n \
                  Do you want to rewrite?");
            return 
        else:
            with open(path,"r") as f:
                f.read(self.read_file());
if __name__ == "__main__":
    file = File("test.txt");
    value = input("Enter your filename or path");
    while True:

        
        choice = int(input("Enter your choice: "));
        if choice == 1:
            file.read_file();
        elif choice == 2:
            value = input("Enter value: ");
            file.write_file(value);
        elif choice == 3:
            value = input("Enter value: ");
            file.append_file(value);
        elif choice == 4:
            file.delete_file();
        elif choice == 5:
            file.clear_file();
        elif choice == 6:
            break;
        elif choice == 7:
            path = input("Enter folder path");
            file.copyFile();
        elif choice == 8:
            value = input("Enter filename");
            file = File(value);
        else:
            print("Invalid choice");
    