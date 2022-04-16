import os

def get_file_path(dir_name, file_name):
    return os.path.join(os.getcwd(),dir_name,file_name)

def read_file(dir_name, file_name, coding):
    file_path = get_file_path(dir_name, file_name)
    exit_dict = {}
    with open(file_path,'r',encoding = coding) as file:
        #получаем первую итерацию
        line = file.readline()
        while line:
            if not line.isspace():
                text_itr = line.replace('\n','')
                exit_dict.setdefault(text_itr,[])
                line = file.readline()
                num_itr = int(line.replace('\n',''))
                i = 1
                while i <= num_itr:
                    line = file.readline()
                    ing_str = str(line.strip())
                    list_ing = ing_str.split("|")
                    dict_ing = {'ingredient_name': list_ing[0].strip(), 'quantity':int(list_ing[1]), 'measure':list_ing[2].strip()}
                    exit_dict[text_itr] += [dict_ing]
                    i += 1
                line = file.readline()
            else:
                line = file.readline()
    return exit_dict

def print_menu(menu_dict):
    for name,list_ing in menu_dict.items():
        print(name,":")
        for it in list_ing:
            print(it)

def get_shop_list_by_dishes(cook_book, dishes, person_count: int):
    exit_list = {}

    for cook in dishes:
        cook_menu = cook_book.get(cook)
        if cook_menu != None:
             for ing in cook_menu:
                ingr_name = ing['ingredient_name']
                val = exit_list.get(ingr_name)
                if val == None:
                    exit_list.setdefault(ingr_name,{'measure':ing['measure'],'quantity':ing['quantity']*person_count})
                else:
                    val['quantity'] += ing['quantity']*person_count
        else:
            print(f'Такого блюда: "{cook}" нет в книге')
    return exit_list

def main():
    cook_book = read_file("files","recipes.txt","utf-8")
    print_menu(cook_book)

    list_cook = ['Омлет','Омлет','Утка по-пекински','Жареный картофель','Фахитос']
    count_person = 1

    dict_ing = get_shop_list_by_dishes(cook_book,list_cook,count_person)

    print(dict_ing)
main()