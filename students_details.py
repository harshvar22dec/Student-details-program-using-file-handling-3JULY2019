def write_data():
    rno=input('Enter Roll No.\t')
    name=input('Enter Name of the Student\t').upper()
    cno=input('Enter the contact number\t')
    obj=open('data.txt','a')
    obj.write(rno+'%*'+name+'%*'+cno+'%*'+'\n')
    print('Successfully Done!')
    obj.close()
def search_data():
    rno=input('Enter Roll No.\t')
    obj=open('data.txt','r')
    data=obj.readlines();obj.close()
    print('__'*35);found=0
    for i in data:
        if rno in i:
            j=i.split('%*');found+=1
            print(f'[{found}]\n  Roll No.: {j[0]}\nName: {j[1]}\tContact No.: {j[2]}\n')
    print('__'*35)
while True:
    print('Press W to write a data, and R to read the data')
    respon=input().upper()
    if respon=='W':write_data()
    elif respon=='R':search_data()
    else:print('Wrong Key Pressed!',end='\n\n')

    
    
    
