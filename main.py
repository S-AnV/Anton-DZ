import requests as rq
import logging.config


log_config = {
    'version': 1,
    'formatters': {
        'primes_formatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'main_formatter': {
            'format': '%(levelname)s: %(message)s'
        }
    },
    'handlers': {
        'success_responses_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'main_formatter',
            'filename': 'success_responses.log',
            'mode': 'w',
            'encoding': 'utf-8'
        },
        'bad_responses_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'main_formatter',
            'filename': 'bad_responses.log',
            'mode': 'w',
            'encoding': 'utf-8'
        },
        'blocked_responses_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'main_formatter',
            'filename': 'blocked_responses.log',
            'mode': 'w',
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        'RequestsLogger_1': {
            'handlers': ['success_responses_handler'],
            'level': 'DEBUG',
        },
        'RequestsLogger_2': {
            'handlers': ['bad_responses_handler'],
            'level': 'DEBUG',
        },
        'RequestsLogger_3': {
            'handlers': ['blocked_responses_handler'],
            'level': 'DEBUG',
        },
    },
}

logging.config.dictConfig(log_config)
log_1 = logging.getLogger('RequestsLogger_1')
log_2 = logging.getLogger('RequestsLogger_2')
log_3 = logging.getLogger('RequestsLogger_3')


sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if str(response) == '<Response [200]>':
            log_1.info(f'{site}, response - {str(response)[-5:-2]}')
        else:
            log_2.warning(f'{site}, response - {str(response)[-5:-2]}')
    except Exception as ext:
        log_3.error(f'{site}, NO CONNECTION\n{ext}')