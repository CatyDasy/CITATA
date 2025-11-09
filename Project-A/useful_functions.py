from email import message
# import tkinter as tk
import random as r
import  time  as t
import re
import pandas as p
import string
import os
import sys
import matplotlib.pyplot as mplb
import numpy as n 
import numpy.random as nr
import time
import colorama as c
from email.mime.text import MIMEText
import json
import smtplib
from plyer import notification
# import mysql.connector as mysql
from colorama import init, Fore, Style
#from blank import Shows_a_line_table
import matplotlib.font_manager as fm
import clipboard

def copy(txt):
    clipboard.copy(txt)
def paste():
    return clipboard.paste()
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def print_hex_color(text, hex_color):
    r, g, b = hex_to_rgb(hex_color)
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m")


def create_table(data,line_names,collumns_names):
    n.array(data)
    return p.DataFrame(data,index=line_names,columns=collumns_names)

def shuffle(iterable):
    iter(iterable)
    returnerList = []
    for o in range((len(iterable) - 1)):
        for i in iterable:
            rchoice = r.choice(iterable)
            returnerList.append(rchoice)
            iterable.pop(iterable.index(rchoice))


    return returnerList
def delete_table_data(table,index):
    try:
        return table.drop(index,axis=0)
    except:
        return table.drop(index,axis=1)
def list_fonts():
    fonts = [f.name for f in fm.fontManager.ttflist]
    return fonts

def show_bar_chart(xval:list,yval:list,xlabel,ylabel,title,length_width:tuple,chartcolor="blue"):
    mplb.figure(figsize=length_width)
    mplb.bar(xval,yval,color=chartcolor)

    mplb.xlabel(xlabel)
    mplb.ylabel(ylabel)
    mplb.title(title)

    mplb.show()
def indent4(data):
    # json.dumps in Python 3 does not accept 'encoding' — return a unicode string;
    # if bytes are required, call .encode('utf-8') on the result where needed.
    return json.dumps(data, indent=4, ensure_ascii=False)
def roll_dice():
    return r.randint(1,6)
def abool(on='on'):
    if on == "on":
        ha = r.randint(1,2)
        if ha == 1:
            return True
        elif ha == 2:
            return False
        else:
            print("USEFUL_FUNCTiON_ERROR")
    else:
        return False
def create_data(status : list = [True,True,True,True,True]):

    if not clear_type(status) == "'list'":
        raise TypeError(f"`status` must be a list of bools, got {clear_type(status)}")

    if len(status) == 5:
        for i in status:
            if not i in [True, False]:
                raise TypeError(f"Only BOOLs in `status`, got {clear_type(i)}")
    else:
        raise IndexError(f"`status` must be have 5 bool items, got {len(status)} length.")

def print_line(text=None,linelong:int = 50, char = '-',color=None):
    if color == None:
        ll = linelong - len(text)
        l = ll // 2
        try:
            line = char*l
        except Exception as exe:
            print(f"Mubarmaj {exe}")
            raise ValueError("PLEASE DO NOT ENTER AN ODD NUMBER TO `LINELONG`")
        print(f"{line}{text}{line}")
    else:
        ll = linelong - len(text)
        l = ll // 2
        try:
            line = char*l
        except Exception as exe:
            print(f"Mubarmaj {exe}")
            raise ValueError("PLEASE DO NOT ENTER AN ODD NUMBER TO `LINELONG`")
        print_color(f"{line}{text}{line}",color=color)

def show_line_chart(
        x_values:list,
        y_values:list,
        title:str,
        chart_color:str = "blue",
        Title_Font_Size:int = 25,
        Font:str="Calibri",
        Title_Color:str="black",
        font_style:str="normal",
        font_weight:str="normal",
        ): 
    """
    Plots a line chart using the given x and y values.
    Displays the chart with the specified color.
    """

    mplb.plot(x_values,y_values,chart_color)
    mplb.title(
        title,
        fontsize=Title_Font_Size,
        color = Title_Color,
        fontstyle = font_style,
        fontweight = font_weight,
        fontname = Font
        )
    mplb.show()
