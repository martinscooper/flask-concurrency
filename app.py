from crypt import methods
from flask import Flask
import threading
from time import time

app = Flask(__name__)

@app.route('/', methods=['POST'])
def check_concurrency():
    def cpu_consuming_task(i):
            for a in range(i):
                j = a * i

    def run():
        print('* ' * 20)
        init = time()
        t = init
        for i in range(3):
            cpu_consuming_task(30000000)
            nt = time()
            #print(f"thread:{threading.get_ident()} i took {nt - t}")
            t = nt
        print(f'thread({threading.get_ident()}) total time was: {time()-init}')
        print('* ' * 20)

    threading.Thread(target=run).start()
    return "started"
