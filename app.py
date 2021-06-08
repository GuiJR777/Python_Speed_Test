import  speedtest
import eel

eel.init('app')

tester = speedtest.Speedtest()

def test_download():
    down = tester.download()
    down = f'{round(down/1000000, 3)} M/Bs'
    print(down)
    eel.write_result(f'Download: {down}', 'down')


def test_upload():
    up = tester.upload()
    up = f'{round(up/1000000, 3)} M/Bs'
    print(up)
    eel.write_result(f'Upload: {up}', 'up')

@eel.expose
def test():
    test_download()
    test_upload()
    eel.all_done()

eel.start('index.html', size=(800,600)) 