def create_name(length=4,Nametype="vowel"):
    """
    Creates a random name; Nano, Takezo, Mu, etc.
    
    You can use these for Namtype:

    • vowel  
    • consonant  
    • random  
    • pass / both

    """
    seslis = ["a","i","u","e","o"]
    letters = [j for j in list(string.ascii_lowercase) if not j in seslis]

    name = ""

    if Nametype == "vowel":
        for i in range(length):
            if not i%2 == 0:
                name += r.choice(letters)
            else:
                name += r.choice(seslis)
    elif Nametype == "consonant":
        for i in range(length):
            if not i%2 == 0:
                name += r.choice(seslis)
            else:
                name += r.choice(letters)
    elif Nametype == "random":
        for i in range(length):
            name += r.choice(list(string.ascii_lowercase))
    elif Nametype == "pass" or Nametype == "both":
        Nametype = r.choice(["vowel","consonant"])
        if Nametype == "vowel":
            for i in range(length):
                if not i%2 == 0:
                    name += r.choice(letters)
                else:
                    name += r.choice(seslis)
        elif Nametype == "consonant":
            for i in range(length):
                if not i%2 == 0:
                    name += r.choice(seslis)
                else:
                    name += r.choice(letters)
    else:
        raise NameError("PLEASE ENTER A VALID NAMETYPE. ( vowel, consonant, random, pass / both)")

    return name.capitalize()


def underscore(val=50):
    print("_"*val)
def clear(val=1000):
    try:
        os.system("cls")
    except:
        os.system("clear")
def clear_type(
        obj:str
        ):
    """
    This function will find the type of 'obj' and return it with clear ; 
    'str' but NOT "<class 'str'>"
    """
    return (str(type(obj)).replace("<class",""))[:-1]
    
# def sql_join_table(
#         host_type,
#         username,
#         user_password,
#         database_name,
#         tablename,
#         tablename2,
#         token,
#         token2,
#         ):
#     db = mysql.connect(
#         host=host_type,
#         user=username,
#         password=user_password,
#         database=database_name
#     )
#     cursor = db.cursor()
#     if filter == None:
#         # sql = "SELECT * FROM"
#         # cursor = db.cursor()
#         sql = f"UPDATE {tablename}.{token},{tablename2}.{token2} FROM {tablename} inner join {tablename2} on {tablename}.{token}={tablename2}.{token2}"
#         cursor.execute(sql)
#         result = cursor.fetchall()
    
    

#         db.commit()
#         cursor.close()
#         db.close()
#         # return result
#         return cursor.rowcount , result
# def sql_connect_by_join(
#         host_type,
#         username,
#         user_password,
#         database_name,
#         tablename,
#         tablename2,
#         token,
#         token2,
#         filter = None
#         ):
#     db = mysql.connect(
#         host=host_type,
#         user=username,
#         password=user_password,
#         database=database_name
#     )
#     cursor = db.cursor()
#     if filter == None:
#         # sql = "SELECT * FROM"
#         # cursor = db.cursor()
#         sql = f"SELECT {tablename}.{token},{tablename2}.{token2} FROM {tablename} inner join {tablename2} on {tablename}.{token}={tablename2}.{token2}"
#         cursor.execute(sql)
#         result = cursor.fetchall()

#         db.commit()
#         # cursor.close()
#         # db.close()
#         # return result
#         return cursor.rowcount , result
#     else:
#         # sql = "SELECT * FROM"
#         # cursor = db.cursor()
#         sql = f"SELECT {tablename}.{token},{tablename2}.{token2} FROM {tablename} inner join {tablename2} on {tablename}.{token}={tablename2}.{token2} WHERE {filter}"
#         cursor.execute(sql)
#         result = cursor.fetchall()

def create_or_check(path):
    with open(path,"a"):
        pass
def print_success(msg: str):
    print(Fore.GREEN + msg + Style.RESET_ALL)

