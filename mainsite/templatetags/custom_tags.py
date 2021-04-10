from django import template

register = template.Library()

def count(value, arg):
    current_times_str=''
    with open('mainsite/templatetags/times.txt', 'r') as times_txt_file:
            current_times_str = times_txt_file.read() # 讀取檔案內容

    if arg == current_times_str:
        print('first time')
        incremented_times = int(arg) + 1
        with open('mainsite/templatetags/times.txt', 'w') as times_txt_file:
            str_times = str(incremented_times)
            times_txt_file.write(str_times) 
        tmp = str(incremented_times)
        return incremented_times
    else:
        current_times_str = ''
        with open('mainsite/templatetags/times.txt', 'r') as times_txt_file:
            current_times_str = times_txt_file.read() # 讀取檔案內容
        current_times_val = int(current_times_str)
        incremented_times_val = current_times_val + 1
        incremented_times_str = str(incremented_times_val)
        print('current_times_val',incremented_times_val)

        with open('mainsite/templatetags/times.txt', 'w') as times_txt_file:
            times_txt_file.write(incremented_times_str) # 讀取檔案內容

        return incremented_times_val
        
def reset(value, arg):
    with open('mainsite/templatetags/times.txt', 'w') as times_txt_file:
        times_txt_file.write('0') # 讀取檔案內容
    return ''

register.filter('count', count)
register.filter('reset', reset)