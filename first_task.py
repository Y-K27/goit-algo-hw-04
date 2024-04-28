from pathlib import Path

def total_salary(path) -> int:
    own_way = Path(path)
    with open(own_way, 'r') as salary_list:
        lines = [el.split(',') for el in salary_list.readlines()]
        i=0
        total = 0
        #print(lines)
        for i in range(0, len(lines)):
            lines[i][1]=lines[i][1].strip()
            total +=int(lines[i][1])
        average = int(total/len(lines))
    return total, average

def get_cats_info(path) -> int:
    own_way = Path(path)
    with open(own_way, 'r') as salary_list:
        lines = [el.split(',') for el in salary_list.readlines()]
        i=0
        cats_info = []       
        for i in range(0, len(lines)):
            lines[i][2]=lines[i][2].strip()
            cats_info.append({
                "id": lines[i][0],
                "name": lines[i][1],
                "age": lines[i][2]})
    return cats_info