def print_alert(msg: str):
    print(Fore.YELLOW + msg + Style.RESET_ALL)

def spinner(seconds: float):
    chars = ['|','/','-','\\']
    for i in range(int(seconds * 10)):
        sys.stdout.write(chars[i % 4])
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def print_banner(text: str, color: str = "green"):
    """
    Prints a banner around the given text.
    - text: the message to display
    - color: one of colorama.Fore attributes (e.g., 'red', 'blue', 'green')
    """
    init(autoreset=True)
    # Map user string to a Fore attribute, default to GREEN if invalid
    fore = getattr(Fore, color.upper(), Fore.GREEN)

    # Build the banner frame
    padding = 4
    width = len(text) + padding
    border = fore + "=" * width

    # Print top border, message line, bottom border
    print(border)
    print(fore + f"= {text.center(width - 4)} =")
    print(border)
    print(Style.RESET_ALL)
def stop():
    sys.exit()
def print_mix_color(text: str):
    """
    Scan the input for COLOR(text) patterns and print each 'text' 
    in the corresponding COLOR. Any other parts of the string 
    remain uncoloured.
    """
    init(autoreset=True)

    # Map of supported colours
    colour_map = {
        'BLACK':   Fore.BLACK,
        'RED':     Fore.RED,
        'GREEN':   Fore.GREEN,
        'YELLOW':  Fore.YELLOW,
        'BLUE':    Fore.BLUE,
        'MAGENTA': Fore.MAGENTA,
        'CYAN':    Fore.CYAN,
        'WHITE':   Fore.WHITE,
    }

    # Regex to match tokens like RED(hello world)
    pattern = re.compile(r'([A-Z]+)\((.*?)\)')

    last_end = 0
    for match in pattern.finditer(text):
        # Print any text before this token in default colour
        if match.start() > last_end:
            print(text[last_end:match.start()], end='')

        color_name = match.group(1)
        segment    = match.group(2)
        colour     = colour_map.get(color_name, '')

        # Print the coloured segment
        print(f"{colour}{segment}{Style.RESET_ALL}", end='')

        last_end = match.end()

    # Print any trailing text after the last token
    if last_end < len(text):
        print(text[last_end:], end='')

    # Final newline
    print()



# login = os.getenv("BREVO_API_KEY")
# password = os.getenv("BREVO_API_KEY")  # Brevo pakai key di dua tempat
# def sql_select_by(host_type,username,user_password,database_name,condition,tablename,filter):
#     db = mysql.connect(
#         host=host_type,
#         user=username,
#         password=user_password,
#         database=database_name
#     )
#     cursor = db.cursor()
#     sql = f"SELECT {condition}({filter}) FROM {tablename}"
#     cursor.execute(sql)
#     result = cursor.fetchall()


#     # db.commit()
#     cursor.close()
#     db.close()
#     return result
# def sql_connect_one(host_type, username, user_password, database_name, tablename):
#     db = mysql.connect(
#         host=host_type,
#         user=username,
#         password=user_password,
#         database=database_name
#     )
#     cursor = db.cursor(buffered=True)
#     sql = f"SELECT * FROM {tablename}"
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     cursor.close()
#     db.close()
#     return result  # Just return the row, not rowcount
# def sql_connect_all(host_type,username,user_password,database_name,tablename):
#     db = mysql.connect(
#         host=host_type,
#         user=username,
#         password=user_password,
#         database=database_name
#     ) 

#     cursor = db.cursor()
#     sql = f"SELECT * FROM {tablename}"
#     cursor.execute(sql)
#     result = cursor.fetchall()


#     # db.commit()
#     cursor.close()
#     db.close()
#     # return result
#     return cursor.rowcount , result


# def sql_update(
#     host_type: str,
#     username: str,
#     user_password: str,
#     database_name: str,
#     table_name: str,
#     where_key: str,
#     where_val,
#     update_key: str,
#     update_val
#         ) -> int:
#     """
#     Executes an UPDATE on `table_name`, setting `update_key` = update_val
#     WHERE where_key = where_val. Returns the number of rows updated.
#     """

