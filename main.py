import time
import hetzner_utils
import check_utils


def maintain():
    while True:
        try:
            check_utils.check_ip('example.com', 'root', 5)
        except Exception as e:
            hetzner_utils.change_ip()
        time.sleep(60*3)


maintain()
