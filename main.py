# парсинг diy by
import requests
from lxml import html

def cnnct(url):
    response = requests.get(url = url)
    print(response.status_code)
    tree = html.fromstring(response.text)
    return tree

def get_data(tree):
    xpath = f"//div/div[@class='td_name' and 3]"
    xpath2 = f"//div[@class='td_price']"
    element = tree.xpath(xpath)
    price = tree.xpath(xpath2)
    print(len(element))
    a = []
    for i in range(len(element)):
        text = element[i].text
        text2 = price[i].text
        temp_conv_text = text.replace("                                                    ", "")
        temp2_conv_text = temp_conv_text.replace("\n", "")
        conv_name = temp2_conv_text.replace("                                            ", "")
        conv_price = text2.replace("                                   ", ":")
        a.append(conv_name + ":" + conv_price)
    return a

def write_to_file(path, a):
    file = open(path, 'a')
    print(a)
    for i in range(len(a)):
        print(a[i])
        file.write(a[i] + '\n')
    file.close()

def main(url=None):
    tree = cnnct(url)
    a = get_data(tree)
    print(len(a))
    print(a)
    path = 'outdata.txt'
    write_to_file(path, a)

main('https://diy.by/catalog/instrument_and_electrical/976.html?PAGECOUNT=80&FIRSTLEVID=instrument_and_electrical&CATSECT=976&PAGEN_1=1')
main('https://diy.by/catalog/instrument_and_electrical/976.html?PAGECOUNT=80&FIRSTLEVID=instrument_and_electrical&CATSECT=976&PAGEN_1=2')