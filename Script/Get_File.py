import os
import io
import shutil
import time
import requests

RULE_URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/"
REJECT_RULES = {
    "Advertising": RULE_URL + "Advertising/Advertising.list",
    "Privacy": RULE_URL + "Privacy/Privacy.list",
}
PROXY_RULES = {
    "GlobalMedia": RULE_URL + "GlobalMedia/GlobalMedia.list",
    "Global": RULE_URL + "Global/Global.list",
    "Proxy": RULE_URL + "Proxy/Proxy.list",
}
DIRECT_RULES = {
    "ChinaMax": RULE_URL + "ChinaMax/ChinaMax.list",
}

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

def load_file(rules_dict, file_dir):
    """
    下载规则文件
    """
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
        
    for key in rules_dict:
        response = requests.get(rules_dict[key], headers=HEADER)
        if response.status_code == 200:
            with open(f"./{file_dir}/{key}.list", "wb") as f:
                with response, io.BytesIO(response.content) as stream:
                    shutil.copyfileobj(stream, f)
            time.sleep(1)

def remove():
    """
    移除所有规则文件
    """
    shutil.rmtree("Reject_Rule")
    shutil.rmtree("Proxy_Rule")
    shutil.rmtree("Direct_Rule")
    print("移除所有文件夹")

if __name__ == '__main__':
    remove()
    load_file(REJECT_RULES, "Reject_Rule")
    load_file(PROXY_RULES, "Proxy_Rule")
    load_file(DIRECT_RULES, "Direct_Rule")