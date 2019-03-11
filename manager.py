import service


def options(number):
    switcher = {
        1: service.CreateInitialScript(""),
        2: service.DownloadData,
        3: service.MakeSubmission,
        4: service.ReadSettings,
        5: service.RunScript,
        6: service.SendEmail,
    }
    switcher[number]()


text = input("What do you want? 1-6")

options(text)