#     # 1) Connect
#     conn = mysql.connect(
#         host=host_type,
#         user=username,
#         password=user_password,
#         database=database_name
#     )
#     cursor = conn.cursor()

#     # 2) Build SQL with placeholders for values
#     #    Note: table_name and column names are injected directly;
#     #    you must ensure they are valid identifiers.
#     sql = f"UPDATE `{table_name}` SET `{update_key}` = %s WHERE `{where_key}` = %s"

#     # 3) Execute and commit
#     cursor.execute(sql, (update_val, where_val))
#     conn.commit()

#     # 4) Clean up
#     rowcount = cursor.rowcount
#     cursor.close()
#     conn.close()

#     return rowcount

# def sql_append(host_type:str,username:str,user_password:str,database_name:str,indexes:list,index_values:tuple,table_name:str):
#     db = mysql.connect(
#         host=host_type,
#         user=username,
#         password=user_password,
#         database=database_name,
#     )
#     cursor = db.cursor()
#     sql = f"INSERT INTO {table_name} ({','.join(indexes)}) VALUES ({','.join(['%s'] * len(index_values))})"
#     value = index_values
#     cursor.execute(sql, value)


#     db.commit()
#     cursor.close()
#     db.close()
#     return cursor.rowcount
# def sql_select(host_type,username,user_password,database_name,table_name,where):
#     db = mysql.connect(
#         host=host_type,
#         user=username,
#         password=user_password,
#         database=database_name
#     )
#     cursor = db.cursor()
#     sql = f"SELECT * FROM {table_name} WHERE {where}"
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     cursor.close()
#     db.close()
#     return result

# def send_code(to, digit, text ):
#     global vcode
#     digits = ["0" for i in range(digit)]
#     digits[0] = "1"
#     digits = int("".join(digits))
#     vcode = r.randint(digits, 10**digit - 1)

#     port = 587
#     smtp_server = "smtp-relay.brevo.com"
#     login = "93ce87001@smtp-brevo.com"
#     password = "fVUTd9qhRxL5DZ3y"

#     sender_email = "mubarmajm@gmail.com"

#     reciever_email = to

#     text = text.replace("[VCODE]", str(vcode))


#     message = MIMEText(text, "plain")
#     message["Subject"] = "Verification Code"
#     message["From"] = sender_email
#     message["To"] = reciever_email

#     with smtplib.SMTP(smtp_server, port) as server:
#         server.starttls()
#         server.login(login, password)
#         server.sendmail(sender_email, reciever_email, message.as_string())
# # send_code("mubarmajm@gmail.com",7,"Assalamu Alaikum, this is your verification code: [VCODE]")
def send_mail(to, text ):
    port = 587
    smtp_server = "smtp-relay.brevo.com"
    login = "93ce87001@smtp-brevo.com"
    password = "fVUTd9qhRxL5DZ3y"

    sender_email = "mubarmajm@gmail.com"

    reciever_email = to

    # text = f"""
    # Merhaba, Bu Eposta uygulamamdam gonderildi 
    # ALHAMDULILLAH
    # verification code : {vcode}


    massage = MIMEText(text, "plain")
    massage["Subject"] = "Verification Code"
    massage["From"] = sender_email
    massage["To"] = reciever_email

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, massage.as_string())

def send_notification(header,body,time):
    notification.notify(
    title = header,
    message = body,
    timeout = time
                        )

def print_rainbow(text):
    c.init()
    colors = [c.Fore.RED, c.Fore.GREEN, c.Fore.BLUE, c.Fore.YELLOW, c.Fore.CYAN, c.Fore.MAGENTA]
    colored_text = ''.join(f"{colors[i % len(colors)]}{char}" for i, char in enumerate(text))
    print(colored_text + c.Style.RESET_ALL)  # Reset color at the end
def print_mix_colors(text):
    c.init()
    colors = [c.Fore.RED, c.Fore.GREEN, c.Fore.BLUE, c.Fore.YELLOW, c.Fore.CYAN, c.Fore.MAGENTA]
    text = text.split("GREEN.")
        
