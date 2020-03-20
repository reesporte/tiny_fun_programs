import random

def answer():
    choices = "It is certain. ● It is decidedly so. ● Without a doubt. ● Yes - definitely. ● You may rely on it. ● As I see it, yes.● Most likely.● Outlook good.● Yes.● Signs point to yes.● Reply hazy, try again.● Ask again later.● Better not tell you now.● Cannot predict now.● Concentrate and ask again.● Don't count on it.● My reply is no.● My sources say no.● Outlook not so good.● Very doubtful."
    choices = choices.split("●")
    return random.choice(choices)

def main():
    x = input("What do you want to know? \n>> ")
    while x != "stop":
        print(answer())
        x = input("What do you want to know? \n>> ")

if __name__ == '__main__':
    main()
