import time
import hetzner_utils
import check_utils

CONFIG = {
    'domain': 'example.com',
    'user': 'root',
    'timeout': 5,
    'interval': 60 * 3
}


def maintain():
    while True:
        try:
            check_utils.check_ip(CONFIG['domain'], CONFIG['user'], CONFIG['timeout'])
        except Exception as e:
            hetzner_utils.change_ip()
        time.sleep(CONFIG['interval'])


maintain()