# send_code("mubarmajm@gmail.com", 6, "Assalamu Alaikum, this is your verification code: [VCODE]")
def bigspace():
    print("\n")
def s():
    print("")
def for_seconds(second,verb):
    second = second + t.time()
    while t.time() < second:
        eval(verb)
        t.sleep(0.00000000001)
        if __name__ == "__main__":
            print("Ended")
def print_red(text):
    c.init()
    print(f"\033[31m{text}\033[0m")
def print_green(text):
    c.init()
    print(f"\033[32m{text}\033[0m")
def print_blue(text):
    c.init()
    print(f"\033[1;34m{text}\033[0m")
def print_yellow(text):
    c.init()
    print(f"\033[1;33m{text}\033[0m")
def print_highlight(text):
    c.init()
    print(f"\033[1;35m{text}\033[0m")
def print_white(text):
    c.init()
    print(f"\033[1;37m{text}\033[0m")
def print_black(text):
    c.init()
    print(f"\033[1;30m{text}\033[0m")
def print_cyan(text):
    c.init()
    print(f"\033[1;36m{text}\033[0m")
def print_pink(text):
    c.init()
    print(f"\033[1;35m{text}\033[0m")
def print_orange(text):
    c.init()
    print(f"\033[38;5;208m{text}\033[0m")  # Orange using ANSI escape code
def print_purple(text):
    c.init()
    print(f"\033[38;5;129m{text}\033[0m")  # Purple using ANSI escape code
def print_gray(text):
    c.init()
    print(f"\033[38;5;245m{text}\033[0m")  # Gray using ANSI escape code
def print_light_blue(text):
    c.init()
    print(f"\033[38;5;153m{text}\033[0m")  # Light Blue using ANSI escape code
def print_highlight_blue(text):
    c.init()
    print(c.Back.BLUE  + c.Fore.BLACK + text + c.Style.RESET_ALL)  # Highlight Blue using ANSI escape code
def print_highlight_red(text):
    c.init()
    print(c.Back.RED  + c.Fore.BLACK + text + c.Style.RESET_ALL)  # Highlight Red using ANSI escape code
def print_highlight_green(text):
    c.init()
    print(c.Back.GREEN  + c.Fore.BLACK + text + c.Style.RESET_ALL)  # Highlight Green using ANSI escape code
def print_highlight_yellow(text):
    c.init()
    print(c.Back.YELLOW  + c.Fore.BLACK + text + c.Style.RESET_ALL)  # Highlight Yellow using ANSI escape code
def print_highlight_purple(text):
    c.init()
    print(c.Back.MAGENTA  + c.Fore.BLACK + text + c.Style.RESET_ALL)  # Highlight Purple using ANSI escape code
def print_highlight_orange(text):
    c.init()
    print(c.Back.YELLOW  + c.Fore.BLACK + text + c.Style.RESET_ALL)  # Highlight Orange using ANSI escape code
def print_highlight_gray(text):
    c.init()
    print(c.Back.WHITE  + c.Fore.BLACK + text + c.Style.RESET_ALL)  # Highlight Gray using ANSI escape code
def print_highlight_pink(text):
    c.init()
    print(c.Back.MAGENTA  + c.Fore.BLACK + text + c.Style.RESET_ALL)  # Highlight Pink using ANSI escape code
def print_highlight_red_white(text):
    c.init()
    print(c.Back.RED  + c.Fore.WHITE + text + c.Style.RESET_ALL)  # Highlight Red with White text using ANSI escape code
def print_highlight_green_white(text):
    c.init()
    print(c.Back.GREEN  + c.Fore.WHITE + text + c.Style.RESET_ALL)  # Highlight Green with White text using ANSI escape code
def print_highlight_blue_white(text):
    c.init()
    print(c.Back.BLUE  + c.Fore.WHITE + text + c.Style.RESET_ALL)  # Highlight Blue with White text using ANSI escape code
