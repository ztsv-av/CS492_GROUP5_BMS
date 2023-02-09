from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import *


scheduler = BackgroundScheduler()
scheduler.add_job(check_book, 'interval', seconds=86400)
scheduler.add_job(check_mfg, 'interval', seconds=86400)


def start_scheduler():
	scheduler.start()
