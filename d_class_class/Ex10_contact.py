
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    # 여기에 코드 작성
    val = Contact(name=input("이름은?"),
                  phone_number=input("전화번호는?"),
                  email=input("이메일은?"),
                  addr=input("주소는?"))
    return val

def print_contact(contact_list):
    # 여기에 코드 작성
    #[ Contact , Contact1]
    li = ["이름:",'전화번호:','이메일:','주소:']
    for i in contact_list:
        for idx,j in enumerate(li):
            if idx==0: print(j,i.name)
            if idx==1: print(j,i.phone_name)
            if idx==2: print(j,i.email)
            if idx==3: print(j,i.addr)


def delete_contact(contact_list, name):
    # 여기에 코드 작성
    for idx,i in enumerate(contact_list):
        if i.name == name:
            del contact_list[idx]
            print(name+"님이 삭제되었습니다.")
        else:
            print('존재하지 않는 이름입니다.')

def run():
    # Contact 인스턴스를 저장할 리스트 자료구조 생성
    contact_list = []
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            contact = set_contact()
            contact_list.append(contact)
        elif menu==2: # 출력을 선택하면
            print_contact(contact_list)
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(contact_list,name)


if __name__ == "__main__":
    run()