def print_highlight_yellow_white(text):
    c.init()
    print(c.Back.YELLOW  + c.Fore.WHITE + text + c.Style.RESET_ALL)  # Highlight Yellow with White text using ANSI escape code
def print_highlight_purple_white(text):
    c.init()
    print(c.Back.MAGENTA  + c.Fore.WHITE + text + c.Style.RESET_ALL)  # Highlight Purple with White text using ANSI escape code
def print_highlight_orange_white(text):
    c.init()
    print(c.Back.YELLOW  + c.Fore.WHITE + text + c.Style.RESET_ALL)  # Highlight Orange with White text using ANSI escape code
def print_highlight_gray_white(text):
    c.init()
    print(c.Back.WHITE  + c.Fore.BLACK + text + c.Style.RESET_ALL)  # Highlight Gray with Black text using ANSI escape code
def print_highlight_pink_white(text):
    c.init()
    print(c.Back.MAGENTA  + c.Fore.WHITE + text + c.Style.RESET_ALL)  # Highlight Pink with White text using ANSI escape code
def print_bold(text):
    c.init()
    print(f"\033[1m{text}\033[0m")  # Bold text using ANSI escape code
def print_italic(text):
    c.init()
    print(f"\033[3m{text}\033[0m")  # Italic text using ANSI escape code
def LoadingEffects(Text,final):
    # print(".") 
    for nonetype in range(0,1):
                for i in range(3):
                    for j in range(0,4):
                        print(f"\r{Text}",j*".","                   .", end="")
                        t.sleep(0.5)
                print(f"\r{final}                                                                                                                       ")     

def print_color(text, color):
    c.init()
    if color == "red":
        print_red(text)
    elif color == "green":
        print_green(text)
    elif color == "blue":
        print_blue(text)    
    elif color == "yellow":
        print_yellow(text)
    elif color == "purple":
        print_purple(text)
    elif color == "orange":
        print_orange(text)
    elif color == "gray":
        print_gray(text)
    elif color == "pink":
        print_pink(text)
    elif color == "cyan":
        print_cyan(text)
    else:
        print_hex_color(text, color)
        # raise ValueError("ENTER A VALID COLOR.")
def make_password(level=1):
    if level == 1:
        return r.randint(1000,9999)
    elif level == 2:
        return r.randint(100000,999999)
    elif level == 3:
        # Define character pools
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        digits = string.digits
        symbols = "!@#$%&*"

        # Ensure at least one of each type
        mandatory = [
            r.choice(upper),
            r.choice(lower),
            r.choice(digits),
            r.choice(symbols)
        ]

        # Fill the rest randomly
        all_chars = upper + lower + digits + symbols
        remaining = [r.choice(all_chars) for _ in range(8)]

        # Combine and shuffle
        password_list = mandatory + remaining
        r.shuffle(password_list)

        return ''.join(password_list)

    





def print_highlight_color(text, color, highlight_color):
    c.init()
    if highlight_color == "red":
        print(c.Back.RED + getattr(c.Fore, color.upper(), c.Fore.BLACK) + text + c.Style.RESET_ALL)
    elif highlight_color == "green":
        print(c.Back.GREEN + getattr(c.Fore, color.upper(), c.Fore.BLACK) + text + c.Style.RESET_ALL)
    elif highlight_color == "blue":
        print(c.Back.BLUE + getattr(c.Fore, color.upper(), c.Fore.BLACK) + text + c.Style.RESET_ALL)
    elif highlight_color == "yellow":
        print(c.Back.YELLOW + getattr(c.Fore, color.upper(), c.Fore.BLACK) + text + c.Style.RESET_ALL)
    elif highlight_color == "magenta" or highlight_color == "purple":
        print(c.Back.MAGENTA + getattr(c.Fore, color.upper(), c.Fore.BLACK) + text + c.Style.RESET_ALL)
    elif highlight_color == "cyan":
        print(c.Back.CYAN + getattr(c.Fore, color.upper(), c.Fore.BLACK) + text + c.Style.RESET_ALL)
    elif highlight_color == "white":
        print(c.Back.WHITE + getattr(c.Fore, color.upper(), c.Fore.BLACK) + text + c.Style.RESET_ALL)
    elif highlight_color == "black":
        print(c.Back.BLACK + getattr(c.Fore, color.upper(), c.Fore.WHITE) + text + c.Style.RESET_ALL)
    else:
        raise ValueError("ENTER A VALID highlight COLOR.")
