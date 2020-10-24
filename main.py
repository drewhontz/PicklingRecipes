def create_qr_code(url, filepath):
    """
    Pass a url and a filepath; writes qr code to that dir
    :param url:
    :return:
    """
    import pyqrcode

    url = pyqrcode.create(url)
    url.svg(filepath, scale=8)
    url.terminal(quiet_zone=1)

if __name__ == '__main__':
    url_objects = {
        "curry_egg" : "https://docs.google.com/document/d/1fh9mbPZcDezq8uiIo4RKGTaFe5JwbxGbCMXDv7AOWUo/edit?usp=sharing",
        "daikon_carrots" : "https://docs.google.com/document/d/1yinoP4UbJ8J-LLV71MEdEg1Und7ObtUKmdAI79BTRzc/edit?usp=sharing",
        "peppers": "https://docs.google.com/document/d/1V4NQ_gs5-8C8a2uGs9iAgRc3FvGgTt4K0PfW9I9CUOU/edit?usp=sharing",
        "onions": "https://docs.google.com/document/d/1CNojyTiHxc4QZ_PaIuGwXdBPdODDg6jdDD5tTr1gGj0/edit?usp=sharing"

    }

    for k, v in url_objects.items():
        filepath = f"./qr_codes/{k}.svg"
        create_qr_code(v, filepath)

