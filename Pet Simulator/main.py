from create_pet import create_pet
from hamster import hamster
from hamster import hamster
from take_care_of_pet import stuff
def main():
    print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   ▀█▀ █░█ █▀▀   █▀█ █▀▀ ▀█▀   █▀ █ █▀▄▀█ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ░█░ █▀█ ██▄   █▀▀ ██▄ ░█░   ▄█ █ █░▀░█ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄
𝕳𝖊𝖗𝖊 𝖞𝖔𝖚 𝖈𝖆𝖓 𝖈𝖗𝖊𝖆𝖙𝖊 𝖆 𝖕𝖊𝖙 𝖆𝖓𝖉 𝖓𝖆𝖒𝖊 𝖎𝖙 𝕿𝖆𝖐𝖊 
𝖈𝖆𝖗𝖊 𝖔𝖋 𝖞𝖔𝖚𝖗 𝖕𝖊𝖙 𝖆𝖓𝖉 𝖜𝖆𝖙𝖈𝖍 𝖎𝖙 𝖌𝖗𝖔𝖜 𝖚𝖕
""")
    ans = input("do you wanna create a pet (y/n): ")
    if ans.lower() in ["yes", "y"]:
        create_pet()
    elif ans.lower() in ["no", "n"]:
        print("ok bye")
        exit()
    else:
        print("bye then")

main()