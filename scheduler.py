from apscheduler.schedulers.blocking import BlockingScheduler
import os

scheduler = BlockingScheduler()

# Run every 1 minute
@scheduler.scheduled_job('interval', minutes=1)
def run_pipeline():
    print("Running Data Pipeline...")

    os.system("python clean_data.py")
    os.system("python analysis.py")

    print("Pipeline Completed!")

scheduler.start()