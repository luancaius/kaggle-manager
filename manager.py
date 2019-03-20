from service import Service


def options(number):
    service = Service()
    if number == 1:
        service.InitCompetition()
    elif number == 2:
        service.MakeSubmission()
    else:
        service.RunScript()


text = input("What do you want? 1-6")

options(int(text))

exit
