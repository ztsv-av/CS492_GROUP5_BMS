from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *


def start_scheduler():
	scheduler = BackgroundScheduler()
	scheduler.add_job(check_book, 'interval', seconds=86400)
	scheduler.start()