def print_overwrite(text,value):
    c.init()
    print(f"\033[{value}A{text}", end="")
mail = ""
def makeMail(mail_input):
    global mail
    mail = mail_input

def detectMail(mail_input):
    pattern = r"\w+@[a-zA-Z0-9]+\.\b(com|net|org)\b"
    research = re.findall(pattern, mail_input)
    if len(research) > 0:
        return True
    else:
        return False
def search(from_ : str, pattern):
    """
from_ : regular expressions formatted string
pattern : any

o(*￣▽￣*)ブ enjoy this func! 
    """
    research = re.findall(pattern, from_)
    if len(research) > 0:
        return True
    else:
        return False
def testPassword(password):
    pattern = re.compile(r".*\b((?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]))+\b.*")

    sonuc = pattern.fullmatch(password)

    if sonuc == None:
        return False
    else:
        if len(password) >= 8:
            return True
        else:
            return False
def Avarage(
        plist : list
        ):
    """
    Enter a list for find Avarage of it...
    """
    h1 = sum(plist)
    h2 = h1 / len(plist)
    return h2
if __name__ == "__main__" :
    makeMail("Hello@hotmail.com")
    bolean = detectMail(mail)
    print(bolean)
# def tk_txtbox(root: tk.Tk):
    
#     i = tk.StringVar(root)
#     txtbx = tk.Entry(root, textvariable=i)
#     txtbx.pack()


#     root.update()

#     return i.get()

# def tk_root():

#     return tk.Tk()
# def tk_resize(root : tk.Tk, tuple_ = (300, 300)):

#     strT = str(tuple_[0]) + 'x' + str(tuple_[1])

#     root.geometry(strT)
#     return root
# def tk_title(root : tk.Tk, txt):
#     label = tk.Label(root, text = txt)

#     label.pack()

#     root.update()

#     return root

class ufs:
    def __init__(self, text):
        self._text = str(text)  # pastikan input jadi string

    def __str__(self):
        return self._text

    def __repr__(self):
        return f'ufs{self._text}")'

    def __len__(self):
        return len(self._text)

    def __getitem__(self, index):
        return self._text[index]

    def lower(self):
        return self._text.lower()

    def upper(self):
        return self._text.upper()

    def replace(self, old, new, count=-1):
        return self._text.replace(old, new, count)
    def remove(self, target):
        return self.replace(target, "")


    
# for_seconds(0.0000003,"print(1+2+3+4+5+6+7+8)")
# class MathClass:
#     def __init__(self, *args):
#         self.args = list(args)

#     def summer(self):
#         return sum(self.args)

#     def mineser(self):
#         self.args.sort()
#         result = self.args[0]
#         for index in range(1, len(self.args)):
#             result -= self.args[index]
#         return result

#     def multiplyer(self):
#         result = 1
#         for num in self.args:
#             result *= num
#         return result

#     def divider(self):
#         self.args.sort()
#         result = self.args[0]
#         try:
#             for index in range(1, len(self.args)):
#                 result /= self.args[index]
#             return result
#         except ZeroDivisionError:
#             return "⚠️ Error: Pembagian dengan 0 tidak boleh!"

# # Coba uji class-nya
# if __name__ == "__main__":
#     bir = MathClass(10, 2, 5)
#     print("Tambah:", bir.summer())     # 17
#     print("Kurang:", bir.mineser())    # 3
#     print("Kali:", bir.multiplyer())   # 100
#     print("Bagi:", bir.divider())      # 1.0
# else:
#     print(".")
print(1==1)