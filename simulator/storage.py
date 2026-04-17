import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import random
from datetime import datetime
from api.app import app, db
from api.models import Volume


def simulate_storage_activity():
    """
    Simulates real storage activity on all volumes.
    Runs every 30 seconds forever.
    """
    print("StorageOps Simulator started!")
    print("Checking storage every 30 seconds...")
    print("-" * 40)

    while True:
        with app.app_context():

            # Get all volumes from database
            volumes = Volume.query.all()

            if not volumes:
                print("No volumes found. Create some volumes first!")
            else:
                for volume in volumes:

                    # Simulate random data being written
                    # Between 5 and 50 GB added each cycle
                    data_added = random.randint(5, 50)

                    # Don't exceed total capacity
                    new_used = min(
                        volume.used_capacity_gb + data_added,
                        volume.total_capacity_gb
                    )
                    volume.used_capacity_gb = new_used

                    # Simulate performance metrics
                    iops = random.randint(100, 5000)
                    latency = round(random.uniform(0.5, 20.0), 2)
                    throughput = round(random.uniform(10, 500), 2)

                    # Print what's happening
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                          f"{volume.name} → "
                          f"{volume.used_capacity_gb}/{volume.total_capacity_gb} GB "
                          f"({volume.utilization_pct}%) "
                          f"IOPS:{iops} "
                          f"Latency:{latency}ms")

                    # Check if critical
                    if volume.is_critical:
                        print(f"🚨 ALERT: {volume.name} is CRITICAL "
                              f"at {volume.utilization_pct}%!")

                db.session.commit()

            print("-" * 40)

        # Wait 30 seconds before next check
        time.sleep(30)


if __name__ == '__main__':
    simulate_storage_activity()