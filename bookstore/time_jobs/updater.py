from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *


def start_books():
	scheduler = BackgroundScheduler()
	scheduler.add_job(check_book, 'interval', seconds=86400)
	scheduler.start()


def start_mfg():
	scheduler = BackgroundScheduler()
	scheduler.add_job(check_mfg, 'interval', seconds=86400)
	scheduler.start()